from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig


class BisericiConfig(AppConfig):
    name = "biserici"

    def ready(self):
        try:
            import biserici_inlemnite.biserici.signals  # noqa F401
        except ImportError as e:
            print("errrrrrr", e)


# class BisericiAdminConfig(AdminConfig):
#     default_site = 'biserici.admin.MyAdminSite'
