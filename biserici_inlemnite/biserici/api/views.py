from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from rest_framework.relations import ManyRelatedField
from rest_framework.metadata import SimpleMetadata

from rest_framework_guardian import filters

from guardian.shortcuts import get_objects_for_user
from guardian.core import ObjectPermissionChecker

from biserici.api import serializers
from biserici.permissions import BaseModelPermissions
from biserici import models
from pprint import pprint



class ForeignMetaData(SimpleMetadata):

    def get_serializer_info(self, serializer):
        orderedDict = super().get_serializer_info(serializer)
        try:
            functiuni = [{'value': x.id, 'display_name': x.nume} for x in models.FunctiuneBiserica.objects.all()]
            orderedDict['identificare']['children']['functiune_initiala']['choices'] = functiuni
            orderedDict['identificare']['children']['functiune']['choices'] = functiuni
        except:
            pass
        return orderedDict


class BisericaViewSet(ModelViewSet):
    serializer_class = serializers.BisericaSerializer
    queryset = models.Biserica.objects.all()
    metadata_class = ForeignMetaData
    permission_classes = [BaseModelPermissions]
    filter_backends = [filters.ObjectPermissionsFilter]

    def get_queryset(self):
        queryset = self.queryset
        user = self.request.user
        biserici_user = []

        # for biserica in get_objects_for_user(user, 'biserici.view_biserica'):
        #     if user.has_perm('view_biserica', biserica):
        #         print(biserica, user.has_perm('view_biserica', biserica))
        #         biserici_user.append(biserica.pk)
        
        # return queryset.filter(pk__in=biserici_user)
        return get_objects_for_user(user, 'biserici.view_biserica')

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
        identificare = models.Biserica.objects.get(pk=pk).identificare
        if request.method == 'GET':
            serializer = serializers.IdentificareSerializer(identificare, context={'request': request})
        elif request.method == 'POST':
            serializer = serializers.IdentificareSerializer(identificare, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save(last_edit_user=request.user)
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