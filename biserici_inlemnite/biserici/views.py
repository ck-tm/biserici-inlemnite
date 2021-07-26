# from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.views.generic.list import ListView
from django.views.generic import View
from django.views.generic.detail import SingleObjectMixin, DetailView
from django.views.generic.edit import UpdateView
from django.http import HttpResponse
from django.urls import reverse
from django.utils import timezone
from django.shortcuts import redirect
from django.db.models import Count
from biserici import models, forms
from django_filters.views import FilterView

from guardian.shortcuts import get_objects_for_user
from guardian.core import ObjectPermissionChecker

# @user_passes_test(lambda u: u.is_superuser)
class BisericiView(FilterView):
    model = models.Biserica
    # paginate_by = 20
    template_name = "biserici/biserici.html"
    # filterset_class = filters.ProgramStudiuFacultateFilter

    def get_queryset(self):
        queryset = super().get_queryset().prefetch_related('identificare__judet', 'identificare__localitate')
        user = self.request.user
        return get_objects_for_user(user, 'biserici.view_biserica')

class BisericaView(DetailView):

    model = models.Biserica
    slug_field = 'pk'
    slug_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context

    def get(self, request, *args, **kwargs):
        user = self.request.user
        obj = self.get_object()
        checker = ObjectPermissionChecker(user)
        for capitol in ['identificare', 'istoric', 'descriere', 'patrimoniu', 'conservare']:
            if checker.has_perm(f'change_{capitol}', getattr(obj, capitol)):
                url = reverse(capitol, args=[obj.pk])
                return redirect(url)

class UpdateChapterMixin(object):
    template_name = "biserici/form_capitol.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['biserica'] = self.object.biserica
        context['active_page'] = self.model._meta.model_name
        return context

    def get_object(self, queryset=None):
        return self.model.objects.get(biserica__pk=self.kwargs['biserica_pk'])

    def get_success_url(self):
        return reverse(self.model._meta.model_name, kwargs={'biserica_pk': self.object.biserica.pk})

    def form_valid(self, form):
        """
        If the form is valid, save the associated model.
        """
        user = self.request.user
        self.object = form.save()
        instance = form.instance
        instance.last_edit_date = timezone.now()
        instance.last_edit_user = user
        instance.save()
        biserica = instance.biserica
        biserica.last_edit_date = timezone.now()
        biserica.last_edit_user = user
        biserica.save()
        return super().form_valid(form)

class IdentificareBisericaView(UpdateChapterMixin, UpdateView):
    model = models.Identificare
    form_class = forms.IdentificareForm


class DescriereBisericaView(UpdateChapterMixin, UpdateView):
    model = models.Descriere
    form_class = forms.DescriereForm


class IstoricBisericaView(UpdateChapterMixin, UpdateView):
    model = models.Istoric
    form_class = forms.IstoricForm


class PatrimoniuBisericaView(UpdateChapterMixin, UpdateView):
    model = models.Patrimoniu
    form_class = forms.PatrimoniuForm


class ConservareBisericaView(UpdateChapterMixin, UpdateView):
    model = models.Conservare
    form_class = forms.ConservareForm
