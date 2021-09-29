from django.utils import timezone
from django.contrib.auth.models import Group
from rest_framework import serializers
from rest_framework.reverse import reverse
from rest_framework_guardian.serializers import ObjectPermissionsAssignmentMixin

from guardian.shortcuts import get_objects_for_user, assign_perm, remove_perm
from guardian.core import ObjectPermissionChecker
from biserici import models
from pprint import pprint


class IdentificareSerializer(ObjectPermissionsAssignmentMixin, serializers.ModelSerializer):
    class Meta:
        model = models.Identificare
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

class IstoricSerializer(ObjectPermissionsAssignmentMixin, serializers.ModelSerializer):
    class Meta:
        model = models.Istoric
        exclude = ["biserica"]
        # read_only_fields = ["last_edit_user"]

    def get_permissions_map(self, created):
        current_user = self.context['request'].user
        instance = self.instance

        grup_judet = None 

        if instance.biserica.idenficare.judet:
            judet_biserica = instance.idenficare.judet.nume
            grup_judet, _ = Group.objects.get_or_create(name=judet_biserica)

        return {
            'view_identificare': [current_user, grup_judet],
            'change_identificare': [current_user, grup_judet],
            'delete_identificare': []
        }

class DescriereSerializer(ObjectPermissionsAssignmentMixin, serializers.ModelSerializer):
    class Meta:
        model = models.Descriere
        exclude = ["biserica"]
        # read_only_fields = ["last_edit_user"]

    def get_permissions_map(self, created):
        current_user = self.context['request'].user
        instance = self.instance

        grup_judet = None 

        if instance.biserica.idenficare.judet:
            judet_biserica = instance.idenficare.judet.nume
            grup_judet, _ = Group.objects.get_or_create(name=judet_biserica)

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

        if instance.biserica.idenficare.judet:
            judet_biserica = instance.idenficare.judet.nume
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

        if instance.biserica.idenficare.judet:
            judet_biserica = instance.idenficare.judet.nume
            grup_judet, _ = Group.objects.get_or_create(name=judet_biserica)


        return {
            'view_identificare': [current_user, grup_judet],
            'change_identificare': [current_user, grup_judet],
            'delete_identificare': []
        }

class BisericaSerializer(ObjectPermissionsAssignmentMixin, serializers.ModelSerializer):
    capitole = serializers.SerializerMethodField()

    class Meta:
        model = models.Biserica
        fields = ["nume", "capitole"]


    def get_capitole(self, obj):
        capitole = []
        user = self.context['request'].user
        checker = ObjectPermissionChecker(user)
        for capitol in ['identificare', 'istoric', 'descriere', 'patrimoniu', 'conservare']:
            if checker.has_perm(f'change_{capitol}', getattr(obj, capitol)):
                capitole.append({
                    'name': capitol,
                    'url': reverse(f"api:biserica-{capitol}", args=[obj.pk], request=self.context['request'])
                    })
        return capitole

    def get_permissions_map(self, created):
        current_user = self.context['request'].user
        instance = self.instance
        group_judet = None

        if instance.idenficare.judet:
            judet_biserica = instance.idenficare.judet.nume
            grup_judet, _ = Group.objects.get_or_create(name=judet_biserica)

        return {
            'view_biserica': [current_user, grup_judet],
            'change_biserica': [current_user, grup_judet],
            'delete_biserica': []
        }

class BisericaListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:biserica-detail")
    capitole = serializers.SerializerMethodField()

    class Meta:
        model = models.Biserica
        fields = ["nume", "pk", "url", "capitole"]

    def get_capitole(self, obj):
        capitole = []
        user = self.context['request'].user
        checker = ObjectPermissionChecker(user)
        for capitol in ['identificare', 'istoric', 'descriere', 'patrimoniu', 'conservare']:
            capitol_obj = getattr(obj, capitol)
            if checker.has_perm(f'change_{capitol}', capitol_obj):
                capitole.append({
                    'nume': capitol,
                    'completare': capitol_obj.completare,
                    'url': reverse(f"api:biserica-{capitol}", args=[obj.pk], request=self.context['request'])
                    })
        return capitole

