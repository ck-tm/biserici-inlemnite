from django import forms
from crispy_forms.helper import FormHelper

from biserici import models

class ReadOnlyForm(object):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['readonly'] = True
            self.fields[field].widget.attrs['disabled'] = True

class IdentificareForm(ReadOnlyForm, forms.ModelForm):
    class Meta:
        model = models.Identificare
        exclude = ('biserica',)

class DescriereForm(ReadOnlyForm, forms.ModelForm):
    class Meta:
        model = models.Descriere
        exclude = ('biserica',)

# class IstoricForm(ReadOnlyForm, forms.ModelForm):
#     class Meta:
#         model = models.Istoric
#         exclude = ('biserica',)
#         # readonly_fields = '__all__'

class PatrimoniuForm(ReadOnlyForm, forms.ModelForm):
    class Meta:
        model = models.Patrimoniu
        exclude = ('biserica',)

class ConservareForm(ReadOnlyForm, forms.ModelForm):
    class Meta:
        model = models.Conservare
        exclude = ('biserica',)