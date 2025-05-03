from django.urls import path, include

urlpatterns = [
    path(
        "api/auth/", include("rest_framework.urls", namespace="rest_framework")
    )
]
