from django.db import models
from typing import TypeVar
from rest_framework.serializers import ModelSerializer
import airport.models

T = TypeVar("T", bound=models.Model)


class BaseAirport(ModelSerializer[T]):
    """Base serializer for all airport-related models."""

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


class Order(BaseAirport[airport.models.Order]):
    class Meta(BaseAirport.Meta):
        model = airport.models.Order


class Ticket(BaseAirport[airport.models.Ticket]):
    class Meta(BaseAirport.Meta):
        model = airport.models.Ticket


class Airport(BaseAirport[airport.models.Airport]):
    class Meta(BaseAirport.Meta):
        model = airport.models.Airport


class Route(BaseAirport[airport.models.Route]):
    class Meta(BaseAirport.Meta):
        model = airport.models.Route
