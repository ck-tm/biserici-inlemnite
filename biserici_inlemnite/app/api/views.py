from django.contrib.auth import get_user_model
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

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


class BisericaViewSet(ModelViewSet): 
    serializer_class = serializers.BisericaListSerializer
    queryset = models.BisericaPage.objects.live()

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.BisericaListSerializer 
        return serializers.BisericaSerializer

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



class FiltersView(ViewSet):

    @method_decorator(cache_page(60 * 60 * 24 * 31))
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
            '': ['datare_prin_interval_timp', 'datare_secol', 'are_pisanie', 'are_studiu_dendro',
                'are_mutari', 'lista_ctitori', 'lista_mesteri', 'lista_zugravi', 'lista_personalitati']
            }
        istoric_filters = utils.get_chapter_filters(
            models.IstoricPage, istoric_filters_name)

        descriere_filters_name = {
            'Tip scanare': [
                'are_scanare_laser', 'are_model_fotogrametric'
            ],
            'Localizare/Peisaj': [
                "amplasament", "topografie", "relatia_cu_cimitirul", "peisagistica_sitului", "ansamblu_construit"
            ],
            'Arhitectura bisericii': [
                "materiale", "numar_accese_pridvor", "numar_accese_naos", "numar_accese_pronaos", "numar_accese_altar",
                "numar_ochiesi", "solee", "bolta_peste_pronaos",
                "bolta_peste_naos", "bolta_peste_altar", "bolta_peste_pronaos_structura", "bolta_peste_naos_structura", "bolta_peste_altar_structura",
                "cor", "sarpanta_tip", "turn_tip", "numar_clopote", "fundatia","sistem_structural", "sistem_in_cheotoare", "sistem_in_catei",
                "tiranti_tip", "finisaj_exterior_tip", "invelitoare_corp_material", "invelitoare_corp_sindrila_numar_straturi", "invelitoare_corp_sindrlia_tipul_de_batere",
                "invelitoare_corp_sindrlia_forma_botului", "invelitoare_corp_sindrila_cu_tesitura", "invelitoare_corp_sindrlia_prelucrare", "invelitoare_corp_sindrlia_esenta_lemnoasa",
                "invelitoare_turn_material", "invelitoare_turn_sindrila_numar_straturi", "invelitoare_turn_sindrlia_tipul_de_batere",
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
            'Perete despărțitor': [
                    "iconostas_pronaos_naos_tip", "iconostas_pronaos_naos_tehnica", "iconostas_pronaos_naos_numar_intrari", 
            ],
            'Altar': [
                'altar_placa_mesei', 'altar_piciorul_mesei'
            ],
            'Pictură exterioară': [
                'pictura_exterioara_localizare', 'pictura_exterioara_suport', 'pictura_exterioara_tehnica', 'pictura_exterioara_numar_straturi_pictura',
                'pictura_exterioara_datare_secol', 'pictura_exterioara_sursa_datare'
            ],
            'Pictură interioară': [
                'pictura_interioara_localizare', 'pictura_interioara_suport', 'pictura_interioara_tehnica_pictura', 'pictura_interioara_numar_straturi_pictura',
                'pictura_interioara_datare_secol', 'pictura_interioara_sursa_datare'
            ],
            'Intervenții': [
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
            'Finisaje biserică': [
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
            'Componenta Artistică': [
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

        localitati_active = models.IdentificarePage.objects.live().values(
            'localitate__id', 'localitate__nume', 'localitate__judet__id' ,'localitate__judet__nume')

        for localitate in localitati_active:
            if localitate['localitate__id']:
                localitate_item = {
                    'id': localitate['localitate__id'],
                    'value': localitate['localitate__nume'],
                    'judet': localitate['localitate__judet__id'],
                    }

                if localitate_item not in localitati_filters:
                    localitati_filters.append(localitate_item)

                    judet_item = {
                        'id': localitate['localitate__judet__id'],
                        'value': localitate['localitate__judet__nume'],
                    }
                    if judet_item not in judete_filters:
                        judete_filters.append(judet_item)

        biserici = models.BisericaPage.objects.live().values('valoare', 'conservare', 'prioritizare')
        for biserica in biserici:
            if biserica['conservare']:
                conservare_item = {
                    'id': round(biserica['conservare']),
                    'value': round(biserica['conservare']),
                }
                if conservare_item not in conservare_filters:
                    conservare_filters.append(conservare_item)
            if biserica['valoare']:
                valoare_item = {
                    'id': round(biserica['valoare']),
                    'value': CLASE_EVALUARE[round(biserica['valoare'])],
                }
                if valoare_item not in valoare_filters:
                    valoare_filters.append(valoare_item)

            if biserica['prioritizare']:
                prioritizare_item = {
                    'id': CLASE_PRIORITIZARE[round(biserica['prioritizare'])]['id'],
                    'value': CLASE_PRIORITIZARE[round(biserica['prioritizare'])]['value'],
                }
                if prioritizare_item not in prioritizare_filters:
                    prioritizare_filters.append(prioritizare_item)

        response = {
            'basic': {
                'judet': judete_filters,
                'localitate': localitati_filters,
                'conservare': conservare_filters,
                'valoare': valoare_filters,
                'prioritizare': prioritizare_filters,
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
                    'title': 'Descriere Arhitectură / Peisaj',
                    'key': 'descriere',
                    'sections': descriere_filters,
                },
                {
                    'title': 'Descriere Componenta Artistică',
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





class AboutViewSet(ViewSet):

    def list(self, request):
        about_page = models.AboutPage.objects.last()
        about_serializer = serializers.AboutSerializer(about_page)
        return Response(about_serializer.data)
