from django.utils import timezone
from rest_framework import serializers
from biserici import models
from pprint import pprint

class IdentificareSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Identificare
        exclude = ["biserica", "id"]


class IstoricSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Istoric
        exclude = ["biserica", "id"]


class DescriereSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Descriere
        exclude = ["biserica"]



class BisericaSerializer(serializers.ModelSerializer):
    identificare = IdentificareSerializer()
    istoric = IstoricSerializer()
    # descriere = DescriereSerializer()

    class Meta:
        model = models.Biserica
        fields = ["nume", "identificare", "istoric"]


    def update(self, instance, validated_data):
        pprint(validated_data)
        if validated_data.get('identificare'):
            identificare_data = validated_data.pop('identificare')
            identificare_data['last_edit_date'] = timezone.now()
            identificare_data['last_edit_user'] = self.context['request'].user
            models.Identificare.objects.filter(pk=instance.identificare.pk).update(**identificare_data)

        if validated_data.get('istoric'):
            istoric_data = validated_data.pop('istoric')
            istoric_data['last_edit_date'] = timezone.now()
            istoric_data['last_edit_user'] = self.context['request'].user
            models.Istoric.objects.filter(pk=instance.istoric.pk).update(**istoric_data)

        if validated_data.get('descriere'):
            descriere_data = validated_data.pop('descriere')
            descriere_data['last_edit_date'] = timezone.now()
            descriere_data['last_edit_user'] = self.context['request'].user
            models.Descriere.objects.filter(pk=instance.descriere.pk).update(**descriere_data)

        models.Biserica.objects.filter(pk=instance.pk).update(**validated_data)
        instance.refresh_from_db()

        return instance


class BisericaListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:biserica-detail")

    class Meta:
        model = models.Biserica
        fields = ["nume", "pk", "url"]
