from django.contrib.auth import get_user_model
from django.db.models import Q
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet, ViewSet
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from rest_framework.relations import ManyRelatedField
from rest_framework.metadata import SimpleMetadata

from rest_framework_guardian import filters

from guardian.shortcuts import get_objects_for_user
from guardian.core import ObjectPermissionChecker
from cacheops import cached_view_as

from app.api import serializers
# from app.permissions import BaseModelPermissions
from app import models
from pprint import pprint
from itertools import chain
from app import utils
import json


CLASE_EVALUARE = {
    1: 'A',
    2: 'B',
    3: 'C',
}

CLASE_PRIORITIZARE = {
    1: {
        'id': 1,
        'value': '1-5'
        },
    2: {
        'id': 1,
        'value': '1-5'
        },
    3: {
        'id': 1,
        'value': '1-5'
        },
    4: {
        'id': 1,
        'value': '1-5'
        },
    5: {
        'id': 1,
        'value': '1-5'
        },
    6: {
        'id': 2,
        'value': '5-10'
        },
    7: {
        'id': 2,
        'value': '5-10'
        },
    8: {
        'id': 2,
        'value': '5-10'
        },
    9: {
        'id': 2,
        'value': '5-10'
        },
    10: {
        'id': 2,
        'value': '5-10'
        },
    11: {
        'id': 3,
        'value': '10-15'
        },
    12: {
        'id': 3,
        'value': '10-15'
        },
    13: {
        'id': 3,
        'value': '10-15'
        },
    14: {
        'id': 3,
        'value': '10-15'
        },
    15: {
        'id': 3,
        'value': '10-15'
        },
}


@method_decorator(cached_view_as(models.BisericaPage, models.IdentificarePage, models.DescrierePage, models.ComponentaArtisticaPage, models.ConservarePage, models.ValoarePage, models.IstoricPage), name='dispatch')
@method_decorator(csrf_exempt, name='dispatch')
class BisericaViewSet(ModelViewSet): 
    serializer_class = serializers.BisericaListSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.BisericaListSerializer 
        return serializers.BisericaSerializer

    def get_queryset(self):
        ignored_fields = ['formsubmission', 'page__revisions', "redirect","sites_rooted_here","aliases","revisions","group_permissions","view_restrictions","workflowpage","workflow_states","wagtail_admin_comments"]
        queryset = models.BisericaPage.objects.live()
        if self.action == 'retrieve':
            prefetch_list = []
            select_list = []
            for field in models.BisericaPage._meta.fields:
                if '_page' in field.name:
                    for related_field in field.related_model._meta.fields:
                        if related_field.get_internal_type() == 'ForeignKey':
                            select_list.append(f"{field.name}__{related_field.name}")
                    for related_field in field.related_model._meta.fields_map:
                        if related_field not in ignored_fields and '+' not in related_field:
                            if 'poze_' in related_field:
                                prefetch_list.append(f"{field.name}__{related_field}")
                                # prefetch_list.append(f"{field.name}__{related_field}__poza")
                            else:
                                prefetch_list.append(f"{field.name}__{related_field}")

            if select_list:
                queryset = queryset.select_related(*select_list)
            if prefetch_list:
                queryset = queryset.prefetch_related(*prefetch_list)

        return queryset

    @action(
        methods=["post"],
        detail=False,
        name="Map filter",
        url_path="filter",
    )
    def map_filter(self, request):
        biserici = utils.filter_biserici(request.data)
        # biserici = [x for x in biserici]
        serializer = serializers.BisericaListSerializer(biserici, many=True)
        return Response(serializer.data)

    def list(self, request):
        query = request.GET.get('query', None)
        if query:
            q = Q(utitle__icontains=query) | Q(cod__icontains=query) | Q(identificare_page__localitate__nume__icontains=query)
            biserici = models.BisericaPage.objects.filter(q)
        else:
            biserici = models.BisericaPage.objects.live()
        serializer = serializers.BisericaListSerializer(biserici, many=True)
        return Response(serializer.data)

    def get(self, request, pk, format=None):
        biserica = self.get_object(pk)
        serializer = BisericaSerializer(biserica)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        biserica = self.get_object()
        serializer = serializers.BisericaSerializer(biserica)
        data = {}
        data['tabs'] = []
        for key, value in serializer.data.items():
            if '_page' in key:
                if value:
                    if value['type'] == 'sections' and  value['sections'] or value['type'] == 'embed' and value['embed']:
                        data['tabs'].append(value)
            else:
                data[key] = value

        return Response(data)

