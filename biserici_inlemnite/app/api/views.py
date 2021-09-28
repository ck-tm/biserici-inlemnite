from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet
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