from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from rest_framework.relations import ManyRelatedField, PrimaryKeyRelatedField
from rest_framework.serializers import ListSerializer
from rest_framework.metadata import SimpleMetadata

from rest_framework_guardian import filters

from guardian.shortcuts import get_objects_for_user
from guardian.core import ObjectPermissionChecker

from biserici.api import serializers
from biserici.permissions import BaseModelPermissions
from biserici import models
from pprint import pprint
from itertools import chain



class ChoicesMetaData(SimpleMetadata):

    def get_field_info(self, field):
        field_info = super().get_field_info(field)
        # print('field:', field2)
        # print('type(field):',field.field_name,  type(field))
        # print('field_info', field_info)
        if type(field) in [PrimaryKeyRelatedField, ManyRelatedField]:
            # field_info['choices'] = field.choices
            if type(field) == ManyRelatedField:
                field = field.child_relation
            if field.queryset.model._meta.app_label == 'fragmente':
                field_info['fragment'] = field.queryset.model._meta.model_name.lower()
        if type(field) == ListSerializer:
            field_info['is_repetition_field'] = True
        else:
            field_info['is_repetition_field'] = False
        return field_info


    # def get_serializer_info(self, serializer):
    #     serializer_info = super().get_serializer_info(serializer)
    #     print('-----')
    #     print(dir(serializer_info))
    #     print(serializer_info.keys())
    #     print('-----')
    #     return serializer_info


class BisericiViewSet(ModelViewSet):
    serializer_class = serializers.BisericaListSerializer
    queryset = models.Biserica.objects.all()
    metadata_class = ChoicesMetaData
    permission_classes = [BaseModelPermissions]
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    filter_backends = [filters.ObjectPermissionsFilter]

    # def get_queryset(self):
    #     queryset = self.queryset
    #     user = self.request.user

    #     if self.request.META['PATH_INFO'].endswith('identificare/'):
    #         return get_objects_for_user(user, 'biserici.view_identificare')
    #     if self.request.META['PATH_INFO'].endswith('descriere'):
    #         return get_objects_for_user(user, 'biserici.view_descriere')
    #     if self.request.META['PATH_INFO'].endswith('istoric'):
    #         return get_objects_for_user(user, 'biserici.view_istoric')
    #     if self.request.META['PATH_INFO'].endswith('patrimoniu'):
    #         return get_objects_for_user(user, 'biserici.view_patrimoniu')
    #     if self.request.META['PATH_INFO'].endswith('conservare'):
    #         return get_objects_for_user(user, 'biserici.view_conservare')
    #     return get_objects_for_user(user, 'biserici.view_biserica')

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.BisericaListSerializer
        if self.action == 'identificare':
            return serializers.IdentificareSerializer
        if self.action == 'descriere':
            return serializers.DescriereSerializer
        if self.action == 'istoric':
            return serializers.IstoricSerializer
        if self.action == 'patrimoniu':
            return serializers.PatrimoniuSerializer
        if self.action == 'conservare':
            return serializers.ConservareSerializer
        return serializers.BisericaSerializer

    @action(detail=True, methods=['post', 'get'])
    def identificare(self, request, pk=None, permission_classes=[BaseModelPermissions]):
        print(request)
        identificare = models.Biserica.objects.get(pk=pk).identificare
        if request.method == 'GET':
            serializer = serializers.IdentificareSerializer(identificare, context={'request': request})
        elif request.method == 'POST':
            serializer = serializers.IdentificareSerializer(identificare, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data)

    @action(detail=True, methods=['post', 'get'])
    def descriere(self, request, pk=None):
        descriere = models.Biserica.objects.get(pk=pk).descriere
        if request.method == 'GET':
            serializer = serializers.DescriereSerializer(descriere, context={'request': request})
        elif request.method == 'POST':
            serializer = serializers.DescriereSerializer(descriere, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save(last_edit_user=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data)

    @action(detail=True, methods=['post', 'get'])
    def istoric(self, request, pk=None):
        istoric = models.Biserica.objects.get(pk=pk).istoric
        if request.method == 'GET':
            serializer = serializers.IstoricSerializer(istoric, context={'request': request})
        elif request.method == 'POST':
            serializer = serializers.IstoricSerializer(istoric, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save(last_edit_user=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data)

    @action(detail=True, methods=['post', 'get'])
    def patrimoniu(self, request, pk=None):
        patrimoniu = models.Biserica.objects.get(pk=pk).patrimoniu
        if request.method == 'GET':
            serializer = serializers.PatrimoniuSerializer(patrimoniu, context={'request': request})
        elif request.method == 'POST':
            serializer = serializers.PatrimoniuSerializer(patrimoniu, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save(last_edit_user=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data)

    @action(detail=True, methods=['post', 'get'])
    def conservare(self, request, pk=None):
        conservare = models.Biserica.objects.get(pk=pk).conservare
        if request.method == 'GET':
            serializer = serializers.ConservareSerializer(conservare, context={'request': request})
        elif request.method == 'POST':
            serializer = serializers.ConservareSerializer(conservare, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save(last_edit_user=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data)