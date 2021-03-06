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
        field_type = None

        try:
            if 'poze_' in field[0]:
                value = PozaSerializer(field_obj.all(), many=True).data
            else:
                all_elements = field_obj.all()
                if all_elements:
                    if type(all_elements[0]).__module__.startswith('nomenclatoare'):
                        value = ', '.join([str(x) for x in all_elements if str(x) != 'None'])
                    else:
                        value = ', '.join([str(x) for x in all_elements if str(x) != 'None'])

                        elements = get_nested_model_data(all_elements)
        except Exception as e:
            # print('****', field,  type(e), obj, e)
            # print(field)
            if type(field_obj) in [str, float, type(None), int, bool]:
                if obj._meta.get_field(field[0]).choices:

                    value = getattr(obj, f'get_{field[0]}_display')()
                else:
                    value = field_obj
            else:
                if field[0] == 'planimetria_bisericii':
                    field_type = 'poza'
                    try:
                        planimetrie = field_obj.get_rendition('width-200')
                        rendition = {
                            "url": planimetrie.url,
                            "width": planimetrie.width,
                            "height": planimetrie.height,
                            "alt": planimetrie.alt
                        }
                    except:
                        rendition = None
                    value = rendition
                else:
                    value = str(field_obj)
        if value :
            if not field_type:
                field_type = 'poze' if 'poze_' in field[0] else 'normal'
            field_serializer = {
                'key': field[0] if 'poze_' not in field[0] else 'Poze',
                'type': field_type,
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
    type = serializers.SerializerMethodField()

    class Meta:
        model = models.IstoricPage
        fields = ['title', 'sections', 'type']

    def get_type(self, obj):
        return 'sections'

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
            'title': 'Func??iune',
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
            'title': '??nscriere documente cadastrale',
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
    type = serializers.SerializerMethodField()

    class Meta:
        model = models.IstoricPage
        fields = ['title', 'sections', 'type']

    def get_type(self, obj):
        return 'sections'

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
                    'title': 'Me??teri',
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
                    'title': 'Personalit????i',
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
            'title': 'Mut??ri',
            'subsections': [{
                'title': '',
                'fields': [
                    ("mutari", "Mut??ri"),
                    ]
                }
            ]
            },
            {
            'title': 'Pove??ti',
            'subsections': [{
                'title': '',
                'fields': [
                    ("povesti", "Pove??ti"),
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
    type = serializers.SerializerMethodField()

    class Meta:
        model = models.IstoricPage
        fields = ['title', 'sections', 'type']

    def get_type(self, obj):
        return 'sections'


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
                    'title': 'Rela??ia cu cimitirul',
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
                    'title': 'Observa??ii',
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
                        ("numar_accese_pridvor_observatii", "Observa??ii accese pridvor"),
                        ("numar_accese_pronaos", ""),
                        ("numar_accese_pronaos_observatii", "Observa??ii accese pronaos"),
                        ("numar_accese_naos", ""),
                        ("numar_accese_naos_observatii", "Observa??ii accese naos"),
                        ("numar_accese_altar", ""),
                        ("numar_accese_altar_observatii", "Observa??ii accese altar"),
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
                    'title': 'Ochie??i / Aerisitoare',
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
                    'title': 'Mas?? altar',
                    'fields': [
                        ("masa_altar_observatii", ""),
                        ("poze_masa_atlar", "Poze"),
                        ]
                    },
                    {
                    'title': 'Bol??i',
                    'fields': [
                        ("bolta_peste_pronaos", "Bolt?? peste pronaos (Tip)"),
                        ("bolta_peste_pronaos_structura", "Bolt?? peste pronaos (Structura)"),
                        ("bolta_peste_pronaos_tipul_de_arc", "Bolt?? peste pronaos (Tipul de arc)"),
                        ("bolta_peste_pronaos_observatii", "Bolt?? peste pronaos (Observa??ii)"),
                        ("bolta_peste_naos", "Bolt?? peste naos (Tip)"),
                        ("bolta_peste_naos_structura", "Bolt?? peste naos (Structura)"),
                        ("bolta_peste_naos_tipul_de_arc", "Bolt?? peste naos (Tipul de arc)"),
                        ("bolta_peste_naos_observatii", "Bolt?? peste naos (Observa??ii)"),
                        ("bolta_peste_altar", "Bolt?? peste altar"),
                        ("bolta_peste_altar_tip", "Bolt?? peste altar (Tip)"),
                        ("bolta_peste_altar_material", "Bolt?? peste altar (Material)"),
                        ("bolta_peste_altar_structura", "Bolt?? peste altar(Structur??)"),
                        ("bolta_peste_altar_tipul_de_arc", "Bolt?? peste altar (Tipul de arc)"),
                        ("bolta_peste_altar_observatii", "Bolt?? peste altar (Observa??ii"),
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
                    'title': '??arpant?? corp',
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
                    'title': 'Funda??ia',
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
                        ("sistem_structural_observatii", ""),
                        ]
                    },
                    {
                    'title': 'Sistem structural al corpului bisericii ??n cheotoare',
                    'fields': [
                        ("sistem_in_cheotoare", ""),
                        ("sistem_in_cheotoare_observatii", ""),
                        ("poze_structura_cheotoare", "Poze"),
                        ]
                    },
                    {
                    'title': 'Sistem structural al corpului bisericii ??n c????ei',
                    'fields': [
                        ("sistem_in_catei", ""),
                        ("sistem_in_catei_observatii", ""),
                        ("poze_structura_catei", "Poze"),
                        ]
                    },
                    {
                    'title': 'Sistem structural al corpului bisericii mixt',
                    'fields': [
                        ("sistem_mixt", ""),
                        ("poze_structura_mixt", "Poze"),
                        ]
                    },
                    {
                    'title': 'Tiran??i',
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
                    'title': 'Exterior corp biseric??',
                    'fields': [
                        ("finisaj_exterior_tip", "Tip"),
                        ("finisaj_exterior_observatii", ""),
                        ("poze_exterior_corp", "Poze"),
                        ]
                    },
                    {
                    'title': '??nvelitoare corp biseric??',
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
                    'title': '??nvelitoare turn',
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
                    'title': '??nchidere tambur turn',
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
                    'title': '??nvelitoare turle',
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
                        ("finisaje_portic", "Finisaje"),
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
                'title': 'Interven??ii',
                'subsections': [
                    {
                    'title': '??nvelitoare actual?? de lemn',
                    'fields': [
                        ("invelitoare_actuala_an", ""),
                        ("invelitoare_actuala_observatii", ""),
                        ]
                    },
                    {
                    'title': 'Etape anterioare vizibile ale ??nvelitorii',
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
    type = serializers.SerializerMethodField()

    class Meta:
        model = models.IstoricPage
        fields = ['title', 'sections', 'type']

    def get_type(self, obj):
        return 'sections'

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
                    'title': 'Obiecte de cult ??nstr??inate',
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
            'title': 'Peretele desp??r??itor pronaos-naos',
            'fields': [
                ("iconostas_pronaos_naos_tip", ""),
                ("iconostas_pronaos_naos_materiale", ""),
                ("iconostas_pronaos_naos_numar_intrari", ""),
                ("iconostas_pronaos_naos_tehnica", "Tehnic??"),
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
            'title': 'Pictur?? exterioar??',
            'fields': [
                    ("pictura_exterioara_localizare", ""),
                    ("pictura_exterioara_localizare_observatii", ""),
                    ("pictura_exterioara_tehnica", ""),
                    ("pictura_exterioara_suport", "Suport"),
                    ("pictura_exterioara_numar_straturi_pictura", ""),
                    ("poze_pictura_exterioara", "Poze"),
                    ("pictura_exterioara_sursa_datare", "Surs?? datare"),
                    ("pictura_exterioara_anul_picturii", ""),
                    ("pictura_exterioara_datare_prin_interval_timp", ""),
                    ("pictura_exterioara_datare_secol", ""),
                    ("pictura_exterioara_datare_observatii", "")
                ]
            },
            {
            'title': 'Pictur?? interioar??',
            'fields': [
                    ("pictura_interioara_localizare", ""),
                    ("pictura_interioara_localizare_observatii", ""),
                    ("pictura_interioara_tehnica_pictura", ""),
                    ("pictura_interioara_suport", "Suport"),
                    ("pictura_interioara_numar_straturi_pictura", ""),
                    ("poze_pictura_interioara", "Poze"),
                    ("pictura_interioara_sursa_datare", "Surs?? datare"),
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
    type = serializers.SerializerMethodField()

    class Meta:
        model = models.IstoricPage
        fields = ['title', 'sections', 'type']

    def get_type(self, obj):
        return 'sections'

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
                    'title': 'Vegeta??ie',
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
                    'title': 'Funda??ii',
                    'fields': [
                        ("fundatii", ""),
                        ("fundatii_pericol", ""),
                        ("fundatii_observatii", ""),
                        ("poze_fundatii", "Poze"),
                        ]
                },
                {
                    'title': 'T??lpi',
                    'fields': [
                        ("talpi", ""),
                        ("talpi_pericol", ""),
                        ("talpi_observatii", ""),
                        ("poze_talpi", "Poze"),
                        ]
                },
                {
                    'title': 'Corp biseric??',
                    'fields': [
                        ("corp_biserica", ""),
                        ("corp_biserica_pericol", ""),
                        ("corp_biserica_observatii", ""),
                        ("poze_corp_biserica", "Poze"),
                        ]
                },
                {
                    'title': 'Bol??i',
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
                    'title': '??arpant?? corp biseric??',
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
                    'title': 'Finisaj pere??i exteriori',
                    'fields': [
                        ("finisaj_exterior", ""),
                        ("finisaj_exterior_pericol", ""),
                        ("finisaj_exterior_observatii", ""),
                        ("poze_finisaj_exterior", "Poze"),
                        ]
                },
                {
                    'title': 'Finisaj pere??i interiori',
                    'fields': [
                        ("finisaj_pereti_interiori", ""),
                        ("finisaj_pereti_interiori_pericol", ""),
                        ("finisaj_pereti_interiori_observatii", ""),
                        ("poze_finisaj_pereti_interiori", "Poze"),
                        ]
                },
                {
                    'title': 'Finisaj tavane ??i bol??i',
                    'fields': [
                        ("finisaj_tavane_si_bolti", ""),
                        ("finisaj_tavane_si_bolti_pericol", ""),
                        ("finisaj_tavane_si_bolti_observatii", ""),
                        ("poze_finisaj_tavane_si_bolti", "Poze"),
                        ]
                },
                {
                    'title': 'T??mpl??rii',
                    'fields': [
                        ("tamplarii", ""),
                        ("tamplarii_pericol", ""),
                        ("tamplarii_observatii", ""),
                        ("poze_tamplarii", "Poze"),
                        ]
                },
                {
                    'title': '??nvelitoare ??arpant?? ??i turn',
                    'fields': [
                        ("invelitoare_sarpanta_si_turn", ""),
                        ("invelitoare_sarpanta_si_turn_pericol", ""),
                        ("invelitoare_sarpanta_si_turn_observatii", ""),
                        ("poze_invelitoare_sarpanta_si_turn", "Poze"),
                        ]
                },
                {
                    'title': 'Instala??ie electric??',
                    'fields': [
                        ("instalatie_electrica", ""),
                        ("instalatie_electrica_pericol", ""),
                        ("instalatie_electrica_observatii", ""),
                        ("poze_instalatie_electrica", "Poze"),
                        ]
                },
                {
                    'title': 'Instala??ie termic??',
                    'fields': [
                        ("instalatie_termica", ""),
                        ("instalatie_termica_pericol", ""),
                        ("instalatie_termica_observatii", ""),
                        ("poze_instalatie_termica", "Poze"),
                        ]
                },
                {
                    'title': 'Paratr??znet',
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
            'title': 'Componenta Artistic??',
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
    type = serializers.SerializerMethodField()

    class Meta:
        model = models.IstoricPage
        fields = ['title', 'sections', 'type']

    def get_type(self, obj):
        return 'sections'

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
                'title': 'Valoare memorial??',
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
                'title': 'Valoarea estetic??',
                'fields': [
                    ("estetica", ""),
                    ("estetica_observatii", ""),
                ]
                },{
                'title': 'Valoarea me??te??ugului',
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
                'title': 'Folosin??a actual??',
                'fields': [
                    ("folosinta_actuala", ""),
                    ("folosinta_actuala_observatii", ""),
                ]
                },{
                'title': 'Relevan??a actual?? pentru comunitate',
                'fields': [
                    ("relevanta_actuala", ""),
                    ("relevanta_actuala_observatii", ""),
                ]
                },{
                'title': 'Poten??ial',
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
    nori_de_puncte_page = serializers.SerializerMethodField()
    fotogrametrie_page = serializers.SerializerMethodField()

    judet = serializers.SerializerMethodField()
    localitate = serializers.SerializerMethodField()
    adresa = serializers.SerializerMethodField()
    latitudine = serializers.SerializerMethodField()
    longitudine = serializers.SerializerMethodField()
    conservare = serializers.SerializerMethodField()
    valoare = serializers.SerializerMethodField()
    datare_prin_interval_timp = serializers.SerializerMethodField()
    datare_secol = serializers.SerializerMethodField()

    class Meta:
        model = models.BisericaPage
        fields = ["id", "title", "cod", "judet", "localitate", "adresa", "latitudine",
                  "longitudine", "datare_prin_interval_timp", "datare_secol",
                   "conservare", "valoare", "identificare_page", "istoric_page", "descriere_page",
                   "componenta_artistica_page","conservare_page", "valoare_page",
                   "nori_de_puncte_page", "fotogrametrie_page"]

    def get_nori_de_puncte_page(self, obj):
        return {
            'title': '3D - Nori de puncte',
            'type': 'embed',
            'embed': obj.descriere_page.model_nori_de_puncte
        }

    def get_fotogrametrie_page(self, obj):
        return {
            'title': '3D - Fotogrametrie',
            'type': 'embed',
            'embed': obj.descriere_page.model_fotogrametrie
        }


    def get_localitate(self, obj):
        return str(obj.identificare_page.localitate)

    def get_judet(self, obj):
        return str(obj.identificare_page.judet)

    def get_adresa(self, obj):
        return obj.identificare_page.adresa

    def get_latitudine(self, obj):
        return obj.identificare_page.latitudine

    def get_longitudine(self, obj):
        return obj.identificare_page.longitudine

    def get_conservare(self, obj):
        return obj.conservare_page.total

    def get_valoare(self, obj):
        return obj.valoare_page.total

    def get_prioritizare(self, obj):
        if obj.valoare_page.total and obj.conservare_page.total:
            return obj.valoare_page.total * obj.conservare_page.total
        return None

    def get_datare_prin_interval_timp(self, obj):
        return obj.istoric_page.datare_prin_interval_timp

    def get_datare_secol(self, obj):
        if obj.istoric_page.datare_secol:
            return obj.istoric_page.datare_secol.nume
        return None


class BisericaListSerializer(serializers.ModelSerializer):
    poze = PozaSerializer(many=True)

    judet = serializers.SerializerMethodField()
    localitate = serializers.SerializerMethodField()
    adresa = serializers.SerializerMethodField()
    latitudine = serializers.SerializerMethodField()
    longitudine = serializers.SerializerMethodField()
    datare = serializers.SerializerMethodField()
    conservare = serializers.SerializerMethodField()
    valoare = serializers.SerializerMethodField()
    prioritizare = serializers.SerializerMethodField()

    class Meta:
        model = models.BisericaPage
        fields = ["id", "title", "cod", "judet", "localitate", "adresa", "latitudine",
                  "longitudine", "datare", "conservare",
                  "valoare", "prioritizare", "poze"]

    def get_localitate(self, obj):
        return str(obj.identificare_page.localitate)

    def get_judet(self, obj):
        return str(obj.identificare_page.judet)

    def get_adresa(self, obj):
        return obj.identificare_page.adresa

    def get_latitudine(self, obj):
        return obj.identificare_page.latitudine

    def get_longitudine(self, obj):
        return obj.identificare_page.longitudine

    def get_conservare(self, obj):
        return obj.conservare_page.total

    def get_valoare(self, obj):
        return obj.valoare_page.total

    def get_prioritizare(self, obj):
        if obj.valoare_page.total and obj.conservare_page.total:
            return obj.valoare_page.total * obj.conservare_page.total
        return None

    def get_datare(self, obj):
        if obj.istoric_page.an_constructie:
            return f'Anul {obj.istoric_page.an_constructie}' 
        if obj.istoric_page.datare_prin_interval_timp:
            return obj.istoric_page.datare_prin_interval_timp
        if obj.istoric_page.datare_secol:
            return f'Secolul {obj.istoric_page.datare_secol}'


class PartnerSerializer(serializers.ModelSerializer):
    logo = ImageRenditionField('width-400')

    class Meta:
        model = models.ParteneriProiect
        fields = ["logo", "link"]


class AboutSerializer(serializers.ModelSerializer):
    parteneri = PartnerSerializer(many=True)
    body = serializers.SerializerMethodField()

    class Meta:
        model = models.AboutPage
        fields = ["title", "body", "parteneri"]


    def get_body(self, obj):

        return [str(section) for section in obj.body]

