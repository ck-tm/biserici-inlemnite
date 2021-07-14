from rest_framework import serializers
from biserici import models


class IdentificareSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Identificare
        exclude = ["biserica"]


class BisericaSerializer(serializers.ModelSerializer):
    identificare = IdentificareSerializer()

    class Meta:
        model = models.Biserica
        fields = ["nume", "identificare"]


class BisericaListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:biserica-detail")

    class Meta:
        model = models.Biserica
        fields = ["nume", "pk", "url"]
