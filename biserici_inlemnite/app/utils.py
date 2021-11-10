from django.db.models import F
from app import models
from pprint import pprint


MAP_CAPITOLE = {
    'identificare': models.IdentificarePage,
    'istoric': models.IstoricPage,
    'descriere': models.DescrierePage,
    'componenta_artistica': models.ComponentaArtisticaPage,
    'conservare': models.ConservarePage,
    'valoare': models.ValoarePage,
}


MAP_FIELD_VERBOSE_NAME = {
    'Localizare/Peisaj': {
        'relatia_cu_cimitirul': 'Relația cu cimitirul'
    },
    'Tip scanare': {
        'are_scanare_laser': 'Model 3d - nor de puncte',
        'are_model_fotogrametric': 'Model 3d - fotogrametrie'
    },
    'Sit': {
        "sit": "Sit",
        "sit_pericol": "Pericol sit",
        "elemente_arhitecturale": "Elemente arhitecturale",
        "elemente_arhitecturale_pericol": "Pericol elemente arhitecturale",
        "alte_elemente_importante": "Alte elemente importante",
        "alte_elemente_importante_pericol": "Pericol alte elemente importante",
        "vegetatie": "Vegetație",
        "vegetatie_pericol": "Pericol vegetație",
    },
    'Arhitectura bisericii': {
        'numar_ochiesi': 'Număr ochieși',
        'numar_clopote': 'Număr clopote',
        'sarpanta_tip': "Șarpantă corp",
        "turn_tip": "Turn",
        "sistem_in_cheotoare": "Sistem structural al corpului bisericii în cheotoare",
        "sistem_in_catei": "Sistem structural al corpului bisericii în căței",
        "bolta_peste_altar_tip": "Tip boltă altar",
        # "invelitoare_corp_sindrila_numar_straturi": "Număr straturi șindrilă peste corp biserică",
        # "invelitoare_corp_sindrlia_tipul_de_batere": "Tip batere șindrilă peste corp biserică",
        # "invelitoare_corp_sindrlia_forma_botului": "Forma botului șindrilă peste corp biserică",

        "invelitoare_corp_material": "Învelitoare corp",
        "invelitoare_corp_sindrila_numar_straturi": "Șindrilă peste corp (număr straturi)",
        "invelitoare_corp_sindrila_cu_horj": "Șindrilă peste corp (cu horj)",
        "invelitoare_corp_sindrlia_tipul_de_batere": "Șindrilă peste corp (tipul de batere)",
        "invelitoare_corp_sindrlia_forma_botului": "Șindrilă peste corp (forma botului)",
        "invelitoare_corp_sindrila_cu_tesitura": "Șindrilă peste corp (cu teșitură)",
        "invelitoare_corp_sindrlia_prelucrare": "Șindrilă peste corp (prelucrare)",
        "invelitoare_corp_sindrlia_esenta_lemnoasa": "Șindrilă peste corp (esență lemnoasă)",
        "invelitoare_turn_material": "Învelitoare turn",
        "invelitoare_turn_sindrila_numar_straturi": "Șindrilă peste turn (număr straturi)",
        "invelitoare_turn_sindrila_cu_horj": "Șindrilă peste turn (cu horj)",
        
        "invelitoare_turn_sindrlia_tipul_de_batere": "Șindrilă peste turn (tipul de batere)",
        "invelitoare_turn_sindrlia_forma_botului": "Șindrilă peste turn (forma botului)",
        "invelitoare_turn_sindrila_cu_tesitura": "Șindrilă peste turn (cu teșitură)",
        "invelitoare_turn_sindrlia_prelucrare": "Șindrilă peste turn (prelucrare)",
        "invelitoare_turn_sindrlia_esenta_lemnoasa": "Șindrilă peste turn (esență lemnoasă)",

        "inchidere_tambur_turn_material": "închidere tambur turn",
        "inchidere_tambur_turn_sindrila_numar_straturi": "Șindrilă închidere turn (număr straturi)",
        "inchidere_tambur_turn_sindrlia_tipul_de_batere": "Șindrilă închidere turn (tipul de batere)",
        "inchidere_tambur_turn_sindrlia_forma_botului": "Șindrilă închidere turn (forma botului)",
        "inchidere_tambur_turn_sindrila_cu_tesitura": "Șindrilă închidere turn (cu teșitură)",
        "inchidere_tambur_turn_sindrlia_prelucrare": "Șindrilă închidere turn (prelucrare)",
        "inchidere_tambur_turn_sindrlia_esenta_lemnoasa": "Șindrilă închidere turn (esență lemnoasă)",
    },
    'Strucutra bisericii': {
        "teren": "Teren",
        "teren_pericol": "Pericol teren",
        "fundatii": "Fundații",
        "fundatii_pericol": "Pericol fundații",
        "talpi": "Tălpi",
        "talpi_pericol": "Pericol tălpi",
        "corp_biserica": "Corp biserica",
        "corp_biserica_pericol": "Pericol corp biserică",
        "bolti": "Bolți",
        "bolti_pericol": "Pericol bolți",
        "cosoroabe": "Cosoroabe",
        "cosoroabe_pericol": "Pericol cosoroabe",
        "sarpanta_peste_corp_biserica": "Șarpantă peste corp biserică",
        "sarpanta_peste_corp_biserica_pericol": "Pericol șarpantă peste corp biserică",
        "turn": "Turn",
        "turn_pericol": "Pericol turn",
    },
    'Finisaje biserică': {
        "zona_din_jurul_biserici": "Zona din jurul biserici",
        "zona_din_jurul_biserici_pericol": "Pericol zona din jurul biserici",
        "pardoseli_interioare": "Pardoseli interioare",
        "pardoseli_interioare_pericol": "Pericol pardoseli interioare",
        "finisaj_exterior": "Finisaj exterior",
        "finisaj_exterior_pericol": "Pericol finisaj exterior",
        "finisaj_pereti_interiori": "Finisaj pereți interiori",
        "finisaj_pereti_interiori_pericol": "Pericol finisaj pereți interiori",
        "finisaj_tavane_si_bolti": "Finisaj tavane și bolți",
        "finisaj_tavane_si_bolti_pericol": "Pericol finisaj tavane și bolți",
        "tamplarii": "Tâmplării",
        "tamplarii_pericol": "Pericol tâmplării",
        "invelitoare_sarpanta_si_turn": "Învelitoare șarpanta și turn",
        "invelitoare_sarpanta_si_turn_pericol": "Pericol învelitoare șarpanta și turn",
        "instalatie_electrica": "Instalație electrică",
        "instalatie_electrica_pericol": "Pericol instalație electrică",
        "instalatie_termica": "Instalație termică",
        "instalatie_termica_pericol": "Pericol instalație termică",
        "paratraznet": "Paratrăznet",
        "paratraznet_pericol": "Pericol paratrăznet",
    },
    'Componenta Artistică': {
        "strat_pictural": "Strat pictural",
        "strat_pictural_pericol": "Pericol strat pictural",
        "obiecte_de_cult": "Obiecte de cult",
        "obiecte_de_cult_pericol": "Pericol obiecte de cult",
        "mobilier": "Mobilier",
        "mobilier_pericol": "Pericol mobilier",
    },
    '': {
        'an_constructie': 'An construcție',
        "vechime": "Vechime",
        "integritate": "Integritate",
        "unicitate": "Unicitate",
        "valoare_memoriala": "Valoare memorială",
        "peisaj_cultural": "Peisaj cultural",
        "valoare_sit": "Valoare sit",
        "estetica": "Estetică",
        "mestesug": "Meșteșug",
        "pictura": "Pictură",
        "folosinta_actuala": "Folosință actuală",
        "relevanta_actuala": "Relevanță actuală pentru comunitate",
        "potential": "Potențial",
        "functiune": "Funcțiune",
        "functiune_initiala": "Funcțiune inițială",
        "pictura": "Componentă artistică",

    }
}

