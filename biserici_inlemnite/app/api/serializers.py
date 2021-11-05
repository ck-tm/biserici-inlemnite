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


class PozaSerializer(serializers.Serializer):
    observatii = serializers.CharField()
    poza = serializers.SerializerMethodField()

    class Meta:
        fields = ['observatii', 'poza']

    def get_poza(self, obj):
        return obj.rendition


def get_nested_model_data(elements):
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
            # if obj.poze.exists():
            obj_serializer.append({
                'label': 'Poze',
                'type': 'poze',
                # 'value': obj.poze.count()
                'value':PozaSerializer(obj.poze.all(), many=True).data
                })
                # obj_serializer['_poze'] = PozaSerializer(obj.poze.all(), many=True).data
        except Exception as e:
            # print('******======', e)
            pass
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
                        value = ', '.join([str(x) for x in all_elements])
                    else:
                        value = ', '.join([str(x) for x in all_elements])
                        elements = get_nested_model_data(all_elements)
        except Exception as e:
            # print('****', field,  type(e), obj, e)


            if type(field_obj) in [str, float, type(None), int, bool]:
                if obj._meta.get_field(field[0]).choices:
                    value = getattr(obj, f'get_{field[0]}_display')()
                else:
                    value = field_obj
            else:
                if field[0] == 'inscriere_documente_cadastrale':
                    print('not in str')
                value = str(field_obj)
        if value :
            field_serializer = {
                'key': field[0] if 'poze_' not in field[0] else 'Poze',
                'type': 'poze' if 'poze_' in field[0] else 'normal',
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
        # prefetch_list = []
        # for field in model._meta.fields:
        #     if field.get_internal_type() == 'ForeignKey':
        #         prefetch_list.append(field.name)
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
                        ("numar_accese_pridvor_observatii", "Observații accese pridvor"),
                        ("numar_accese_pronaos", ""),
                        ("numar_accese_pronaos_observatii", "Observații accese pronaos"),
                        ("numar_accese_naos", ""),
                        ("numar_accese_naos_observatii", "Observații accese naos"),
                        ("numar_accese_altar", ""),
                        ("numar_accese_altar_observatii", "Observații accese altar"),
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
                        ("masa_altar_observatii", ""),
                        ("poze_masa_atlar", "Poze"),
                        ]
                    },
                    {
                    'title': 'Bolți',
                    'fields': [
                        ("bolta_peste_pronaos", ""),
                        ("bolta_peste_pronaos_structura", ""),
                        ("bolta_peste_pronaos_tipul_de_arc", ""),
                        ("bolta_peste_pronaos_observatii", ""),
                        ("bolta_peste_naos", ""),
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
            {
                'title': 'Structura',
                'subsections': [
                    {
                    'title': 'Fundația',
                    'fields': [
                        ("fundatia", ""),
                        ("fundatia_observatii", ""),
                        ("poze_fundatie", "Poze"),
                        ]
                    },
                    {
                    'title': 'Sistem structural al corpului bisericii',
                    'fields': [
                        ("sistem_structural", ""),
                        ]
                    },
                    {
                    'title': 'Sistem structural al corpului bisericii în cheotoare',
                    'fields': [
                        ("sistem_in_cheotoare", ""),
                        ("sistem_in_cheotoare_observatii", ""),
                        ("poze_structura_cheotoare", "Poze"),
                        ]
                    },
                    {
                    'title': 'Sistem structural al corpului bisericii în căței',
                    'fields': [
                        ("sistem_in_catei", ""),
                        ("sistem_in_catei_observatii", ""),
                        ("poze_structura_catei", ""),
                        ]
                    },
                    {
                    'title': 'Sistem structural al corpului bisericii mixt',
                    'fields': [
                        ("sistem_mixt", ""),
                        ("poze_structura_mixt", ""),
                        ]
                    },
                    {
                    'title': 'Tiranți',
                    'fields': [
                        ("tiranti_numar", ""),
                        ("tiranti_tip", ""),
                        ("tiranti_observatii", ""),
                        ("poze_tiranti", "Poze"),
                        ]
                    },
                ]
            },
            {
                'title': 'Finisaje',
                'subsections': [
                    {
                    'title': 'Exterior corp biserică',
                    'fields': [
                        ("finisaj_exterior_tip", "Tip"),
                        ("finisaj_exterior_observatii", ""),
                        ("poze_exterior_corp", "Poze"),
                        ]
                    },
                    {
                    'title': 'Învelitoare corp biserică',
                    'fields': [
                        ("invelitoare_corp_material", ""),
                        ("invelitoare_corp_sindrila_lungime", ""),
                        ("invelitoare_corp_sindrila_latime_medie", ""),
                        ("invelitoare_corp_sindrila_grosime_medie", ""),
                        ("invelitoare_corp_sindrila_pasul_latuirii", ""),
                        ("invelitoare_corp_sindrila_pasul_baterii", ""),
                        ("invelitoare_corp_sindrila_numar_straturi", ""),
                        ("invelitoare_corp_sindrila_cu_horj", ""),
                        ("invelitoare_corp_sindrlia_tipul_de_batere", ""),
                        ("invelitoare_corp_sindrlia_tipul_prindere", ""),
                        ("invelitoare_corp_sindrlia_forma_botului", ""),
                        ("invelitoare_corp_sindrila_cu_tesitura", ""),
                        ("invelitoare_corp_sindrlia_prelucrare", ""),
                        ("invelitoare_corp_sindrlia_esenta_lemnoasa", ""),
                        ("invelitoare_corp_observatii", ""),
                        ("poze_invelitoare", "Poze"),
                        ]
                    },
                    {
                    'title': 'Învelitoare turn',
                    'fields': [
                        ("invelitoare_turn_material", ""),
                        ("invelitoare_turn_sindrila_lungime", ""),
                        ("invelitoare_turn_sindrila_latime_medie", ""),
                        ("invelitoare_turn_sindrila_grosime_medie", ""),
                        ("invelitoare_turn_sindrila_pasul_latuirii", ""),
                        ("invelitoare_turn_sindrila_pasul_baterii", ""),
                        ("invelitoare_turn_sindrila_numar_straturi", ""),
                        ("invelitoare_turn_sindrila_cu_horj", ""),
                        ("invelitoare_turn_sindrlia_tipul_de_batere", ""),
                        ("invelitoare_turn_sindrlia_tipul_prindere", ""),
                        ("invelitoare_turn_sindrlia_forma_botului", ""),
                        ("invelitoare_turn_sindrila_cu_tesitura", ""),
                        ("invelitoare_turn_sindrlia_prelucrare", ""),
                        ("invelitoare_turn_sindrlia_esenta_lemnoasa", ""),
                        ("invelitoare_turn_observatii", ""),
                        ("poze_invelitoare_turn", "Poze"),
                        ]
                    },
                    {
                    'title': 'Închidere tambur turn',
                    'fields': [
                        ("inchidere_tambur_turn_material", ""),
                        ("inchidere_tambur_turn_sindrila_lungime", ""),
                        ("inchidere_tambur_turn_sindrila_latime_medie", ""),
                        ("inchidere_tambur_turn_sindrila_grosime_medie", ""),
                        ("inchidere_tambur_turn_sindrila_pasul_latuirii", ""),
                        ("inchidere_tambur_turn_sindrila_pasul_baterii", ""),
                        ("inchidere_tambur_turn_sindrila_numar_straturi", ""),
                        ("inchidere_tambur_turn_sindrila_cu_horj", ""),
                        ("inchidere_tambur_turn_sindrlia_tipul_de_batere", ""),
                        ("inchidere_tambur_turn_sindrlia_tipul_prindere", ""),
                        ("inchidere_tambur_turn_sindrlia_forma_botului", ""),
                        ("inchidere_tambur_turn_sindrila_cu_tesitura", ""),
                        ("inchidere_tambur_turn_sindrlia_prelucrare", ""),
                        ("inchidere_tambur_turn_sindrlia_esenta_lemnoasa", ""),
                        ("inchidere_tambur_turn_observatii", ""),
                        ("poze_inchidere_tambur", "Poze"),
                        ]
                    },
                    {
                    'title': 'Învelitoare turle',
                    'fields': [
                        ("invelitoare_turle_material", "Material"),
                        ("invelitoare_turle_sindrila_lungime", ""),
                        ("invelitoare_turle_sindrila_latime_medie", ""),
                        ("invelitoare_turle_sindrila_grosime_medie", ""),
                        ("invelitoare_turle_sindrila_pasul_latuirii", ""),
                        ("invelitoare_turle_sindrila_pasul_baterii", ""),
                        ("invelitoare_turle_sindrila_numar_straturi", ""),
                        ("invelitoare_turle_sindrila_cu_horj", ""),
                        ("invelitoare_turle_sindrlia_tipul_de_batere", ""),
                        ("invelitoare_turle_sindrlia_tipul_prindere", ""),
                        ("invelitoare_turle_sindrlia_forma_botului", ""),
                        ("invelitoare_turle_sindrila_cu_tesitura", ""),
                        ("invelitoare_turle_sindrlia_prelucrare", ""),
                        ("invelitoare_turle_sindrlia_esenta_lemnoasa", ""),
                        ("invelitoare_turle_observatii", ""),
                        ("poze_invelitoare_turle", "Poze"),
                        ]
                    },
                    {
                    'title': 'Finisaje Portic',
                    'fields': [
                        ("finisaje_portic", ""),
                        ]
                    },
                    {
                    'title': 'Pronaos',
                    'fields': [
                        ("finisaje_pronaos", "Finisaje"),
                        ]
                    },
                    {
                    'title': 'Naos',
                    'fields': [
                        ("finisaje_naos", "Finisaje"),
                        ]
                    },
                    {
                    'title': 'Altar',
                    'fields': [
                        ("finisaje_altar", "Finisaje"),
                        ]
                    },
                ]
            },
            {
                'title': 'Intervenții',
                'subsections': [
                    {
                    'title': 'Învelitoare actuală de lemn',
                    'fields': [
                        ("invelitoare_actuala_an", ""),
                        ("invelitoare_actuala_observatii", ""),
                        ]
                    },
                    {
                    'title': 'Etape anterioare vizibile ale învelitorii',
                    'fields': [
                        ("interventii_invelitoare_etape_anterioare_vizibile", ""),
                        ("interventii_invelitoare_sindrila_pasul_latuirii", ""),
                        ("interventii_invelitoare_sindrila_numar_straturi", ""),
                        ("interventii_invelitoare_sindrila_cu_horj", ""),
                        ("interventii_invelitoare_sindrlia_tipul_de_batere", ""),
                        ("interventii_invelitoare_sindrlia_forma_botului", ""),
                        ("interventii_invelitoare_sindrila_cu_tesitura", ""),
                        ("interventii_invelitoare_sindrlia_esenta_lemnoasa", ""),
                        ("interventii_invelitoare_alte_tipuri_invelitoare", ""),
                        ("interventii_invelitoare_observatii", ""),
                        ]
                    },
                    {
                    'title': 'Alte etape istorice vizibile',
                    'fields': [
                        ("etape_istorice_vizibile", "Etape"),
                        ]
                    },
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
                'title': '',
                'subsections': [
                    {
                    'title': 'Proscomidie',
                    'fields': [
                        ("proscomidie", ""),
                        ("suport_proscomidie", "Suport"),
                        ("poze_proscomidie", "Poze"),
                        ]
                    },
                    {
                    'title': 'Elemente Sculptate',
                    'fields': [
                        ("elemente_sculptate", ""),
                        ("elemente_observatii", ""),
                        ("poze_elemente_sculptate", "Poze"),
                        ]
                    },
                    {
                    'title': 'Alte icoane vechi',
                    'fields': [
                        ("alte_icoane_vechi", ""),
                        ("alte_icoane_vechi_observatii", ""),
                        ("poze_icoane_vechi", "Poze"),
                        ]
                    },
                    {
                    'title': 'Obiecte de cult',
                    'fields': [
                        ("obiecte_de_cult", "Obiecte"),
                        ("obiecte_de_cult_observatii", ""),
                        ("poze_obiecte_de_cult", "Poze"),
                        ]
                    },
                    {
                    'title': 'Mobiliere',
                    'fields': [
                        ("mobiliere", "Mobiliere"),
                        ("mobiliere_observatii", ""),
                        ("poze_mobiliere", "Poze"),
                        ]
                    },
                    {
                    'title': 'Obiecte de cult înstrăinate',
                    'fields': [
                        ("obiecte_instrainate", ""),
                        ("obiecte_instrainate_observatii", ""),
                        ("poze_obiecte_instrainate", "Poze"),
                        ]
                    },
                    
                ]
            },
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
            },
            {
            'title': 'Peretele despărțitor pronaos-naos',
            'fields': [
                ("iconostas_pronaos_naos_tip", ""),
                ("iconostas_pronaos_naos_materiale", ""),
                ("iconostas_pronaos_naos_numar_intrari", ""),
                ("iconostas_pronaos_naos_tehnica", "Tehnică"),
                ("iconostas_pronaos_naos_observatii", ""),
                ("poze_perete_despartitor", "Poze"),
                ]
            },
            {
            'title': 'Altarul',
            'fields': [
                    ("altar_placa_mesei", "Placa mesei"),
                    ("altar_piciorul_mesei", "Piciorul mesei"),
                    ("altar_observatii", ""),
                    ("poze_altar", "Poze"),
                ]
            },
            {
            'title': 'Pictură exterioară',
            'fields': [
                    ("pictura_exterioara_localizare", ""),
                    ("pictura_exterioara_localizare_observatii", ""),
                    ("pictura_exterioara_tehnica", ""),
                    ("pictura_exterioara_suport", "Suport"),
                    ("pictura_exterioara_numar_straturi_pictura", ""),
                    ("poze_pictura_exterioara", "Poze"),
                    ("pictura_exterioara_sursa_datare", "Sursă datare"),
                    ("pictura_exterioara_anul_picturii", ""),
                    ("pictura_exterioara_datare_prin_interval_timp", ""),
                    ("pictura_exterioara_datare_secol", ""),
                    ("pictura_exterioara_datare_observatii", "")
                ]
            },
            {
            'title': 'Pictură interioară',
            'fields': [
                    ("pictura_interioara_localizare", ""),
                    ("pictura_interioara_localizare_observatii", ""),
                    ("pictura_interioara_tehnica_pictura", ""),
                    ("pictura_interioara_suport", "Suport"),
                    ("pictura_interioara_numar_straturi_pictura", ""),
                    ("poze_pictura_interioara", "Poze"),
                    ("pictura_interioara_sursa_datare", "Sursă datare"),
                    ("pictura_interioara_anul_picturii", ""),
                    ("pictura_interioara_datare_prin_interval_timp", ""),
                    ("pictura_interioara_datare_secol", ""),
                    ("pictura_interioara_datare_observatii", "")
                ]
            },
            {
            'title': 'Etape istorice vizibile',
            'fields': [
                    ("etape_istorice_vizibile", "Etape"),
                ]
            },
            
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
            'subsections': [
                {
                    'title': 'Sit',
                    'fields': [
                        ("sit", ""),
                        ("sit_pericol", ""),
                        ("sit_observatii", ""),
                        ("poze_sit", "Poze"),
                        ]
                },
                {
                    'title': 'Elemente arhitecturale',
                    'fields': [
                        ("elemente_arhitecturale", ""),
                        ("elemente_arhitecturale_pericol", ""),
                        ("elemente_arhitecturale_observatii", ""),
                        ("poze_elemente_arhitecturale", "Poze"),
                        ]
                },
                {
                    'title': 'Alte elemente importante',
                    'fields': [
                        ("alte_elemente_importante", ""),
                        ("alte_elemente_importante_pericol", ""),
                        ("alte_elemente_importante_observatii", ""),
                        ("poze_alte_elemente_importante", "Poze"),
                        ]
                },
                {
                    'title': 'Vegetație',
                    'fields': [
                        ("vegetatie", ""),
                        ("vegetatie_pericol", ""),
                        ("vegetatie_observatii", ""),
                        ("poze_vegetatie", "Poze"),
                        ]
                },
                ]
            },
            {
            'title': 'Structura',
            'subsections': [
                {
                    'title': 'Teren',
                    'fields': [
                        ("teren", ""),
                        ("teren_pericol", ""),
                        ("teren_observatii", ""),
                        ("poze_teren", "Poze"),
                        ]
                },
                {
                    'title': 'Fundații',
                    'fields': [
                        ("fundatii", ""),
                        ("fundatii_pericol", ""),
                        ("fundatii_observatii", ""),
                        ("poze_fundatii", "Poze"),
                        ]
                },
                {
                    'title': 'Tălpi',
                    'fields': [
                        ("talpi", ""),
                        ("talpi_pericol", ""),
                        ("talpi_observatii", ""),
                        ("poze_talpi", "Poze"),
                        ]
                },
                {
                    'title': 'Corp biserică',
                    'fields': [
                        ("corp_biserica", ""),
                        ("corp_biserica_pericol", ""),
                        ("corp_biserica_observatii", ""),
                        ("poze_corp_biserica", "Poze"),
                        ]
                },
                {
                    'title': 'Bolți',
                    'fields': [
                        ("bolti", ""),
                        ("bolti_pericol", ""),
                        ("bolti_observatii", ""),
                        ("poze_bolti", "Poze"),
                        ]
                },
                {
                    'title': 'Cosoroabe',
                    'fields': [
                        ("cosoroabe", ""),
                        ("cosoroabe_pericol", ""),
                        ("cosoroabe_observatii", ""),
                        ("poze_cosoroabe", "Poze"),
                        ]
                },
                {
                    'title': 'Șarpantă corp biserică',
                    'fields': [
                        ("sarpanta_peste_corp_biserica", ""),
                        ("sarpanta_peste_corp_biserica_pericol", ""),
                        ("sarpanta_peste_corp_biserica_observatii", ""),
                        ("poze_sarpanta_corp_biserica", "Poze"),
                        ]
                },
                {
                    'title': 'Turn',
                    'fields': [
                        ("turn", ""),
                        ("turn_pericol", ""),
                        ("turn_observatii", ""),
                        ("poze_turn", "Poze"),
                        ]
                },
                
                ]
            },
            {
            'title': 'Finisaje',
            'subsections': [
                {
                    'title': 'Zona din jurul biserici',
                    'fields': [
                        ("zona_din_jurul_biserici", ""),
                        ("zona_din_jurul_biserici_pericol", ""),
                        ("zona_din_jurul_biserici_observatii", ""),
                        ("poze_zona_din_jurul_biserici", "Poze"),
                        ]
                },
                {
                    'title': 'Pardoseli interioare',
                    'fields': [
                        ("pardoseli_interioare", ""),
                        ("pardoseli_interioare_pericol", ""),
                        ("pardoseli_interioare_observatii", ""),
                        ("poze_pardoseli_interioare", "Poze"),
                        ]
                },
                {
                    'title': 'Finisaj pereți exteriori',
                    'fields': [
                        ("finisaj_exterior", ""),
                        ("finisaj_exterior_pericol", ""),
                        ("finisaj_exterior_observatii", ""),
                        ("poze_finisaj_exterior", "Poze"),
                        ]
                },
                {
                    'title': 'Finisaj pereți interiori',
                    'fields': [
                        ("finisaj_pereti_interiori", ""),
                        ("finisaj_pereti_interiori_pericol", ""),
                        ("finisaj_pereti_interiori_observatii", ""),
                        ("poze_finisaj_pereti_interiori", "Poze"),
                        ]
                },
                {
                    'title': 'Finisaj tavane și bolți',
                    'fields': [
                        ("finisaj_tavane_si_bolti", ""),
                        ("finisaj_tavane_si_bolti_pericol", ""),
                        ("finisaj_tavane_si_bolti_observatii", ""),
                        ("poze_finisaj_tavane_si_bolti", "Poze"),
                        ]
                },
                {
                    'title': 'Tâmplării',
                    'fields': [
                        ("tamplarii", ""),
                        ("tamplarii_pericol", ""),
                        ("tamplarii_observatii", ""),
                        ("poze_tamplarii", "Poze"),
                        ]
                },
                {
                    'title': 'Învelitoare șarpantă și turn',
                    'fields': [
                        ("invelitoare_sarpanta_si_turn", ""),
                        ("invelitoare_sarpanta_si_turn_pericol", ""),
                        ("invelitoare_sarpanta_si_turn_observatii", ""),
                        ("poze_invelitoare_sarpanta_si_turn", "Poze"),
                        ]
                },
                {
                    'title': 'Instalație electrică',
                    'fields': [
                        ("instalatie_electrica", ""),
                        ("instalatie_electrica_pericol", ""),
                        ("instalatie_electrica_observatii", ""),
                        ("poze_instalatie_electrica", "Poze"),
                        ]
                },
                {
                    'title': 'Instalație termică',
                    'fields': [
                        ("instalatie_termica", ""),
                        ("instalatie_termica_pericol", ""),
                        ("instalatie_termica_observatii", ""),
                        ("poze_instalatie_termica", "Poze"),
                        ]
                },
                {
                    'title': 'Paratrăznet',
                    'fields': [
                        ("paratraznet", ""),
                        ("paratraznet_pericol", ""),
                        ("paratraznet_observatii", ""),
                        ("poze_paratraznet", "Poze"),
                        ]
                },
                
                ]
            },
            {
            'title': 'Componenta Artistică',
            'subsections': [
                {
                    'title': 'Strat pictural',
                    'fields': [
                        ("strat_pictural", ""),
                        ("strat_pictural_pericol", ""),
                        ("strat_pictural_observatii", ""),
                        ("poze_strat_pictural", "Poze"),
                        ]
                },
                {
                    'title': 'Obiecte de cult',
                    'fields': [
                        ("obiecte_de_cult", ""),
                        ("obiecte_de_cult_pericol", ""),
                        ("obiecte_de_cult_observatii", ""),
                        ("poze_obiecte_de_cult", "Poze"),
                        ]
                },
                {
                    'title': 'Mobilier',
                    'fields': [
                        ("mobilier", ""),
                        ("mobilier_pericol", ""),
                        ("mobilier_observatii", ""),
                        ("poze_mobilier", "Poze"),
                        ]
                }
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
                        ("vechime", ""),
                        ("vechime_observatii", ""),
                    ]
                },{
                'title': 'Integritate / Autenticitate',
                'fields': [
                    ("integritate", ""),
                    ("integritate_observatii", ""),
                ]
                },{
                'title': 'Unicitate',
                'fields': [
                    ("unicitate", ""),
                    ("unicitate_observatii", ""),
                ]
                },{
                'title': 'Valoare memorială',
                'fields': [
                    ("valoare_memoriala", ""),
                    ("valoare_memoriala_observatii", ""),
                ]
                },{
                'title': 'Valoarea peisajului cultural',
                'fields': [
                    ("peisaj_cultural", ""),
                    ("peisaj_cultural_observatii", ""),
                ]
                },{
                'title': 'Valoarea sitului',
                'fields': [
                    ("valoare_sit", ""),
                    ("valoare_sit_observatii", ""),
                ]
                },{
                'title': 'Valoarea estetică',
                'fields': [
                    ("estetica", ""),
                    ("estetica_observatii", ""),
                ]
                },{
                'title': 'Valoarea meșteșugului',
                'fields': [
                    ("mestesug", ""),
                    ("mestesug_observatii", ""),
                ]
                },{
                'title': 'Valoarea componentei artistice',
                'fields': [
                    ("pictura", ""),
                    ("pictura_observatii", ""),
                ]
                },{
                'title': 'Folosința actuală',
                'fields': [
                    ("folosinta_actuala", ""),
                    ("folosinta_actuala_observatii", ""),
                ]
                },{
                'title': 'Relevanța actuală pentru comunitate',
                'fields': [
                    ("relevanta_actuala", ""),
                    ("relevanta_actuala_observatii", ""),
                ]
                },{
                'title': 'Potențial',
                'fields': [
                    ("potential", ""),
                    ("potential_observatii", ""),
                ]
                }
                
            ]

        return get_sections_serialized(obj, sections)

    def get_title(self, obj):
        return obj.title.split('. ')[-1]


