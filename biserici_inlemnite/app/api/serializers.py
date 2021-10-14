from django.utils import timezone
from django.utils.html import strip_tags
from django.contrib.auth.models import Group
from rest_framework import serializers
from rest_framework.reverse import reverse
from wagtail.images.api.fields import ImageRenditionField
from rest_framework.relations import PrimaryKeyRelatedField, ManyRelatedField
from app import models
from pprint import pprint
from nomenclatoare import models as n_models

class ReprMixin(object):

    def __init__(self, *args, **kwargs):
     super().__init__(*args, **kwargs)

     exclude = [
            "title", "id", "path", "depth", "numchild", "translation_key",
            "draft_title", "slug", "live", "has_unpublished_changes", "url_path",
            "seo_title", "show_in_menus", "search_description", "go_live_at",
            "expire_at", "expired", "locked", "locked_at", "first_published_at",
            "last_published_at", "latest_revision_created_at", "locale",
            "content_type", "owner", "locked_by", "live_revision", "alias_of"
        ]

     for field_name in exclude:
       if field_name in self.fields:
         del self.fields[field_name]

    def to_representation(self, instance):
        data = super().to_representation(instance)

        for field_name, field_type in self.fields.items():

            if field_type.style == {'base_template': 'textarea.html'}:
                # data[field_name] = strip_tags(data[field_name])
                pass
            if type(field_type) == PrimaryKeyRelatedField:
                if data[field_name]:
                    data[field_name] = field_type.choices[data[field_name]]
            if type(field_type) == ManyRelatedField:
                try:
                    data[field_name] = [field_type.choices[data[x]] for x in data[field_name]]
                except:
                    pass

        return data


class PozaSerializer(serializers.Serializer):
    observatii = serializers.CharField()
    poza = ImageRenditionField('width-480')

    class Meta:
        fields = ['poza', 'observatii']

class ElementSerializer(serializers.Serializer):
    element = serializers.CharField()
    observatii = serializers.CharField()
    poze = PozaSerializer(many=True)

    class Meta:
        fields = ['poza', 'observatii']



class IdentificareSerializer(ReprMixin, serializers.ModelSerializer):

    class Meta:
        model = models.IdentificarePage
        fields = '__all__'


class IstoricSerializer(ReprMixin, serializers.ModelSerializer):

    class Meta:
        model = models.IstoricPage
        fields = '__all__'


class DescriereSerializer(ReprMixin, serializers.ModelSerializer):

    poze_amplasament = PozaSerializer(many=True)
    elemente_ansamblu_construit = ElementSerializer(many=True)
    elemente_importante_ansamblu_construit = ElementSerializer(many=True)

    class Meta:
        model = models.DescrierePage
        fields = '__all__'


class ComponentaArtisticaSerializer(ReprMixin, serializers.ModelSerializer):

    class Meta:
        model = models.ComponentaArtisticaPage
        fields = '__all__'


class ConservareSerializer(ReprMixin, serializers.ModelSerializer):

    class Meta:
        model = models.ConservarePage
        fields = '__all__'


class ValoareSerializer(ReprMixin, serializers.ModelSerializer):

    class Meta:
        model = models.ValoarePage
        fields = '__all__'



class BisericaSerializer(serializers.ModelSerializer):
    identificare = serializers.SerializerMethodField()
    descriere = serializers.SerializerMethodField()
    istoric = serializers.SerializerMethodField()
    componenta_artistica = serializers.SerializerMethodField()
    conservare = serializers.SerializerMethodField()
    valoare = serializers.SerializerMethodField()

    class Meta:
        model = models.BisericaPage
        fields = ["id", "title", "identificare", "istoric", "descriere", "componenta_artistica", "conservare", "valoare"]

    def get_identificare(self, obj):
        identificare_page = obj.get_children().type(
            models.IdentificarePage)[0].specific
        serializer = IdentificareSerializer(identificare_page)
        return serializer.data

    def get_descriere(self, obj):
        descriere_page = obj.get_children().type(
            models.DescrierePage)[0].specific
        serializer = DescriereSerializer(descriere_page)
        return serializer.data

    def get_istoric(self, obj):
        istoric_page = obj.get_children().type(
            models.IstoricPage)[0].specific
        serializer = IstoricSerializer(istoric_page)
        return serializer.data

    def get_componenta_artistica(self, obj):
        componenta_artistica_page = obj.get_children().type(
            models.ComponentaArtisticaPage)[0].specific
        serializer = ComponentaArtisticaSerializer(componenta_artistica_page)
        return serializer.data

    def get_conservare(self, obj):
        conservare_page = obj.get_children().type(
            models.ConservarePage)[0].specific
        serializer = ConservareSerializer(conservare_page)
        return serializer.data

    def get_valoare(self, obj):
        valoare_page = obj.get_children().type(
            models.ValoarePage)[0].specific
        serializer = ValoareSerializer(valoare_page)
        return serializer.data


class BisericaListSerializer(serializers.ModelSerializer):
    poze = PozaSerializer(many=True)

    class Meta:
        model = models.BisericaPage
        fields = ["id", "title", "judet", "localitate", "adresa", "latitudine",
                  "longitudine", "datare_prin_interval_timp", "datare_secol",
                   "conservare", "valoare", "prioritizare", "poze"]

