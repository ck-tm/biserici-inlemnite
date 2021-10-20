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


def get_nested_model_data(elements):
    print('------')
    print(elements)
    print('------')
    serializer_list = []
    meta_fields = type(elements[0])._meta.fields
    for obj in elements:
        obj_serializer = []
        for field in meta_fields:
            field_value = getattr(obj, field.name)
            if field_value and field.name not in ['page', 'id', 'sort_order']:
                if type(field_value) in [str, float, type(None), int, bool]:
                    obj_serializer.append({
                        'label': field.verbose_name.capitalize(),
                        'value': field_value
                    })
                    # obj_serializer[field.verbose_name.capitalize()] = field_value
                else:
                    obj_serializer.append({
                        'label': field.verbose_name.capitalize(),
                        'value': str(field_value)
                    })
                    # obj_serializer[field.verbose_name.capitalize()] = str(field_value)

        try:
            if obj.poze.exists():
                obj_serializer.append({
                    'label': '_poze',
                    'value':PozaSerializer(obj.poze.all(), many=True).data
                    })
                # obj_serializer['_poze'] = PozaSerializer(obj.poze.all(), many=True).data
        except Exception as e:
            print('******======', e)
        if obj_serializer:
            serializer_list.append(obj_serializer)

    return serializer_list


def get_section_fields(obj, section):
    fields = []
    for field in section['fields']:
        field_obj = getattr(obj, field[0])
        elements = []
        value = None
        try:
            if 'poze_' in field[0]:
                value = PozaSerializer(field_obj.all(), many=True).data
            else:
                all_elements = field_obj.all()
                if all_elements:
                    if type(all_elements[0]).__module__.startswith('nomenclatoare'):
                        value = ' \n'.join([str(x) for x in all_elements])
                    else:
                        value = ', '.join([str(x) for x in all_elements])
                        elements = get_nested_model_data(all_elements)
        except Exception as e:
            print('****', type(e), obj, e)
            if type(field_obj) in [str, float, type(None), int, bool]:
                value = field_obj
            else:
                value = str(field_obj)
        if value :
            field_serializer = {
                'key': field[0] if 'poze_' not in field[0] else '_poze',
                'label': field[1] if field[1] else obj._meta.get_field(field[0]).verbose_name.capitalize(),
                'value': value,
                'elements': elements
            }
            fields.append(field_serializer)
    return fields

