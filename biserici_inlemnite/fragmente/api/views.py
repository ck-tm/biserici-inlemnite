from rest_framework import generics
from .serializers import GeneralSerializer


from wq.db.rest.views import ModelViewSet


class GenericAPIView(ModelViewSet):
    pass
    # serializer_class = GeneralSerializer
    # queryset = models.Biserica.objects.all()
    # metadata_class = ChoicesMetaData
    # permission_classes = [BaseModelPermissions]
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # filter_backends = [filters.ObjectPermissionsFilter]

# class GenericAPIView(generics.ListAPIView):
#     def dispatch(self, request, *args, **kwargs):
#         self.model = kwargs.pop('model')
#         self.queryset = self.model.objects.all()
#         serializer = GeneralSerializer
#         serializer.Meta.model = self.model
#         self.serializer_class = serializer
#         return super().dispatch(request, *args, **kwargs)