class BisericaSerializer(serializers.ModelSerializer):
    identificare_page = IdentificareSerializer()
    istoric_page = IstoricSerializer()
    descriere_page = DescriereSerializer()
    componenta_artistica_page = ComponentaArtisticaSerializer()
    valoare_page = ValoareSerializer()
    conservare_page = ConservareSerializer()

    class Meta:
        model = models.BisericaPage
        fields = ["id", "title", "title", "judet", "localitate", "adresa", "latitudine",
                  "longitudine", "datare_prin_interval_timp", "datare_secol",
                   "conservare", "valoare", "istoric_page", "identificare_page", "descriere_page",
                   "componenta_artistica_page","valoare_page","conservare_page"]


class BisericaListSerializer(serializers.ModelSerializer):
    poze = PozaSerializer(many=True)

    datare = serializers.SerializerMethodField()

    class Meta:
        model = models.BisericaPage
        fields = ["id", "title", "judet", "localitate", "adresa", "latitudine",
                  "longitudine", "datare", "conservare",
                  "valoare", "prioritizare", "poze"]

    def get_datare(self, obj):
        if obj.datare_an:
            return f'Anul {obj.datare_an}' 
        if obj.datare_prin_interval_timp:
            return obj.datare_prin_interval_timp
        if obj.datare_secol:
            return f'Secolul {obj.datare_secol}'


class PartnerSerializer(serializers.ModelSerializer):
    logo = ImageRenditionField('width-400')

    class Meta:
        model = models.ParteneriProiect
        fields = ["logo", "link"]


class AboutSerializer(serializers.ModelSerializer):
    parteneri = PartnerSerializer(many=True)

    class Meta:
        model = models.AboutPage
        fields = ["title", "body", "parteneri"]

