from app import models
from pprint import pprint


map_capitole = {
    'identificare': models.IdentificarePage,
    'istoric': models.IstoricPage,
    'descriere': models.DescrierePage,
    'componenta_artistica': models.ComponentaArtisticaPage,
    'conservare': models.ConservarePage,
    'valoare': models.ValoarePage,
}


map_field_verbose_name = {
    'Sit': {
        "sit": "Sit",
        "elemente_arhitecturale": "Elemente arhitecturale",
        "alte_elemente_importante": "Alte elemente importante",
        "vegetatie": "Vegetație",
        "vegetatie_pericol": "Pericol vegetație",
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
        "relevanta_actuala": "Relevanță actuală",
        "potential": "Potențial",

    }
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

    filters_values = model.objects.live().values(*filters_name)
    for item in filters_values:
        for field_name, field_value in item.items():
            section = filters_mapping[field_name]
            filters.setdefault(section, {})
            filters[section].setdefault(field_name, [])

            if field_value is not None and field_value not in filters[section][field_name]:
                filters[section][field_name].append(field_value)


    for section, section_filters in filters.items():
        filters_list = []
        for field in section_filters:
            if section_filters[field]:
                field_verbose = map_field_verbose_name.get(section, {}).get(field, None)
                if model._meta.get_field(field).remote_field:
                    field_model = model._meta.get_field(field).remote_field.model
                    filters_list.append({
                        "title": field_verbose if field_verbose else model._meta.get_field(field).verbose_name.title(),
                        "key": field,
                        "values": field_model.objects.filter(id__in=section_filters[field]).values('id', 'nume')
                    })
                else:
                    if model._meta.get_field(field).choices:
                        choices =  {x[0]: x[1] for x in model._meta.get_field(field).choices}
                        filters_list.append({
                            "title": field_verbose if field_verbose else model._meta.get_field(field).verbose_name.title(),
                            "key": field,
                            "values": [choices[x] for x in section_filters[field]]
                        })
                    else:
                        filters_list.append({
                            "title": field_verbose if field_verbose else  model._meta.get_field(field).verbose_name.title(),
                            "key": field,
                            "values": section_filters[field]
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
    biserici_paths = []
    i = 0
    for item in data:
        for nume_capitol, capitol_filters in item.items():
            filters = {}
            for indicator in capitol_filters:
                filters[f"{indicator['key']}__in"] = indicator['values']
            capitole_pages = map_capitole[nume_capitol].objects.filter(**filters).values_list('path', flat=True)
            if i < 1:
                biserici_paths = set([x[:12] for x in capitole_pages])
            else:
                biserici_paths = biserici_paths.intersection(set([x[:12] for x in capitole_pages]))
            i += 1
    biserici = models.BisericaPage.objects.filter(path__in=biserici_paths)
    return biserici