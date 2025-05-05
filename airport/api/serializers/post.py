from rest_framework.serializers import PrimaryKeyRelatedField

import airport.api.serializers.base as base
import airport.models


class Ticket(base.Ticket):
    flight = PrimaryKeyRelatedField(
        queryset=airport.models.Flight.objects.select_related()
    )


class Order(base.Order):
    tickets = Ticket(many=True)


class Flight(base.Flight):
    route = PrimaryKeyRelatedField(
        queryset=airport.models.Route.objects.select_related()
    )


class Route(base.Route):
    __airport_queryset = list(airport.models.Airport.objects.select_related())
    source = PrimaryKeyRelatedField(queryset=__airport_queryset)
    destination = PrimaryKeyRelatedField(queryset=__airport_queryset)