MAP_CLASE_PRIORITIZARE = {
    1: (1, 5),
    2: (5, 10),
    3: (10, 15),
}


def get_chapter_filters(model, filters_dict):
    filters = {}
    sections_list = []
    filters_name = []
    filters_mapping = {}
    for section, section_filters in filters_dict.items():

        filters_name += section_filters
        for filter_name in section_filters:
            filters_mapping[filter_name] = section

    # prefetch_list = []
    # for field in model._meta.fields:
    #     if field.get_internal_type() == 'ForeignKey':
    #         prefetch_list.append(field.name)
    # print(prefetch_list)
    # print('------')
    # filters_values = model.objects.prefetch_related(*prefetch_list).live().values(*filters_name)
    filters_values = model.objects.live().values(*filters_name)

    for item in filters_values:
        for field_name, field_value in item.items():
            section = filters_mapping[field_name]
            filters.setdefault(section, {})
            filters[section].setdefault(field_name, [])

            if type(field_value) == list:
                for field in field_value:
                    if field is not None and field not in filters[section][field_name]:
                        filters[section][field_name].append(field)
            else:
                if field_value is not None and field_value not in filters[section][field_name]:
                    filters[section][field_name].append(field_value)


    for section, section_filters in filters.items():
        filters_list = []
        for field in section_filters:
            if section_filters[field]:
                field_verbose = MAP_FIELD_VERBOSE_NAME.get(section, {}).get(field, None)
                if model._meta.get_field(field).remote_field:
                    field_model = model._meta.get_field(field).remote_field.model
                    if field == 'planimetria_bisericii':
                        planimetrii = []
                        for image in field_model.objects.filter(id__in=section_filters[field]):
                            try:
                                planimetrie = image.get_rendition('width-200')
                                rendition = {
                                    "url": planimetrie.url,
                                    "width": planimetrie.width,
                                    "height": planimetrie.height,
                                    "alt": planimetrie.alt
                                }
                                planimetrii.append(rendition)
                            except:
                                pass
                        filters_list.append({
                            "title": field_verbose if field_verbose else model._meta.get_field(field).verbose_name.capitalize(),
                            "type": 'poza',
                            "key": field,
                            "values": planimetrii
                        })
                    else:
                        # Nomenclatoare
                        filters_list.append({
                            "title": field_verbose if field_verbose else model._meta.get_field(field).verbose_name.capitalize(),
                            "type": 'checkbox',
                            "key": field,
                            "values": field_model.objects.filter(id__in=section_filters[field]).values('id', 'nume')
                        })
                else:
                    if model._meta.get_field(field).choices:
                        # Has choices
                        choices =  {x[0]: x[1] for x in model._meta.get_field(field).choices}
                        filters_list.append({
                            "title": field_verbose if field_verbose else model._meta.get_field(field).verbose_name.capitalize(),
                            "type": 'checkbox',
                            "key": field,
                            "values": [{'id': x, 'nume': choices[x]} for x in section_filters[field]]
                        })
                    else:
                        values = []
                        if type(section_filters[field][0]) == list:
                            # ManytoMany
                            for x in section_filters[field][0]:
                                value = {'id': x, 'nume': x}
                                if value not in values:
                                    values.append(value)
                        else:
                            # Regular field
                            for x in section_filters[field]:
                                value = {'id': x, 'nume': x}
                                if value not in values:
                                    values.append(value)
                            # values = [{'id': x, 'nume': x} for x in section_filters[field]]
                        filters_list.append({
                            "title": field_verbose if field_verbose else  model._meta.get_field(field).verbose_name.capitalize(),
                            "type": 'checkbox',
                            "key": field,
                            "values": values
                        })
            # else:
                # del section_filters[field]
        if len(filters_list):
            sections_list.append({
                'title': section,
                'filters': filters_list
                })
    return sections_list


