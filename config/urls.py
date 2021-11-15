from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt
# from django.contrib import admin
from baton.autodiscover import admin
from django.urls import include, path, re_path
from django.views import defaults as default_views
from django.views.generic import TemplateView
from rest_framework.authtoken.views import obtain_auth_token
from biserici import views
from app import views as app_views
# from dj_rest_auth.views import PasswordResetConfirmView
from rest_framework.authtoken import views as token_views

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from .api_router import wagtail_api


urlpatterns = [
    # path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path('<int:pk>', app_views.BisericaDetailView.as_view(), name='work-preview'),
    path('profile/<int:pk>', app_views.BisericaDetailView.as_view(), name='work-detail'),
    path('cms/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
    path('cms/pages/<int:parent_page_id>/', app_views.wagtail_pages, name='wagtailadmin_explore'),
    path('cms/pages/', include(wagtail_urls)),

    path('admin/', admin.site.urls),
    # User management
    path("users/", include("biserici_inlemnite.users.urls", namespace="users")),
    # path("accounts/", include("allauth.urls")),
    # Your stuff: custom urls includes go here
    path("", view=app_views.BisericiView.as_view(), name="home"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# API URLS
urlpatterns += [
    # API base url
    # re_path(r'^api/rest-auth/password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', PasswordResetConfirmView.as_view(),
            # name='password_reset_confirm'),
    # path('api/rest-auth/password/reset/confirm/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('api/auth/', include('djoser.urls')),
    path("api/auth/token", token_views.obtain_auth_token),
    # path('api/rest-auth/registration/', include('rest_auth.registration.urls')),
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
