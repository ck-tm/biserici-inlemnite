from django.conf import settings
from django.core.paginator import Paginator
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.urls import reverse
from django.conf import settings
from wagtail.admin.auth import user_has_any_page_permission, user_passes_test
from wagtail.admin.navigation import get_explorable_root_page
from wagtail.core import hooks
from wagtail.core.models import Page, UserPagePermissionsProxy

from django.views.generic import DetailView, RedirectView, UpdateView
from django.views.generic.list import ListView

from app import models

from meta.views import MetadataMixin
from django_json_ld.views import JsonLdDetailView

@user_passes_test(user_has_any_page_permission)
def wagtail_pages(request, parent_page_id=None):
    if parent_page_id:
        parent_page = get_object_or_404(Page, id=parent_page_id)
    else:
        parent_page = Page.get_first_root_node()

    # This will always succeed because of the @user_passes_test above.
    root_page = get_explorable_root_page(request.user)

    # If this page isn't a descendant of the user's explorable root page,
    # then redirect to that explorable root page instead.
    if not (
        parent_page.pk == root_page.pk
        or parent_page.is_descendant_of(root_page)
    ):
        return redirect('wagtailadmin_explore', root_page.pk)

    parent_page = parent_page.specific

    user_perms = UserPagePermissionsProxy(request.user)
    pages = (
        parent_page.get_children().prefetch_related(
            "content_type", "sites_rooted_here"
        )
        & user_perms.explorable_pages()
    )

    # Get page ordering
    ordering = request.GET.get('ordering', 'title')
    if ordering not in [
        'title',
        '-title',
        'content_type',
        '-content_type',
        'live', '-live',
        'latest_revision_created_at',
        '-latest_revision_created_at',
        'ord'
    ]:
        ordering = '-latest_revision_created_at'

    if ordering == 'ord':
        # preserve the native ordering from get_children()
        pass
    elif ordering == 'latest_revision_created_at':
        # order by oldest revision first.
        # Special case NULL entries - these should go at the top of the list.
        # Do this by annotating with Count('latest_revision_created_at'),
        # which returns 0 for these
        pages = pages.annotate(
            null_position=Count('latest_revision_created_at')
        ).order_by('null_position', 'latest_revision_created_at')
    elif ordering == '-latest_revision_created_at':
        # order by oldest revision first.
        # Special case NULL entries - these should go at the end of the list.
        pages = pages.annotate(
            null_position=Count('latest_revision_created_at')
        ).order_by('-null_position', '-latest_revision_created_at')
    else:
        pages = pages.order_by(ordering)

    # Don't paginate if sorting by page order - all pages must be shown to
    # allow drag-and-drop reordering
    do_paginate = ordering != 'ord'

    if do_paginate or pages.count() < 100:
        # Retrieve pages in their most specific form, so that custom
        # get_admin_display_title and get_url_parts methods on subclasses are respected.
        # However, skip this on unpaginated listings with >100 child pages as this could
        # be a significant performance hit. (This should only happen on the reorder view,
        # and hopefully no-one is having to do manual reordering on listings that large...)
        pages = pages.specific(defer=True)

    # allow hooks to modify the queryset
    for hook in hooks.get_hooks('construct_explorer_page_queryset'):
        pages = hook(parent_page, pages, request)

    # Pagination
    if do_paginate:
        paginator = Paginator(pages, per_page=50)
        pages = paginator.get_page(request.GET.get('p'))

    context = {
        'parent_page': parent_page.specific,
        'ordering': ordering,
        'pagination_query_params': "ordering=%s" % ordering,
        'pages': pages,
        'do_paginate': do_paginate,
        'locale': None,
        'translations': [],
    }

    if getattr(settings, 'WAGTAIL_I18N_ENABLED', False) and not parent_page.is_root():
        context.update({
            'locale': parent_page.locale,
            'translations': [
                {
                    'locale': translation.locale,
                    'url': reverse('wagtailadmin_explore', args=[translation.id]),
                }
                for translation in parent_page.get_translations().only('id', 'locale').select_related('locale')
            ],
        })

    return TemplateResponse(request, 'wagtailadmin/pages/index.html', context)

class BisericiView(MetadataMixin, ListView):
    template_name = 'app/meta_base.html'
    model = models.BisericaPage
    title = 'Biserici ??nlemnite'
    object_type = 'website'
    description = 'Biserici ??nlemnite a venit ca un r??spuns la una dintre cele mai mari probleme ale p??str??rii ??i gestion??rii bisericilor de lemn de patrimoniu din Rom??nia: lipsa informa??iilor privind num??rul, starea ??i valoarea lor.'
    image = '/static/images/logo.png'
    url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sd'] =  {
          "@context": "https://schema.org/",
          "@type": "website",
          "url": "https://biserici-inlemnite.ro/",
          "name": "Biserici ??nlemnite",
          "description": "Biserici ??nlemnite a venit ca un r??spuns la una dintre cele mai mari probleme ale p??str??rii ??i gestion??rii bisericilor de lemn de patrimoniu din Rom??nia: lipsa informa??iilor privind num??rul, starea ??i valoarea lor.",
          "image": '/static/images/logo.png'
        }
        return context

class BisericaDetailView(MetadataMixin, JsonLdDetailView):
    template_name = 'app/meta_biserica.html'
    model = models.BisericaPage
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.get_object())
        print(self.get_object().as_meta(self.request))
        context['meta'] = self.get_object().as_meta(self.request)
        return context


