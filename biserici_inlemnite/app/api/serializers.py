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



def generic_serializer_data(field):
    try:
        values = field.all()
        if values:
            print(values)
            if type(values[0]).__module__.startswith('nomenclatoare'):
                return ', '.join([str(x) for x in values])

            serializer_list = []
            meta_fields = type(values[0])._meta.fields
            for obj in values:
                obj_serializer = {}
                for field in meta_fields:
                    field_value = getattr(obj, field.name)
                    if field_value and field.name not in ['page', 'id', 'sort_order']:
                        obj_serializer[field.verbose_name.capitalize()] = str(field_value)
                if obj_serializer:
                    print('=======')
                    pprint(obj_serializer)
                    serializer_list.append(obj_serializer)

            return serializer_list
        return None
    except:
        if type(field) in [str, float, type(None)]:
            return field
        return str(field)


def get_sections_serialized(obj, sections):
    sections_serializer = []
    for section in sections:
        section_serializer = {
            'title': section['title'],
            'fields': []
            }
        for field in section['fields']:
            value = generic_serializer_data(getattr(obj, field[0]))
            if value:
                field_serializer = {
                    'key': field[0],
                    'label': field[1] if field[1] else obj._meta.get_field(field[0]).verbose_name,
                    'value': value
                }
                section_serializer['fields'].append(field_serializer)
        if section_serializer['fields']:
            sections_serializer.append(section_serializer)
    return sections_serializer


class IdentificareSerializer(serializers.ModelSerializer):
    sections = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()

    class Meta:
        model = models.IdentificarePage
        fields = ['title', 'sections']

    def get_sections(self, obj):
        sections =  [
            {
            'title': 'Localizare',
            'fields': [
                ("judet", "Jude"),
                ("localitate", "Localitate"),
                ("adresa", "Adresa"),
                ("latitudine", "Latitudine"),
                ("longitudine", "Longitudine"),
                ]
            },
            {
            'title': 'Statut',
            'fields': [
                ("statut", "Statut"),
                ]
            },
            {
            'title': 'Hram',
            'fields': [
                ("hram", "Hram"),
                ]
            },
            {
            'title': 'Denumire',
            'fields': [
                ("denumire_actuala", "Denumire actuala"),
                ("denumire_precedenta", "Denumire precedenta"),
                ("denumire_locala", "Denumire locala"),
                ("denumire_oberservatii", "Denumire oberservatii"),
                ]
            },
            {
            'title': 'Cult',
            'fields': [
                ("cult", "Cult"),
                ]
            },
            {
            'title': 'Utilizare',
            'fields': [
                ("utilizare", "Utilizare"),
                ("utilizare_observatii", "Utilizare observatii"),
                ]
            },
            {
            'title': 'Singularitate',
            'fields': [
                ("singularitate", "Singularitate"),
                ("singularitate_observatii", "Singularitate observatii"),
                ]
            },
            {
            'title': 'Funcțiune',
            'fields': [
                ("functiune", "Functiune"),
                ("functiune_observatii", "Functiune observatii"),
                ("functiune_initiala", "Functiune initiala"),
                ("functiune_initiala_observatii", "Functiune initiala observatii"),
                ]
            },
            {
            'title': 'Proprietate',
            'fields': [
                ("proprietate_actuala", "Proprietate actuala"),
                ("proprietate_observatii", "Proprietate observatii"),
                ("proprietar_actual", "Proprietar actual"),
                ]
            },
            {
            'title': 'Înscriere documente cadastrale',
            'fields': [
                ("inscriere_documente_cadastrale", "Inscriere documente cadastrale"),
                ]
            },
        ]

        return get_sections_serialized(obj, sections)

    def get_title(self, obj):
        return obj.title.split('. ')[-1]


class IstoricSerializer(serializers.ModelSerializer):
    sections = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()

    class Meta:
        model = models.IstoricPage
        fields = ['title', 'sections']

    def get_sections(self, obj):
        sections =  [
            {
            'title': 'Datare',
            'fields': [
                ("sursa_datare", "Sursa datare"),
                ("an_constructie", "An constructie"),
                ("datare_prin_interval_timp", "Datare prin interval timp"),
                ("datare_secol", "Datare secol"),
                ("datare_secol_observatii", "Datare secol observatii"),
                ("datare_secol_sursa", "Datare secol sursa"),
                ]
            },
            {
            'title': 'Studiu dendrocronologic',
            'fields': [
                ("studiu_dendocronologic_fisier", "Studiu dendocronologic fisier"),
                ("studiu_dendocronologic_autor", "Studiu dendocronologic autor"),
                ("studiu_dendocronologic_an", "Studiu dendocronologic an"),
                ("studiu_dendocronologic_observatii", "Studiu dendocronologic observatii"),
                ]
            },
            {
            'title': 'Pisanie',
            'fields': [
                ("pisanie_traducere", "Pisanie traducere"),
                ("pisanie_secol_observatii", "Pisanie secol observatii"),
                ("pisanie_secol_sursa", "Pisanie secol sursa"),
                ]
            },
            {
            'title': 'Persoane',
            'fields': [
                ("ctitori", "Ctitori"),
                ("mesteri", "Mesteri"),
                ("zugravi", "Zugravi"),
                ("personalitati", "Personalitati"),
                ]
            },
            {
            'title': 'Evenimente',
            'fields': [
                ("evenimente", "Evenimente"),
                ]
            },
            {
            'title': 'Mutări',
            'fields': [
                ("mutari", "Mutari"),
                ]
            },
            {
            'title': 'Povești',
            'fields': [
                ("povesti", "Povesti"),
                ]
            },
            
        ]

        return get_sections_serialized(obj, sections)

    def get_title(self, obj):
        return obj.title.split('. ')[-1]


