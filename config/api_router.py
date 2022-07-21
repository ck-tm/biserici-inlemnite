from django.conf import settings
from django.apps import apps
from rest_framework.routers import DefaultRouter, SimpleRouter


from wagtail.api.v2.views import PagesAPIViewSet
from wagtail.api.v2.router import WagtailAPIRouter
from wagtail.images.api.v2.views import ImagesAPIViewSet
from wagtail.documents.api.v2.views import DocumentsAPIViewSet

from app.api import views
from biserici.api import views as biserici_views


app_name = "api"

# Create the router. "wagtailapi" is the URL namespace
wagtail_api = WagtailAPIRouter("wagtailapi")

# Add the three endpoints using the "register_endpoint" method.
# The first parameter is the name of the endpoint (eg. pages, images). This
# is used in the URL of the endpoint
# The second parameter is the endpoint class that handles the requests
wagtail_api.register_endpoint("pages", PagesAPIViewSet)
wagtail_api.register_endpoint("images", ImagesAPIViewSet)
wagtail_api.register_endpoint("documents", DocumentsAPIViewSet)


if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()


# NEW
router.register("map", views.MapViewSet, basename="biserica")
router.register("about", views.AboutViewSet, basename="about")
router.register("filters", views.FiltersView, basename="filters")
router.register("biserici", biserici_views.BisericiViewSet, basename="biserici")


urlpatterns = router.urls
