from rest_framework.serializers import PrimaryKeyRelatedField

import airport.api.serializers.base as base
import airport.models


class Ticket(base.Ticket):
    flight = PrimaryKeyRelatedField(
        queryset=airport.models.Flight.objects.select_related()
    )


class Order(base.Order):
    tickets = Ticket(many=True)
