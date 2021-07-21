from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from biserici_inlemnite.users.api.views import UserViewSet
from biserici_inlemnite.biserici.api.views import BisericaViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("biserici", BisericaViewSet, basename='biserica')


app_name = "api"
urlpatterns = router.urls
