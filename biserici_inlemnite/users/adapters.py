from typing import Any

from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.utils import build_absolute_uri
from django.conf import settings
from django.http import HttpRequest


class AccountAdapter(DefaultAccountAdapter):
    def is_open_for_signup(self, request: HttpRequest):
        return getattr(settings, "ACCOUNT_ALLOW_REGISTRATION", True)

    # def send_mail(self, template_prefix, email, context):
    #     context['activate_url'] = settings.URL_FRONT + \
    #         'verify-email/' + context['key']
    #     msg = self.render_mail(template_prefix, email, context)
    #     msg.send()

    def get_email_confirmation_url(self, request, emailconfirmation):
        url = settings.CUSTOM_ACCOUNT_CONFIRM_EMAIL_URL.format(emailconfirmation.key)
        ret = build_absolute_uri(request, url)
        return ret


class SocialAccountAdapter(DefaultSocialAccountAdapter):
    def is_open_for_signup(self, request: HttpRequest, sociallogin: Any):
        return getattr(settings, "ACCOUNT_ALLOW_REGISTRATION", True)