class DescriereSerializer(serializers.ModelSerializer):
    sections = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()

    class Meta:
        model = models.DescrierePage
        fields = ['title', 'sections']

    def get_sections(self, obj):
        sections =  [
            {
            'title': 'Ansamblu construit',
            'fields': [
                ("elemente_ansamblu_construit", "Elemente arhitecturale"),
                ]
            }
            
        ]

        return get_sections_serialized(obj, sections)

    def get_title(self, obj):
        return obj.title.split('. ')[-1]


class ComponentaArtisticaSerializer(serializers.ModelSerializer):
    sections = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()

    class Meta:
        model = models.ComponentaArtisticaPage
        fields = ['title', 'sections']

    def get_sections(self, obj):
        sections =  [
            {
            'title': 'Iconostasul',
            'fields': [
                ("iconostas_naos_altar_tip", ""),
                ("iconostas_naos_altar_numar_intrari", ""),
                ("iconostas_naos_altar_materiale", ""),
                ("iconostas_naos_altar_tehnica", ""),
                ("iconostas_naos_altar_registre", ""),
                ("iconostas_naos_altar_tip_usi", ""),
                ("iconostas_naos_altar_observatii", ""),
                ("poze_iconostas", "Poze")
                ]
            }
            
        ]

        return get_sections_serialized(obj, sections)

    def get_title(self, obj):
        return obj.title.split('. ')[-1]

class ConservareSerializer(serializers.ModelSerializer):
    sections = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()

    class Meta:
        model = models.ConservarePage
        fields = ['title', 'sections']

    def get_sections(self, obj):
        sections =  [
            {
            'title': 'Sit',
            'fields': [
                ("sit", ""),
                ("sit_observatii", ""),
                ("poze_sit", "Poze"),
                ]
            }
            
        ]

        return get_sections_serialized(obj, sections)

    def get_title(self, obj):
        return obj.title.split('. ')[-1]

class ValoareSerializer(serializers.ModelSerializer):
    sections = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()

    class Meta:
        model = models.ValoarePage
        fields = ['title', 'sections']

    def get_sections(self, obj):
        sections =  [
            {
            'title': 'Vechime',
            'fields': [
                ("vechime", "Clasa"),
                ("vechime_observatii", "Observații"),
                ]
            }
            
        ]

        return get_sections_serialized(obj, sections)

    def get_title(self, obj):
        return obj.title.split('. ')[-1]



class BisericaSerializer(serializers.ModelSerializer):
    # identificare = serializers.SerializerMethodField()
    # descriere = serializers.SerializerMethodField()
    # istoric = serializers.SerializerMethodField()
    # componenta_artistica = serializers.SerializerMethodField()
    # conservare = serializers.SerializerMethodField()
    tabs = serializers.SerializerMethodField()

    class Meta:
        model = models.BisericaPage
        fields = ["id", "title", "title", "judet", "localitate", "adresa", "latitudine",
                  "longitudine", "datare_prin_interval_timp", "datare_secol",
                   "conservare", "valoare", "tabs"]

    def get_tabs(self, obj):
        identificare_page = obj.get_children().type(
            models.IdentificarePage)[0].specific
        descriere_page = obj.get_children().type(
            models.DescrierePage)[0].specific
        istoric_page = obj.get_children().type(
            models.IstoricPage)[0].specific
        componenta_artistica_page = obj.get_children().type(
            models.ComponentaArtisticaPage)[0].specific
        conservare_page = obj.get_children().type(
            models.ConservarePage)[0].specific
        valoare_page = obj.get_children().type(
            models.ValoarePage)[0].specific

        tabs = [
            IdentificareSerializer(identificare_page).data,
            DescriereSerializer(descriere_page).data,
            ComponentaArtisticaSerializer(componenta_artistica_page).data,
            IstoricSerializer(istoric_page).data,
            ValoareSerializer(valoare_page).data,
            ConservareSerializer(conservare_page).data,
            ]
        return tabs

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

