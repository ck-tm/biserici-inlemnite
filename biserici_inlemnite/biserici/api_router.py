from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from biserici.api import views

app_name = "api_admin"




if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()


router.register("biserici", views.BisericaViewSet, basename='biserici')

urlpatterns = router.urls
