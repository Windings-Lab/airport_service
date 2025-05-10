from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from django_stubs_ext.db.models import TypedModelMeta
else:
    TypedModelMeta = object
from django.core.exceptions import ValidationError
from django.conf import settings
from django.core.validators import MinValueValidator
from django.db.models import (
    CASCADE,
    SET_NULL,
    CharField,
    DateTimeField,
    ForeignKey,
    IntegerField,
    ManyToManyField,
    Model,
    UniqueConstraint,
)

from airport.validators import fields_cant_be_same


class Flight(Model):
    route = ForeignKey("Route", on_delete=CASCADE, related_name="flights")
    airplane = ForeignKey(
        "Airplane", on_delete=SET_NULL, null=True, related_name="flights"
    )
    crew = ManyToManyField("airport.Crew", related_name="flights")
    departure_time = DateTimeField()
    arrival_time = DateTimeField()

    @property
    def name(self):
        return (
            f"{self.route.name} ({self.departure_time.strftime("%Y-%m-%d %H:%M:%S")}"
            f" → {self.arrival_time.strftime("%Y-%m-%d %H:%M:%S")})"
        )

    def clean(self):
        fields_cant_be_same(self.departure_time, self.arrival_time)

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


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
    rows = IntegerField(validators=[MinValueValidator(1)])
    seats_in_row = IntegerField(validators=[MinValueValidator(1)])
    airplane_type = ForeignKey(
        "AirplaneType", on_delete=CASCADE, related_name="airplanes"
    )

    @property
    def capacity(self):
        return self.rows * self.seats_in_row

    def __str__(self):
        return self.name


class AirplaneType(Model):
    name = CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Order(Model):
    created_at = DateTimeField(auto_now_add=True)
    user = ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=CASCADE, related_name="orders"
    )

    class Meta(TypedModelMeta):
        ordering = ["-created_at"]


class Ticket(Model):
    row = IntegerField()
    seat = IntegerField()
    flight = ForeignKey("Flight", on_delete=CASCADE, related_name="tickets")
    order = ForeignKey("Order", on_delete=CASCADE, related_name="tickets")

    class Meta(TypedModelMeta):
        constraints = [
            UniqueConstraint(name="unique_ticket", fields=["row", "seat", "flight"])
        ]

    def clean(self):
        airplane: Airplane = self.flight.airplane

        if not (1 <= self.row <= airplane.rows):
            raise ValidationError(f"Row should be in range (1, {airplane.rows})")

        if not (1 <= self.seat <= airplane.seats_in_row):
            raise ValidationError(
                f"Seat should be in range (1, {airplane.seats_in_row})"
            )

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)


class Airport(Model):
    name = CharField(max_length=100, unique=True)
    closest_big_city = CharField(max_length=100)

    def __str__(self):
        return self.name


class Route(Model):
    source = ForeignKey("Airport", on_delete=CASCADE, related_name="routes_from")
    destination = ForeignKey("Airport", on_delete=CASCADE, related_name="routes_to")
    distance = IntegerField(validators=[MinValueValidator(1)])

    @property
    def name(self):
        return f"{self.source.closest_big_city} → {self.destination.closest_big_city}"

    def __str__(self):
        return self.name

    def clean(self):
        fields_cant_be_same(self.source, self.destination)

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
