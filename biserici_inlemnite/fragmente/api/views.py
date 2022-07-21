from django.apps import apps
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from .serializers import GeneralSerializer

from wq.db.rest.views import ModelViewSet


class GenericAPIView(ModelViewSet):
    pass


class FragmenteView(ViewSet):

    # @method_decorator(cache_page(60 * 60 * 24 * 31))
    def list(self, request):
        response = []
        app = apps.get_app_config("fragmente")

        for model_name, model in app.models.items():
            if not "historical" in model_name:
                response.append({"model": model_name, "values": model.objects.values()})

        return Response(response)
