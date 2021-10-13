from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt
# from django.contrib import admin
from baton.autodiscover import admin
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView
from rest_framework.authtoken.views import obtain_auth_token
from biserici import views
from app import views as app_views


from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from .api_router import wagtail_api


urlpatterns = [
    # path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path("", view=views.BisericiView.as_view(), name="home"),
    path('cms/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
    path('pages/<int:parent_page_id>/', app_views.wagtail_pages, name='wagtailadmin_explore'),
    path('pages/', include(wagtail_urls)),

    path("biserici/", view=views.BisericiView.as_view(), name="biserici"),
    path('biserici/<int:pk>/', view=views.BisericaView.as_view(), name='biserica'),
    path('biserici/<int:biserica_pk>/identificare', view=views.IdentificareBisericaView.as_view(), name='identificare'),
    path('biserici/<int:biserica_pk>/descriere', view=views.DescriereBisericaView.as_view(), name='descriere'),
    path('biserici/<int:biserica_pk>/istoric', view=views.IstoricBisericaView.as_view(), name='istoric'),
    path('biserici/<int:biserica_pk>/patrimoniu', view=views.PatrimoniuBisericaView.as_view(), name='patrimoniu'),
    path('biserici/<int:biserica_pk>/conservare', view=views.ConservareBisericaView.as_view(), name='conservare'),
    path("biserici/add-constant/<str:model_name>", view=views.ContentCreateView.as_view(), name="constant-create"),
    path(
        "about/", TemplateView.as_view(template_name="pages/about.html"), name="about"
    ),
    # Django Admin, use {% url 'admin:index' %}
    # url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    # url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    # path(settings.ADMIN_URL, admin.site.urls),
    path('admin/', admin.site.urls),
    # User management
    path("users/", include("biserici_inlemnite.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
    # Your stuff: custom urls includes go here
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# API URLS
urlpatterns += [
    # API base url
    path('api/rest-auth/', include('dj_rest_auth.urls')),
    path("api/", include("config.api_router")),
    path('wagtail/api/', wagtail_api.urls),
    # DRF auth token
    path("auth-token/", obtain_auth_token),

]

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
