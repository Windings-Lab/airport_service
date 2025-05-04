from django.urls import include, path
from django.conf import settings

urlpatterns = [
    path("account/", include("account.urls", namespace="account")),
    path("airport/", include("airport.urls", namespace="airport")),
]

if settings.DEBUG:
    from debug_toolbar.toolbar import debug_toolbar_urls
    urlpatterns += debug_toolbar_urls()