# @method_decorator(cached_view_as(models.BisericaPage, models.IdentificarePage, models.DescrierePage, models.ComponentaArtisticaPage, models.ConservarePage, models.ValoarePage, models.IstoricPage), name='dispatch')
@method_decorator(csrf_exempt, name='dispatch')
class FiltersView(ViewSet):

    # @method_decorator(cache_page(60 * 60 * 24 * 31))
    def list(self, request):
        """
        Return a list of all users.
        """
        identificare_filters_name = {
            '': ['statut', 'hram', 'cult', 'utilizare', 'singularitate', 'functiune',
                'functiune_initiala', 'proprietate_actuala', 'inscriere_documente_cadastrale']
             }
        identificare_filters = utils.get_chapter_filters(
            models.IdentificarePage, identificare_filters_name)

        istoric_filters_name = {
            '': ['datare_prin_interval_timp', 'an_constructie', 'datare_secol', 'are_pisanie', 'are_studiu_dendro',
                'are_mutari', 'lista_ctitori', 'lista_mesteri', 'lista_zugravi', 'lista_personalitati']
            }
        istoric_filters = utils.get_chapter_filters(
            models.IstoricPage, istoric_filters_name)
        # print('----')
        # pprint(istoric_filters)
        # print('----')
        descriere_filters_name = {
            'Tip scanare': [
                'are_scanare_laser', 'are_model_fotogrametric'
            ],
            'Localizare/Peisaj': [
                "amplasament", "topografie", "relatia_cu_cimitirul", "peisagistica_sitului", "ansamblu_construit"
            ],
            'Arhitectura bisericii': [
                "materiale", "planimetria_bisericii", "numar_accese_naos", "numar_accese_pronaos", "numar_accese_altar",
                "numar_ochiesi", "solee", "bolta_peste_pronaos",
                "bolta_peste_naos", "bolta_peste_altar", "bolta_peste_pronaos_structura", "bolta_peste_naos_structura", "bolta_peste_altar_structura",
                "bolta_peste_altar_tip",
                "cor", "sarpanta_tip", "turn_tip", "numar_clopote", "fundatia","sistem_structural", "sistem_in_cheotoare", "sistem_in_catei",
                "tiranti_tip", "finisaj_exterior_tip", "invelitoare_corp_material", "invelitoare_corp_sindrila_numar_straturi", "invelitoare_corp_sindrila_cu_horj", "invelitoare_corp_sindrlia_tipul_de_batere",
                "invelitoare_corp_sindrlia_forma_botului", "invelitoare_corp_sindrila_cu_tesitura", "invelitoare_corp_sindrlia_prelucrare", "invelitoare_corp_sindrlia_esenta_lemnoasa",
                "invelitoare_turn_material", "invelitoare_turn_sindrila_numar_straturi", "invelitoare_turn_sindrila_cu_horj", "invelitoare_turn_sindrlia_tipul_de_batere",
                "invelitoare_turn_sindrlia_forma_botului", "invelitoare_turn_sindrila_cu_tesitura", "invelitoare_turn_sindrlia_prelucrare", "invelitoare_turn_sindrlia_esenta_lemnoasa"
            ],
        }
        descriere_filters = utils.get_chapter_filters(
            models.DescrierePage, descriere_filters_name)

        componenta_artistica_name = {
            '': [
                    "suport_proscomidie", "obiecte_de_cult", "mobiliere", "obiecte_instrainate"
                ],
            'Iconostasul': [
                    "iconostas_naos_altar_tip", "iconostas_naos_altar_materiale", "iconostas_naos_altar_tehnica", "iconostas_naos_altar_registre", "iconostas_naos_altar_tip_usi"
            ],
            'Perete desp??r??itor (??ntre pronaos ??i naos)': [
                    "iconostas_pronaos_naos_tip", "iconostas_pronaos_naos_tehnica", "iconostas_pronaos_naos_tehnica", 
            ],
            'Altar': [
                'altar_placa_mesei', 'altar_piciorul_mesei'
            ],
            'Pictur?? exterioar??': [
                'pictura_exterioara_localizare', 'pictura_exterioara_suport', 'pictura_exterioara_tehnica', 'pictura_exterioara_numar_straturi_pictura',
                'pictura_exterioara_datare_secol', 'pictura_exterioara_sursa_datare'
            ],
            'Pictur?? interioar??': [
                'pictura_interioara_localizare', 'pictura_interioara_suport', 'pictura_interioara_tehnica_pictura', 'pictura_interioara_numar_straturi_pictura',
                'pictura_interioara_datare_secol', 'pictura_interioara_sursa_datare'
            ],
            'Interven??ii': [
                'elemente_interventii'
            ]
         }
        componenta_artistica_filters = utils.get_chapter_filters(
            models.ComponentaArtisticaPage, componenta_artistica_name)


        conservare_filters_name = {
            'Sit': [
                "sit",
                "sit_pericol",
                "elemente_arhitecturale",
                "elemente_arhitecturale_pericol",
                "alte_elemente_importante",
                "alte_elemente_importante_pericol",
                "vegetatie",
                "vegetatie_pericol",
            ],
            'Strucutra bisericii': [
                "teren",
                "teren_pericol",
                "fundatii",
                "fundatii_pericol",
                "talpi",
                "talpi_pericol",
                "corp_biserica",
                "corp_biserica_pericol",
                "bolti",
                "bolti_pericol",
                "cosoroabe",
                "cosoroabe_pericol",
                "sarpanta_peste_corp_biserica",
                "sarpanta_peste_corp_biserica_pericol",
                "turn",
                "turn_pericol",
            ],
            'Finisaje biseric??': [
                "zona_din_jurul_biserici",
                "zona_din_jurul_biserici_pericol",
                "pardoseli_interioare",
                "pardoseli_interioare_pericol",
                "finisaj_exterior",
                "finisaj_exterior_pericol",
                "finisaj_pereti_interiori",
                "finisaj_pereti_interiori_pericol",
                "finisaj_tavane_si_bolti",
                "finisaj_tavane_si_bolti_pericol",
                "tamplarii",
                "tamplarii_pericol",
                "invelitoare_sarpanta_si_turn",
                "invelitoare_sarpanta_si_turn_pericol",
                "instalatie_electrica",
                "instalatie_electrica_pericol",
                "instalatie_termica",
                "instalatie_termica_pericol",
                "paratraznet",
                "paratraznet_pericol",
            ],
            'Componenta Artistic??': [
                "strat_pictural",
                "strat_pictural_pericol",
                "obiecte_de_cult",
                "obiecte_de_cult_pericol",
                "mobilier",
                "mobilier_pericol",
            ]
            }
        advanced_conservare_filters = utils.get_chapter_filters(
            models.ConservarePage, conservare_filters_name)

        valoare_filters_name =  {
            '': ["vechime", "integritate", "unicitate", "valoare_memoriala", "peisaj_cultural", "valoare_sit", "estetica", "mestesug", "pictura", "folosinta_actuala", "relevanta_actuala", "potential"]}
        advanced_valoare_filters = utils.get_chapter_filters(
            models.ValoarePage, valoare_filters_name)

        localitati_filters = []
        judete_filters = []
        conservare_filters = []
        valoare_filters = []
        prioritizare_filters = []

        localitati_active = models.BisericaPage.objects.live().values(
            'identificare_page__localitate__id', 'identificare_page__localitate__nume', 'identificare_page__localitate__judet__id' ,'identificare_page__localitate__judet__nume')

        for localitate in localitati_active:
            if localitate['identificare_page__localitate__id']:
                localitate_item = {
                    'id': localitate['identificare_page__localitate__id'],
                    'value': localitate['identificare_page__localitate__nume'],
                    'judet': localitate['identificare_page__localitate__judet__id'],
                    }

                if localitate_item not in localitati_filters:
                    localitati_filters.append(localitate_item)

                    judet_item = {
                        'id': localitate['identificare_page__localitate__judet__id'],
                        'value': localitate['identificare_page__localitate__judet__nume'],
                    }
                    if judet_item not in judete_filters:
                        judete_filters.append(judet_item)

        biserici = models.BisericaPage.objects.live().values('valoare_page__total', 'conservare_page__total')

        for biserica in biserici:
            if biserica['conservare_page__total']:
                conservare_item = {
                    'id': round(biserica['conservare_page__total']),
                    'value': round(biserica['conservare_page__total']),
                }
                if conservare_item not in conservare_filters:
                    conservare_filters.append(conservare_item)
            if biserica['valoare_page__total']:
                valoare_item = {
                    'id': round(biserica['valoare_page__total']),
                    'value': CLASE_EVALUARE[round(biserica['valoare_page__total'])],
                }
                if valoare_item not in valoare_filters:
                    valoare_filters.append(valoare_item)

            if biserica['conservare_page__total'] and biserica['valoare_page__total']:
                prioritizare = biserica['conservare_page__total'] * biserica['valoare_page__total']

                prioritizare_item = {
                    'id': CLASE_PRIORITIZARE[round(prioritizare)]['id'],
                    'value': CLASE_PRIORITIZARE[round(prioritizare)]['value'],
                }
                if prioritizare_item not in prioritizare_filters:
                    prioritizare_filters.append(prioritizare_item)

        response = {
            'basic': {
                'judet': judete_filters,
                'localitate': localitati_filters,
                'conservare': sorted(conservare_filters, key=lambda d: d['id']) ,
                'valoare': sorted(valoare_filters, key=lambda d: d['id']),
                'prioritizare': sorted(prioritizare_filters, key=lambda d: d['id']),
            },
            'advanced': [
                {
                    'title': 'Identificare',
                    'key': 'identificare',
                    'sections': identificare_filters,
                },
                {
                    'title': 'Istoric',
                    'key': 'istoric',
                    'sections': istoric_filters,
                },
                {
                    'title': 'Descriere Arhitectur?? / Peisaj',
                    'key': 'descriere',
                    'sections': descriere_filters,
                },
                {
                    'title': 'Descriere Componenta Artistic??',
                    'key': 'componenta_artistica',
                    'sections': componenta_artistica_filters,
                },
                {
                    'title': 'Conservare',
                    'key': 'conservare',
                    'sections': advanced_conservare_filters,
                },
                {
                    'title': 'Valoare',
                    'key': 'valoare',
                    'sections': advanced_valoare_filters,
                },
            ]
        }
        return Response(response)

    @method_decorator(csrf_exempt)
    @action(
        methods=["post"],
        detail=False,
        name="Filters preview",
        url_path="preview",
    )
    def filters_preview(self, request):
        response = {
            'count': utils.filter_biserici(request.data).count()
        }
        return Response(response)


@method_decorator(csrf_exempt, name='dispatch')
class AboutViewSet(ViewSet):

    def list(self, request):
        about_page = models.AboutPage.objects.last()
        about_serializer = serializers.AboutSerializer(about_page)
        return Response(about_serializer.data)
