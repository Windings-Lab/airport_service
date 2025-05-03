from django.contrib.auth import get_user_model
from django.db.models import (
    Model,
    CharField,
    DateTimeField,
    IntegerField,
    ForeignKey,
    ManyToManyField,
    SET_NULL,
    CASCADE,
)


class Flight(Model):
    route = ForeignKey("Route", on_delete=CASCADE, related_name="flights")
    airplane = ForeignKey(
        "Airplane", on_delete=SET_NULL, null=True, related_name="flights"
    )
    crew = ManyToManyField("Crew", related_name="flights")
    departure_time = DateTimeField()
    arrival_time = DateTimeField()


class Crew(Model):
    first_name = CharField(max_length=100)
    last_name = CharField(max_length=100)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name


class Airplane(Model):
    name = CharField(max_length=100)
    rows = IntegerField()
    seats_in_row = IntegerField()
    airplane_type = ForeignKey(
        "AirplaneType", on_delete=CASCADE, related_name="airplanes"
    )

    def __str__(self):
        return self.name


class AirplaneType(Model):
    name = CharField(max_length=100)

    def __str__(self):
        return self.name


class Order(Model):
    created_at = DateTimeField()
    user = ForeignKey(
        get_user_model(), on_delete=CASCADE, related_name="orders"
    )


class Ticket(Model):
    row = IntegerField()
    seat = IntegerField()
    flight = ForeignKey("Flight", on_delete=CASCADE, related_name="tickets")
    order = ForeignKey("Order", on_delete=CASCADE, related_name="tickets")


class Airport(Model):
    name = CharField(max_length=100)
    closest_big_city = CharField(max_length=100)

    def __str__(self):
        return self.name


class Route(Model):
    source = ForeignKey("Airport", on_delete=CASCADE, related_name="routes")
    destination = ForeignKey(
        "Airport", on_delete=CASCADE, related_name="routes"
    )
    distance = IntegerField()
