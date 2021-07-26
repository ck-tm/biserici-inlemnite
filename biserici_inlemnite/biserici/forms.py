from django import forms
from biserici import models


class IdentificareForm(forms.ModelForm):
    class Meta:
        model = models.Identificare
        exclude = ('biserica', 'last_edit_user', 'last_edit_date')

class DescriereForm(forms.ModelForm):
    class Meta:
        model = models.Descriere
        exclude = ('biserica', 'last_edit_user', 'last_edit_date')

class IstoricForm(forms.ModelForm):
    class Meta:
        model = models.Istoric
        exclude = ('biserica', 'last_edit_user', 'last_edit_date')

class PatrimoniuForm(forms.ModelForm):
    class Meta:
        model = models.Patrimoniu
        exclude = ('biserica', 'last_edit_user', 'last_edit_date')

class ConservareForm(forms.ModelForm):
    class Meta:
        model = models.Conservare
        exclude = ('biserica', 'last_edit_user', 'last_edit_date')