def get_sections_serialized(obj, sections):
    sections_serializer = []
    for section in sections:
        section_serializer = {
            'title': section['title'],
            'subsections': [],
            'fields': [],
            }
        if 'subsections' in section.keys():
            for subsection in section['subsections']:
                subsection_serializer = {
                    'title': subsection['title'],
                    'fields': get_section_fields(obj, subsection)
                }
                if subsection_serializer['fields']:
                    section_serializer['subsections'].append(subsection_serializer)
            if section_serializer['subsections']:
                sections_serializer.append(section_serializer)
        else:
            section_serializer['fields'] = get_section_fields(obj, section)
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
                ("judet", ""),
                ("localitate", ""),
                ("adresa", ""),
                ("latitudine", ""),
                ("longitudine", ""),
                ]
            },
            {
            'title': 'Statut',
            'fields': [
                ("statut", ""),
                ]
            },
            {
            'title': 'Hram',
            'fields': [
                ("hram", ""),
                ]
            },
            {
            'title': 'Denumire',
            'fields': [
                ("denumire_actuala", ""),
                ("denumire_precedenta", ""),
                ("denumire_locala", ""),
                ("denumire_oberservatii", ""),
                ]
            },
            {
            'title': 'Cult',
            'fields': [
                ("cult", ""),
                ]
            },
            {
            'title': 'Utilizare',
            'fields': [
                ("utilizare", ""),
                ("utilizare_observatii", ""),
                ]
            },
            {
            'title': 'Singularitate',
            'fields': [
                ("singularitate", ""),
                ("singularitate_observatii", ""),
                ]
            },
            {
            'title': 'Funcțiune',
            'fields': [
                ("functiune", ""),
                ("functiune_observatii", ""),
                ("functiune_initiala", ""),
                ("functiune_initiala_observatii", ""),
                ]
            },
            {
            'title': 'Proprietate',
            'fields': [
                ("proprietate_actuala", ""),
                ("proprietate_observatii", ""),
                ("proprietar_actual", ""),
                ]
            },
            {
            'title': 'Înscriere documente cadastrale',
            'fields': [
                ("inscriere_documente_cadastrale", ""),
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
            'title': 'Istoric',
            'subsections':[
                {
                'title': 'Datare',
                'fields': [
                    ("sursa_datare", ""),
                    ("an_constructie", ""),
                    ("datare_prin_interval_timp", ""),
                    ("datare_secol", ""),
                    ("datare_secol_observatii", ""),
                    ("datare_secol_sursa", ""),
                    ]
                },
                {
                'title': 'Studiu dendrocronologic',
                'fields': [
                    ("studiu_dendocronologic_an", ""),
                    ("studiu_dendocronologic_autor", ""),
                    ("studiu_dendocronologic_fisier", ""),
                    ("studiu_dendocronologic_observatii", ""),
                    ]
                },
                {
                'title': 'Pisanie',
                'fields': [
                    ("pisanie_traducere", ""),
                    ("pisanie_secol_observatii", ""),
                    ("pisanie_secol_sursa", ""),
                    ]
                }
            ]},
            {
            'title': 'Persoane',
            'subsections':[
                {
                    'title': 'Ctitori',
                    'fields': [
                        ("ctitori", "Nume")
                    ]
                },
                {
                    'title': 'Meșteri',
                    'fields': [
                        ("mesteri", "Nume")
                    ]
                },
                {
                    'title': 'Zugravi',
                    'fields': [
                        ("zugravi", "Nume")
                    ]
                },
                {
                    'title': 'Personalități',
                    'fields': [
                        ("personalitati", "Nume")
                    ]
                }
            ]},
            {
            'title': 'Evenimente',
            'subsections': [{
                'title': '',
                'fields': [
                    ("evenimente", "Evenimente"),
                ]
                }
            ]},

            {
            'title': 'Mutări',
            'subsections': [{
                'title': '',
                'fields': [
                    ("mutari", "Mutări"),
                    ]
                }
            ]
            },
            {
            'title': 'Povești',
            'subsections': [{
                'title': '',
                'fields': [
                    ("povesti", "Povești"),
                    ]
                }]
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
                'title': 'Localizare/Peisaj',
                'subsections': [
                    {
                    'title': 'Amplasament',
                    'fields': [
                        ("amplasament", ""),
                        ("poze_amplasament", "Poze"),
                        ]
                    },
                    {
                    'title': 'Topografie',
                    'fields': [
                        ("topografie", ""),
                        ]
                    },
                    {
                    'title': 'Toponim',
                    'fields': [
                        ("toponim", ""),
                        ("toponim_sursa", ""),
                        ]
                    },
                    {
                    'title': 'Relația cu cimitirul',
                    'fields': [
                        ("relatia_cu_cimitirul", ""),
                        ]
                    },
                    {
                    'title': 'Peisagistica sitului',
                    'fields': [
                        ("peisagistica_sitului", ""),
                        ("poze_peisagistica_sitului", "Poze"),
                        ]
                    },
                    {
                    'title': 'Observații',
                    'fields': [
                        ("observatii", ""),
                        ]
                    },
                ]
            },
            {
                'title': 'Ansamblu construit',
                'subsections': [
                    {
                    'title': 'Elemente arhitecturale',
                    'fields': [
                        ("elemente_ansamblu_construit", "Elemente"),
                        ]
                    },
                    {
                    'title': 'Alte componente importante ale sitului',
                    'fields': [
                        ("elemente_importante", "Elemente"),
                        ]
                    }

                ]
            },
            {
                'title': 'Arhitectura bisericii',
                'subsections': [
                    {
                    'title': 'Materiale',
                    'fields': [
                        ("materiale", ""),
                        ("detalii_materiale", ""),
                        ]
                    },
                    {
                    'title': 'Planimetria bisericii',
                    'fields': [
                        ("planimetria_bisericii", ""),
                        ]
                    },
                    {
                    'title': 'Accese',
                    'fields': [
                        ("numar_accese_pridvor", ""),
                        ("numar_accese_pridvor_observatii", ""),
                        ("numar_accese_pronaos", ""),
                        ("numar_accese_pronaos_observatii", ""),
                        ("numar_accese_naos", ""),
                        ("numar_accese_naos_observatii", ""),
                        ("numar_accese_altar", ""),
                        ("numar_accese_altar_observatii", ""),
                        ("poze_accese", "Poze"),
                        ]
                    },
                    {
                    'title': 'Ferestre',
                    'fields': [
                        ("numar_ferestre_pridvor", ""),
                        ("numar_ferestre_pridvor_observatii", ""),
                        ("numar_ferestre_pronaos", ""),
                        ("numar_ferestre_pronaos_observatii", ""),
                        ("numar_ferestre_naos", ""),
                        ("numar_ferestre_naos_observatii", ""),
                        ("numar_ferestre_altar", ""),
                        ("numar_ferestre_altar_observatii", ""),
                        ("poze_ferestre", "Poze"),
                        ]
                    },
                    {
                    'title': 'Ochieși / Aerisitoare',
                    'fields': [
                        ("ochiesi_aerisitoare", ""),
                        ("numar_ochiesi", ""),
                        ("ochiesi_aerisitoare_observatii", ""),
                        ("poze_ochiesi", "Poze"),
                        ]
                    },
                    {
                    'title': 'Solee',
                    'fields': [
                        ("solee", ""),
                        ("solee_observatii", ""),
                        ("poze_solee", "Poze"),
                        ]
                    },
                    {
                    'title': 'Masă altar',
                    'fields': [
                        ("masa_altar_material_picior", ""),
                        ("masa_altar_material_blat", ""),
                        ("masa_altar_observatii", ""),
                        ("poze_masa_atlar", "Poze"),
                        ]
                    },
                    {
                    'title': 'Bolți',
                    'fields': [
                        ("bolta_peste_pronaos", ""),
                        ("bolta_peste_pronaos_material", ""),
                        ("bolta_peste_pronaos_structura", ""),
                        ("bolta_peste_pronaos_tipul_de_arc", ""),
                        ("bolta_peste_pronaos_observatii", ""),
                        ("bolta_peste_naos", ""),
                        ("bolta_peste_naos_material", ""),
                        ("bolta_peste_naos_structura", ""),
                        ("bolta_peste_naos_tipul_de_arc", ""),
                        ("bolta_peste_naos_observatii", ""),
                        ("bolta_peste_altar", ""),
                        ("bolta_peste_altar_tip", ""),
                        ("bolta_peste_altar_material", ""),
                        ("bolta_peste_altar_structura", ""),
                        ("bolta_peste_altar_tipul_de_arc", ""),
                        ("bolta_peste_altar_observatii", ""),
                        ]
                    },
                    {
                    'title': 'Cor',
                    'fields': [
                        ("cor", ""),
                        ("cor_material", ""),
                        ("cor_observatii", ""),
                        ("poze_cor", "Poze"),
                        ]
                    },
                    {
                    'title': 'Șarpantă corp',
                    'fields': [
                        ("sarpanta_tip", ""),
                        ("sarpanta_veche_nefolosita", ""),
                        ("sarpanta_numar_turnulete", ""),
                        ("sarpanta_numar_cruci", ""),
                        ("sarpanta_material_cruci", ""),
                        ("sarpanta_observatii", ""),
                        ("poze_sarpanta", "Poze"),
                        ]
                    },
                    {
                    'title': 'Turn',
                    'fields': [
                        ("turn_dimensiune", ""),
                        ("turn_tip", ""),
                        ("turn_numar", ""),
                        ("turn_numar_stalpi", ""),
                        ("turn_plan", ""),
                        ("turn_amplasare", ""),
                        ("turn_galerie", ""),
                        ("turn_numar_arcade", ""),
                        ("turn_numar_arcade_observatii", ""),
                        ("turn_asezare_talpi", ""),
                        ("turn_relatie_talpi", ""),
                        ("turn_numar_talpi", ""),
                        ("turn_observatii", ""),
                        ("poze_turn", "Poze"),
                        ]
                    },
                    {
                    'title': 'Clopote',
                    'fields': [
                        ("clopote", "An"),
                        ("poze_clopote", "Poze"),
                        ]
                    },
                    {
                    'title': 'Turle',
                    'fields': [
                        ("turle_exista", ""),
                        ("turle_numar", ""),
                        ("turle_pozitionare", ""),
                        ("turle_numar_goluri", ""),
                        ("turle_forma_sarpanta", ""),
                        ("turle_observatii", ""),
                        ("poze_turle", "Poze"),
                        ]
                    },
                    {
                    'title': 'Poze Generale Exterior',
                    'fields': [
                        ("poze_generale_exterior", "Poze"),
                        ]
                    },
                    {
                    'title': 'Poze Generale Interior',
                    'fields': [
                        ("poze_generale_interior", "Poze"),
                        ]
                    }

                ]
            },
            
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
            IstoricSerializer(istoric_page).data,
            DescriereSerializer(descriere_page).data,
            # ComponentaArtisticaSerializer(componenta_artistica_page).data,
            # ValoareSerializer(valoare_page).data,
            # ConservareSerializer(conservare_page).data,
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

