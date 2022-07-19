from wq.db import rest
from django.apps import apps
from fragmente.api import views as fragmente_views


app = apps.get_app_config('fragmente')

for model_name, model in app.models.items():
    if not 'historical' in model_name:
        rest.router.register_model(
            model,
            fields="__all__",
            viewset=fragmente_views.GenericAPIView,
            url=model_name
        )

rest.router.register(
    prefix='all',
    viewset=fragmente_views.FragmenteView,
    basename="all"
)
