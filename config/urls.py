from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
urlpatterns = [
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    # Your stuff: custom urls includes go here
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# API URLS
urlpatterns += [
    # JWT using rest_framework_simplejwt
    path("users/", include("finman_backend.users.urls", namespace="users")),
    # path("watch_health_data/", include("finman_backend.watchHealthData.urls", namespace='Watch Data')),
    # API base url
    path("", include("config.api_router")),
    # DRF auth token
    path("schema/", SpectacularAPIView.as_view(), name="api-schema"),
    path('authentication/', include('dj_rest_auth.urls')),
    path('authentication/registration/', include('dj_rest_auth.registration.urls')),
    path('accounts/', include('allauth.urls'), name='socialaccount_signup'),

    # path('accounts/', include('allauth.urls')),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="api-schema"),
        name="api-docs",
    ),

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
