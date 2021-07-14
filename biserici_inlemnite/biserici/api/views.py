from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from rest_framework.relations import ManyRelatedField
from rest_framework.metadata import SimpleMetadata

from biserici.api import serializers
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


    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.BisericaListSerializer
        return serializers.BisericaSerializer