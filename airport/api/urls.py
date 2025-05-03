from rest_framework import routers

import airport.api.views as views

app_name = "api_airport"
router = routers.DefaultRouter()

router.register("flight", views.Flight)

urlpatterns = router.urls
