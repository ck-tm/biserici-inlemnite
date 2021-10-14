from app import models
from pprint import pprint


def get_chapter_filters(model, filters_dict):
    filters = {}
    sections_list = []
    filters_name = []
    filters_mapping = {}
    for section_dict in filters_dict:
        for section, section_filters in section_dict.items():

            filters_name += section_dict[section]
            for filter_name in section_dict[section]:
                filters_mapping[filter_name] = section

    filters_values = model.objects.live().values(*filters_name)
    for item in filters_values:
        for field_name, field_value in item.items():
            section = filters_mapping[field_name]
            filters.setdefault(section, {})
            filters[section].setdefault(field_name, [])
            if field_value and field_value not in filters[section][field_name]:
                filters[section][field_name].append(field_value)


    for section, section_filters in filters.items():
        filters_list = []
        for field in section_filters:
            if section_filters[field]:
                if model._meta.get_field(field).remote_field:
                    field_model = model._meta.get_field(field).remote_field.model
                    filters_list.append({
                        "title": model._meta.get_field(field).verbose_name.title(),
                        "key": field,
                        "values": field_model.objects.filter(id__in=section_filters[field]).values('id', 'nume')
                    })
                else:
                    if model._meta.get_field(field).choices:
                        choices =  {x[0]: x[1] for x in model._meta.get_field(field).choices}
                        filters_list.append({
                            "title": field.replace('_', ' ').title(),
                            "key": field,
                            "values": [choices[x] for x in section_filters[field]]
                        })
                    else:
                        filters_list.append({
                            "title": field.replace('_', ' ').title(),
                            "key": field,
                            "values": section_filters[field]
                        })
            # else:
                # del section_filters[field]
        sections_list.append({
            'title': section,
            'filters': filters_list
            })
    return sections_list


map_capitole = {
    'identificare': models.IdentificarePage,
    'istoric': models.IstoricPage,
    'descriere': models.DescrierePage,
    'componenta_artistica': models.ComponentaArtisticaPage,
    'conservare': models.ConservarePage,
    'valoare': models.ValoarePage,
}

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