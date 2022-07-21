from django import template, forms
from django.forms.models import ModelChoiceField, ModelMultipleChoiceField

register = template.Library()


@register.filter(name="get_model")
def get_model(field):
    if field.field.__class__ in [ModelChoiceField, ModelMultipleChoiceField]:
        try:
            m = field.field.queryset[0]
            return m.__class__._meta.object_name
        except:
            pass
    return None


@register.filter(name="has_group")
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()


# @register.filter
# def is_checkboxselectmultiple(field):
#     if field.field.__class__ == ModelMultipleChoiceField:
#         return True
#     return isinstance(field.field.widget, forms.CheckboxSelectMultiple)
