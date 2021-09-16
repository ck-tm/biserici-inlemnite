from django.apps import AppConfig


class AppConfig(AppConfig):
    name = 'app'


    def ready(self):
        try:
            import biserici_inlemnite.app.signals  # noqa F401
        except ImportError as e:
            print('errrrrrr', e)