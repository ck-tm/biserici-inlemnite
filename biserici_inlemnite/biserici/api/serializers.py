from django.utils import timezone
from django.contrib.auth.models import Group
from rest_framework import serializers
from rest_framework.reverse import reverse
from rest_framework_guardian.serializers import ObjectPermissionsAssignmentMixin
from drf_writable_nested.serializers import WritableNestedModelSerializer

from guardian.shortcuts import get_objects_for_user, assign_perm, remove_perm
from guardian.core import ObjectPermissionChecker
from biserici import models
from pprint import pprint



class FotografieSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Fotografie
        exclude = ["id"]

class IdentificareFrecventaUtilizariiSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.IdentificareFrecventaUtilizarii
        fields = "__all__"


class IdentificareSingularitateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.IdentificareSingularitate
        exclude = ["id"]

class LocalizareUnitatiTeritorialeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LocalizareUnitatiTeritoriale
        exclude = ["id"]

class LocalizareAdresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LocalizareAdresa
        exclude = ["id"]

class LocalizareReferinteCadastraleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LocalizareReferinteCadastrale
        exclude = ["id"]

class LocalizareRegimulDeProprietateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LocalizareRegimulDeProprietate
        exclude = ["id"]


class RepereGeograficeFormaReliefSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RepereGeograficeFormaRelief
        exclude = ["id"]


class RepereGeograficeReperHidrograficSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RepereGeograficeReperHidrografic
        exclude = ["id"]


class RepereGeograficeZoneNaturaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RepereGeograficeZoneNaturale
        exclude = ["id"]

class IstoricScurtIstoricSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.IstoricScurtIstoric
        exclude = ["id"]

class IstoricPisanieSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.IstoricPisanie
        exclude = ["id"]

class IstoricPersoanaSerializer(serializers.ModelSerializer):
    foto = FotografieSerializer(many=True)

    class Meta:
        model = models.IstoricPersoana
        exclude = ["id"]

class IstoricEvenimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.IstoricEveniment
        exclude = ["id"]

class IstoricMutareSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.IstoricMutare
        exclude = ["id"]


class IdentificareSerializer(ObjectPermissionsAssignmentMixin, WritableNestedModelSerializer):
    frecventa_utilizarii = IdentificareFrecventaUtilizariiSerializer()
    singularitate = IdentificareSingularitateSerializer()

    class Meta:
        model = models.Identificare
        fields = [
            "codul_lmi",
            "categoria",
            "statut",
            "denumire_oficiala",
            "hram",
            "cult",
            "frecventa_utilizarii",
            "singularitate",
        ]
        # read_only_fields = ["last_edit_user"]

    def get_permissions_map(self, created):
        current_user = self.context['request'].user
        instance = self.instance

        grup_judet = None 

        if instance.biserica.descriere.judet:
            judet_biserica = instance.descriere.judet.nume
            grup_judet, _ = Group.objects.get_or_create(name=judet_biserica)

        return {
            'view_identificare': [current_user, grup_judet],
            'change_identificare': [current_user, grup_judet],
            'delete_identificare': []
        }


class LocalizareSerializer(WritableNestedModelSerializer):
    unitati_teritoriale = LocalizareUnitatiTeritorialeSerializer()
    adresa = LocalizareAdresaSerializer()
    referinte_cadastrale = LocalizareReferinteCadastraleSerializer()
    regim_proprietate = LocalizareRegimulDeProprietateSerializer()

    class Meta:
        model = models.Localizare
        exclude = ["biserica"]


class RepereGeograficeSeralizer(WritableNestedModelSerializer):
    forma_relief = RepereGeograficeFormaReliefSerializer()
    reper_hidrografic = RepereGeograficeReperHidrograficSerializer()
    zone_naturale = RepereGeograficeZoneNaturaleSerializer()

    class Meta:
        model = models.RepereGeografice
        exclude = ["biserica"]

class IstoricSerializer(WritableNestedModelSerializer):
    scurt_istoric = IstoricScurtIstoricSerializer()
    pisanie = IstoricPisanieSerializer()
    ctitori = IstoricPersoanaSerializer(many=True)
    mesteri = IstoricPersoanaSerializer(many=True)
    zugravi = IstoricPersoanaSerializer(many=True)
    personalitati = IstoricPersoanaSerializer(many=True)
    evenimente = IstoricEvenimentSerializer(many=True)
    mutari = IstoricMutareSerializer(many=True)
    class Meta:
        model = models.Istoric
        exclude = ["biserica"]




