# from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.views.generic.list import ListView
from django.views.generic import View
from django.views.generic.detail import SingleObjectMixin, DetailView
from django.http import HttpResponse
from django.db.models import Count
from biserici import models
from django_filters.views import FilterView


# @user_passes_test(lambda u: u.is_superuser)
class BisericiView(FilterView):
    model = models.Biserica
    # paginate_by = 20
    template_name = "biserici/biserici.html"
    # filterset_class = filters.ProgramStudiuFacultateFilter

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     universitati_pk = []
    #     similar_rncis = {}
    #     ani_programe = {}
    #     programe_pks = context["object_list"].values_list('pk', flat=True)

    #     for program in context["object_list"]:
    #         universitati_pk.append(program.facultate.universitate.pk)
    #         if program.program:
    #             similar_rncis[program.pk] = anc_models.Program.objects.filter(
    #                 nume__trigram_similar=program.program.nume, link_universitate=program.facultate.universitate
    #             )
    #     for program in models.ProgramStudiuFacultate.objects.filter(pk__in=programe_pks).values('pk', 'studenti__absolviri__an_calendaristic__an_inceput').annotate(c=Count('studenti__absolviri__an_calendaristic__an_inceput')).order_by('studenti__absolviri__an_calendaristic__an_inceput'):
    #         ani_programe.setdefault(program['pk'], {})
    #         if program['studenti__absolviri__an_calendaristic__an_inceput']:
    #             ani_programe[program['pk']][program['studenti__absolviri__an_calendaristic__an_inceput']] = program['c']

    #     context["rncis_dict"] = {x.pk: x.anc.all() for x in models.Universitate.objects.filter(pk__in=universitati_pk)}
    #     context["similar_rncis"] = similar_rncis
    #     context["ani_programe"] = ani_programe

        # return context

    def get_queryset(self):
        queryset = super().get_queryset().prefetch_related('identificare__judet', 'identificare__localitate')
        # return filters.ProgramStudiuFacultateFilter(
        #   self.request.GET, queryset=queryset).qs
        return queryset

class BisericaView(DetailView):

    model = models.Biserica
    slug_field = 'pk'
    slug_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['now'] = timezone.now()
        print(context)
        return context