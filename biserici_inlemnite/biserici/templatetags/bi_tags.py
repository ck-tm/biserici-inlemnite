from django import template, forms
from django.forms.models import ModelChoiceField, ModelMultipleChoiceField

register = template.Library()

@register.filter(name='get_model')
def get_model(field):
    print(field)
    print(field.field.__class__)
    if field.field.__class__ in [ModelChoiceField, ModelMultipleChoiceField]:
        try:
            m = field.field.queryset[0]
            return m.__class__._meta.object_name
        except:
            pass
    return None



 


@register.filter
def is_checkboxselectmultiple(field):
    if field.field.__class__ == ModelMultipleChoiceField:
        print(field, True)
        return True
    return isinstance(field.field.widget, forms.CheckboxSelectMultiple)