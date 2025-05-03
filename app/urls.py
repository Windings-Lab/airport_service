from django.urls import include, path

urlpatterns = [
    path("account/", include("account.urls", namespace="account")),
    path("airport/", include("airport.urls", namespace="airport")),
]
