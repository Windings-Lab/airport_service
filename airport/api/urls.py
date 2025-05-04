from rest_framework import routers

import airport.api.views as views

app_name = "api_airport"
router = routers.DefaultRouter()

router.register("flight", views.Flight)
router.register("crew", views.Crew)
router.register("airplane", views.Airplane)
router.register("airplane-type", views.AirplaneType)
router.register("order", views.Order)
router.register("ticket", views.Ticket)
router.register("airport", views.Airport)
router.register("route", views.Route)

urlpatterns = router.urls
