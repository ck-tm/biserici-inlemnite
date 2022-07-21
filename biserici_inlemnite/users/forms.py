from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django import forms

# from allauth.account.forms import SignupForm

User = get_user_model()


class UserChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User


class UserCreationForm(admin_forms.UserCreationForm):
    class Meta(admin_forms.UserCreationForm.Meta):
        model = User

        error_messages = {"username": {"unique": _("This username has already been taken.")}}


# class AllAuthCustomSignupForm(SignupForm):
#     name = forms.CharField(max_length=100)

#     def save(self, request):
#         user = super().save(request)
#         user.name = self.cleaned_data['name']
#         user.save()
#         return user