def filter_biserici(data):
    filters = {}

    for nume_capitol, capitol_filters in data.get('advanced', {}).items():
        for indicator, indicator_values in capitol_filters.items():
            if MAP_CAPITOLE[nume_capitol]._meta.get_field(indicator).get_internal_type() == 'ArrayField':
                filters[f"{nume_capitol}_page__{indicator}__contains"] = indicator_values
            else:
                filters[f"{nume_capitol}_page__{indicator}__in"] = indicator_values

    for indicator, indicator_values in data['basic'].items():
        if indicator == 'conservare':

            filters["conservare_page__total__range"] = (indicator_values[0]-0.5, indicator_values[0]+0.5)
        elif indicator == 'valoare':
            filters["valoare_page__total__range"] = (indicator_values[0]-0.5, indicator_values[0]+0.5)

        elif indicator == 'prioritizare':
            prioritizare_biserici = models.BisericaPage.objects.annotate(
                p=F('conservare_page__total') * F('valoare_page__total')).filter(
                **{'p__range':MAP_CLASE_PRIORITIZARE[indicator_values[0]]}).values_list('pk', flat=True)
            filters["pk__in"] = prioritizare_biserici
        elif indicator == 'judet':
            filters["identificare_page__judet__in"] = indicator_values
        else:
            filters["identificare_page__localitate__in"] = indicator_values

    if filters:
        biserici = models.BisericaPage.objects.live().filter(**filters)
    else:
        biserici = models.BisericaPage.objects.live()
    return biserici