from django.db import models, transaction
from typing import TypeVar
from rest_framework.serializers import (
    ModelSerializer,
    ValidationError,
    SlugRelatedField,
)
import airport.models

T = TypeVar("T", bound=models.Model)


class BaseAirport(ModelSerializer[T]):
    """Base serializer for all airport-related models."""

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        meta = getattr(cls, "Meta", None)
        if meta and not hasattr(meta, "ref_name"):
            module_name = cls.__module__.split(".")[-1].capitalize()
            class_name = cls.__name__
            meta.ref_name = f"{module_name}{class_name}"

    class Meta:
        fields = "__all__"


class Flight(BaseAirport[airport.models.Flight]):
    class Meta(BaseAirport.Meta):
        model = airport.models.Flight


class Crew(BaseAirport[airport.models.Crew]):
    class Meta(BaseAirport.Meta):
        model = airport.models.Crew


class Airplane(BaseAirport[airport.models.Airplane]):
    class Meta(BaseAirport.Meta):
        model = airport.models.Airplane


class AirplaneType(BaseAirport[airport.models.AirplaneType]):
    class Meta(BaseAirport.Meta):
        model = airport.models.AirplaneType


class Ticket(BaseAirport[airport.models.Ticket]):
    flight = SlugRelatedField(read_only=True, slug_field="name")

    class Meta(BaseAirport.Meta):
        model = airport.models.Ticket
        fields = ("id", "row", "seat", "flight")

    def validate(self, attrs):
        data = super().validate(attrs=attrs)

        row = attrs["row"]
        seat = attrs["seat"]
        flight: airport.models.Flight = attrs["flight"]
        airplane: airport.models.Airplane = flight.airplane

        if not (1 <= row <= airplane.rows):
            raise ValidationError(f"Row should be in range (1, {airplane.rows})")

        if not (1 <= seat <= airplane.seats_in_row):
            raise ValidationError(
                f"Seat should be in range (1, {airplane.seats_in_row})"
            )

        return data


class Order(BaseAirport[airport.models.Order]):
    tickets = Ticket(many=True, read_only=True)

    class Meta(BaseAirport.Meta):
        model = airport.models.Order
        fields = ("id", "tickets", "created_at")

    def create(self, validated_data):
        with transaction.atomic():
            tickets_data = validated_data.pop("tickets")
            user = self.context["request"].user
            validated_data["user"] = user
            order = airport.models.Order.objects.create(**validated_data)
            for ticket_data in tickets_data:
                airport.models.Ticket.objects.create(order=order, **ticket_data)
            return order


class Airport(BaseAirport[airport.models.Airport]):
    class Meta(BaseAirport.Meta):
        model = airport.models.Airport


class Route(BaseAirport[airport.models.Route]):
    class Meta(BaseAirport.Meta):
        model = airport.models.Route
