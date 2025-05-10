from django.urls import include, path


app_name = "airport"
urlpatterns = [path("api/", include("airport.api.urls", namespace="api_airport"))]
