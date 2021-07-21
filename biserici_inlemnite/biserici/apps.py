from django.apps import AppConfig


class BisericiConfig(AppConfig):
    name = 'biserici'

    def ready(self):
        try:
            import biserici_inlemnite.biserici.signals  # noqa F401
        except ImportError as e:
            print('errrrrrr', e)
