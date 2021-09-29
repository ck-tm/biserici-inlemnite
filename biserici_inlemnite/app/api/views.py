from django.contrib.auth import get_user_model
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


class BisericaViewSet(ModelViewSet):
    serializer_class = serializers.BisericaListSerializer
    queryset = models.BisericaPage.objects.live()

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.BisericaListSerializer
        return serializers.BisericaSerializer


def get_chapter_filters(model, filters_name):
    filters = {}
    filters_values = model.objects.live().values(*filters_name)
    for item in filters_values:
        for field_name, field_value in item.items():
            filters.setdefault(field_name, [])
            if field_value and field_value not in filters[field_name]:
                filters[field_name].append(field_value)
    for field in filters_name:
        if filters[field]:
            if model._meta.get_field(field).remote_field:
                field_model = model._meta.get_field(field).remote_field.model
                filters[field] = {
                    "title": model._meta.get_field(field).verbose_name.title(),
                    "key": field,
                    "values": field_model.objects.filter(id__in=filters[field]).values('id', 'nume')
                }
            else:
                if model._meta.get_field(field).choices:
                    choices =  {x[0]: x[1] for x in model._meta.get_field(field).choices}
                    filters[field] = {
                        "title": field.replace('_', ' ').title(),
                        "key": field,
                        "values": [choices[x] for x in filters[field]]
                    }
                else:
                    filters[field] = {
                        "title": field.replace('_', ' ').title(),
                        "key": field,
                        "values": filters[field]
                    }
        else:
            del filters[field]
    return filters


class FiltersView(ViewSet):

    def list(self, request):
        """
        Return a list of all users.
        """
        identificare_filters_name = ['statut', 'cult', 'utilizare', 'singularitate', 'functiune',
                                     'functiune_initiala', 'proprietate_actuala']
        identificare_filters = get_chapter_filters(
            models.IdentificarePage, identificare_filters_name)

        istoric_filters_name = ['datare_secol', 'sursa_datare']
        istoric_filters = get_chapter_filters(
            models.IstoricPage, istoric_filters_name)

        descriere_filters_name = ["amplasament", "topografie", "relatia_cu_cimitirul",
                                  "turn_dimensiune", "turn_tip", "turn_plan", "turn_amplasare",
                                  "turn_galerie", "turn_asezare_talpi", "turn_relatie_talpi", "sarpanta_material_cruci",
                                  "bolta_peste_pronaos", "bolta_peste_naos", "bolta_peste_altar", "bolta_peste_altar_tip",
                                  "masa_altar_material_picior", "masa_altar_material_blat", "turle_forma_sarpanta",
                                  "fundatia", "sistem_in_cheotoare", "sistem_in_catei", "tiranti_tip",
                                  "invelitoare_corp_material", "invelitoare_corp_sindrlia_tipul_de_batere",
                                  "invelitoare_corp_sindrlia_tipul_prindere", "invelitoare_corp_sindrlia_forma_botului",
                                  "invelitoare_corp_sindrlia_prelucrare", "invelitoare_corp_sindrlia_esenta_lemnoasa",
                                  "invelitoare_turn_material", "invelitoare_turn_sindrlia_tipul_de_batere",
                                  "invelitoare_turn_sindrlia_tipul_prindere", "invelitoare_turn_sindrlia_forma_botului",
                                  "invelitoare_turn_sindrlia_prelucrare", "invelitoare_turn_sindrlia_esenta_lemnoasa",
                                  "inchidere_tambur_turn_material", "inchidere_tambur_turn_sindrlia_tipul_de_batere",
                                  "inchidere_tambur_turn_sindrlia_tipul_prindere", "inchidere_tambur_turn_sindrlia_forma_botului",
                                  "inchidere_tambur_turn_sindrlia_prelucrare", "inchidere_tambur_turn_sindrlia_esenta_lemnoasa",
                                  "invelitoare_turle_sindrlia_tipul_de_batere", "invelitoare_turle_sindrlia_tipul_prindere",
                                  "invelitoare_turle_sindrlia_forma_botului", "invelitoare_turle_sindrlia_prelucrare",
                                  "invelitoare_turle_sindrlia_esenta_lemnoasa",
                                  "interventii_invelitoare_sindrlia_tipul_de_batere",
                                  "interventii_invelitoare_sindrlia_forma_botului",
                                  "interventii_invelitoare_sindrlia_esenta_lemnoasa", "peisagistica_sitului", "elemente",
                                  "elemente_importante", "materiale", "sarpanta_tip", "bolta_peste_pronaos_material",
                                  "bolta_peste_pronaos_tipul_de_arc", "bolta_peste_naos_material", "bolta_peste_naos_tipul_de_arc",
                                  "bolta_peste_altar_material", "bolta_peste_altar_tipul_de_arc", "cor_material", "turle_pozitionare",
                                  "finisaj_exterior_tip", "invelitoare_turle_material"]
        descriere_filters = get_chapter_filters(
            models.DescrierePage, descriere_filters_name)

        componenta_artistica_name = [
                    "iconostas_naos_altar_tip", "iconostas_pronaos_naos_tip", "iconostas_pronaos_naos_material",
                    "altar_decor", "pictura_exterioara_localizare", "pictura_exterioara_tehnica", "pictura_exterioara_datare_secol",
                    "pictura_interioara_localizare", "pictura_interioara_tehnica_pictura", "pictura_interioara_datare_secol",
                    "suport_proscomidie", "obiecte_de_cult", "mobiliere", "iconostas_naos_altar_tehnica",
                    "iconostas_naos_altar_registre", "iconostas_naos_altar_tip_usi", "iconostas_naos_altar_materiale",
                    "iconostas_pronaos_naos_tehnica", "altar_placa_mesei", "altar_piciorul_mesei", "pictura_exterioara_suport",
                    "pictura_exterioara_sursa_datare", "pictura_interioara_suport", "pictura_interioara_sursa_datare"]
        componenta_artistica_filters = get_chapter_filters(
            models.ComponentaArtisticaPage, componenta_artistica_name)


        conservare_filters_name = ["sit", "elemente_arhitecturale", "alte_elemente_importante", "vegetatie", "teren", "fundatii", "talpi", "corp_biserica", "bolti", "cosoroabe", "sarpanta_peste_corp_biserica", "turn", "zona_din_jurul_biserici", "pardoseli_interioare", "finisaj_exterior", "finisaj_pereti_interiori", "finisaj_tavane_si_bolti", "tamplarii", "invelitoare_sarpanta_si_turn", "instalatie_electrica", "instalatie_termica", "paratraznet", "strat_pictural", "obiecte_de_cult", "mobilier"]
        conservare_filters = get_chapter_filters(
            models.ConservarePage, conservare_filters_name)

        valoare_filters_name = ["vechime", "integritate", "unicitate", "valoare_memoriala", "peisaj_cultural", "valoare_sit", "estetica", "mestesug", "pictura", "folosinta_actuala", "relevanta_actuala", "potential"]
        valoare_filters = get_chapter_filters(
            models.ValoarePage, valoare_filters_name)

        localitati_filters = []
        judete_filters = []
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

        response = {
            'basic': {
                'judete': judete_filters,
                'localitati': localitati_filters,
            },
            'advanced': {
                'identificare': identificare_filters,
                'istoric': istoric_filters,
                'descriere': descriere_filters,
                'componenta_artistica': componenta_artistica_filters,
                'conservare': conservare_filters,
                'valoare': valoare_filters,
            }
        }
        return Response(response)
