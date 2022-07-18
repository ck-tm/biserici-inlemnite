# from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.contrib.contenttypes.models import ContentType

from django.views.generic.list import ListView
from django.views.generic import View
from django.views.generic.detail import SingleObjectMixin, DetailView
from django.views.generic.edit import UpdateView, CreateView
from django.http import HttpResponse
from django.urls import reverse
from django.utils import timezone
from django.shortcuts import redirect
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from biserici import models, forms, mixins
from django_filters.views import FilterView

from guardian.shortcuts import get_objects_for_user, get_perms
from guardian.core import ObjectPermissionChecker

# @user_passes_test(lambda u: u.is_superuser)
@method_decorator(login_required, name='dispatch')
class BisericiView(FilterView):
    model = models.Biserica
    # paginate_by = 20
    template_name = "biserici/biserici.html"
    # filterset_class = filters.ProgramStudiuFacultateFilter

    def get_queryset(self):
        queryset = super().get_queryset().prefetch_related('identificare__judet', 'identificare__localitate')
        user = self.request.user
        # checker = ObjectPermissionChecker(user)
        # for obj in queryset:
        #     print(obj)
        #     print(checker.get_user_perms(obj))
        #     print(checker.get_group_perms(obj))
        #     print(get_perms(user, obj))
        # print(get_objects_for_user(user, 'biserici.change_biserica'))
        # print(user)
        return queryset
        return get_objects_for_user(user, 'biserici.change_biserica')

    # def get(self, request, *args, **kwargs):
        # user = self.request.user
        # if 'editor' in user.groups.values_list('name', flat=True):
            # return redirect("admin:index")
        # return super().get(request, *args, **kwargs)

@method_decorator(login_required, name='dispatch')
class BisericaView(DetailView):

    model = models.Biserica
    slug_field = 'pk'
    slug_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        user = self.request.user
        obj = self.get_object()
        checker = ObjectPermissionChecker(user)
        # print(dir(checker))
        # print(checker.get_user_perms(obj))
        # print(checker.get_group_perms(obj))
        # print(get_objects_for_user(user, 'biserici.change_biserica'))
        # for i in models.Identificare.objects.all():
        #     i.save(force_update=True)
        #     print(i)
        for capitol in ['identificare', 'istoric', 'descriere', 'patrimoniu', 'conservare']:
            if checker.has_perm(f'biserici.change_{capitol}', getattr(obj, capitol)):
                url = reverse(capitol, args=[obj.pk])
                return redirect(url)
        return super().get(request, *args, **kwargs)


class UpdateChapterMixin(object):
    template_name = "biserici/form_capitol.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        obj = self.get_object()
        checker = ObjectPermissionChecker(user)
        # print(dir(checker))
        user_permissions = []
        for chapter in ['identificare', 'istoric', 'descriere', 'patrimoniu', 'conservare']:
            user_permissions += checker.get_perms(getattr(obj.biserica, chapter))
        # print(user_permissions)
        context['user_permissions'] = user_permissions
        context['biserica'] = self.object.biserica
        context['active_page'] = self.model._meta.model_name
        return context

    def get_object(self, queryset=None):
        return self.model.objects.get(biserica__pk=self.kwargs['biserica_pk'])

    def get_success_url(self):
        return reverse(self.model._meta.model_name, kwargs={'biserica_pk': self.object.biserica.pk})

    # def form_valid(self, form):
    #     """
    #     If the form is valid, save the associated model.
    #     """
    #     user = self.request.user
    #     self.object = form.save()
    #     return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class IdentificareBisericaView(UpdateChapterMixin, UpdateView):
    model = models.Identificare
    form_class = forms.IdentificareForm


@method_decorator(login_required, name='dispatch')
class DescriereBisericaView(UpdateChapterMixin, UpdateView):
    model = models.Descriere
    form_class = forms.DescriereForm


# @method_decorator(login_required, name='dispatch')
# class IstoricBisericaView(UpdateChapterMixin, UpdateView):
#     model = models.Istoric
    # form_class = forms.IstoricForm


@method_decorator(login_required, name='dispatch')
class PatrimoniuBisericaView(UpdateChapterMixin, UpdateView):
    model = models.Patrimoniu
    form_class = forms.PatrimoniuForm


@method_decorator(login_required, name='dispatch')
class ConservareBisericaView(UpdateChapterMixin, UpdateView):
    model = models.Conservare
    form_class = forms.ConservareForm


class ContentCreateView(mixins.JsonableResponseMixin, CreateView):
    template_name='biserici/snippets/create_form.html'
    fields='__all__'

    def dispatch(self, request, *args, **kwargs):
        model_name = kwargs['model_name'].lower()
        model = ContentType.objects.get_by_natural_key('biserici', model_name)
        self.model = model.model_class()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # print(context)
        context['title'] = self.model._meta.object_name
        # print(self.model)
        return context

    def get_success_url(self):
        return '%'


