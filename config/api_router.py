from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from biserici_inlemnite.users.api.views import UserViewSet
from biserici_inlemnite.biserici.api.views import BisericaViewSet
from app.api import views

from wagtail.api.v2.views import PagesAPIViewSet
from wagtail.api.v2.router import WagtailAPIRouter
from wagtail.images.api.v2.views import ImagesAPIViewSet
from wagtail.documents.api.v2.views import DocumentsAPIViewSet

# Create the router. "wagtailapi" is the URL namespace
wagtail_api = WagtailAPIRouter('wagtailapi')

# Add the three endpoints using the "register_endpoint" method.
# The first parameter is the name of the endpoint (eg. pages, images). This
# is used in the URL of the endpoint
# The second parameter is the endpoint class that handles the requests
wagtail_api.register_endpoint('pages', PagesAPIViewSet)
wagtail_api.register_endpoint('images', ImagesAPIViewSet)
wagtail_api.register_endpoint('documents', DocumentsAPIViewSet)


if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

# OLD
router.register("users", UserViewSet)
router.register("biserici", BisericaViewSet, basename='biserica')

# NEW
router.register("map", views.BisericaViewSet, basename='biserica-new')


app_name = "api"
urlpatterns = router.urls