class DescriereSerializer(ObjectPermissionsAssignmentMixin, serializers.ModelSerializer):
    class Meta:
        model = models.Descriere
        exclude = ["biserica"]
        # read_only_fields = ["last_edit_user"]

    def get_permissions_map(self, created):
        current_user = self.context['request'].user
        instance = self.instance
        grup_judet = None
        if instance.judet:
            grup_judet, _ = Group.objects.get_or_create(name=judet_biserica)
        #     biserica = instance.biserica

        #     judet_biserica = instance.judet.nume
        #     assign_perm('view_biserica', grup_judet, biserica)
        #     assign_perm('change_biserica', grup_judet, biserica)

        #     for t in ['istoric', 'descriere', 'patrimoniu', 'conservare']:
        #             assign_perm(f'view_{t}', grup_judet, getattr(biserica, t))
        #             assign_perm(f'change_{t}', grup_judet, getattr(biserica, t))

        #     for judet in Group.objects.exclude(name=judet_biserica):
        #         remove_perm('view_biserica', judet, biserica)
        #         remove_perm('change_biserica', judet, biserica)

        #         for t in ['istoric', 'descriere', 'patrimoniu', 'conservare']:
        #             remove_perm(f'view_{t}', judet, getattr(biserica, t))
        #             remove_perm(f'change_{t}', judet, getattr(biserica, t))

        return {
            'view_identificare': [current_user, grup_judet],
            'change_identificare': [current_user, grup_judet],
            'delete_identificare': []
        }
class PatrimoniuSerializer(ObjectPermissionsAssignmentMixin, serializers.ModelSerializer):
    class Meta:
        model = models.Patrimoniu
        exclude = ["biserica"]
        # read_only_fields = ["last_edit_user"]

    def get_permissions_map(self, created):
        current_user = self.context['request'].user
        instance = self.instance

        grup_judet = None 

        if instance.biserica.descriere.judet:
            judet_biserica = instance.descriere.judet.nume
            grup_judet, _ = Group.objects.get_or_create(name=judet_biserica)

        

        return {
            'view_identificare': [current_user, grup_judet],
            'change_identificare': [current_user, grup_judet],
            'delete_identificare': []
        }

class ConservareSerializer(ObjectPermissionsAssignmentMixin, serializers.ModelSerializer):
    class Meta:
        model = models.Conservare
        exclude = ["biserica"]
        # read_only_fields = ["last_edit_user"]

    def get_permissions_map(self, created):
        current_user = self.context['request'].user
        instance = self.instance

        grup_judet = None 

        if instance.biserica.descriere.judet:
            judet_biserica = instance.descriere.judet.nume
            grup_judet, _ = Group.objects.get_or_create(name=judet_biserica)


        return {
            'view_identificare': [current_user, grup_judet],
            'change_identificare': [current_user, grup_judet],
            'delete_identificare': []
        }


class BisericaSerializer(ObjectPermissionsAssignmentMixin, WritableNestedModelSerializer):
    identificare = IdentificareSerializer()
    localizare = LocalizareSerializer()
    repere_geografice = RepereGeograficeSeralizer()
    istoric = IstoricSerializer()

    class Meta:
        model = models.Biserica
        fields = ["nume"]
        fields = ["nume", "identificare", "localizare", "repere_geografice", "istoric"]


    def get_permissions_map(self, created):
        current_user = self.context['request'].user
        instance = self.instance
        grup_judet = None

        if instance.descriere.judet:
            judet_biserica = instance.descriere.judet.nume
            grup_judet, _ = Group.objects.get_or_create(name=judet_biserica)

        return {
            'view_biserica': [current_user, grup_judet],
            'change_biserica': [current_user, grup_judet],
            'delete_biserica': []
        }

class BisericaListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api_admin:biserici-detail")
    # capitole = serializers.SerializerMethodField()

    class Meta:
        model = models.Biserica
        fields = ["nume", "pk", "url"]
        # fields = ["nume", "pk", "url", "capitole"]

    # def get_capitole(self, obj):
    #     capitole = []
    #     user = self.context['request'].user
    #     checker = ObjectPermissionChecker(user)
    #     for capitol in ['identificare', 'istoric', 'descriere', 'patrimoniu', 'conservare']:
    #         capitol_obj = getattr(obj, capitol)
    #         if checker.has_perm(f'change_{capitol}', capitol_obj):
    #             capitole.append({
    #                 'nume': capitol,
    #                 'url': reverse(f"api_admin:biserici-{capitol}", args=[obj.pk], request=self.context['request'])
    #                 })
    #     return capitole

