from rest_framework.serializers import CharField, SlugRelatedField

import airport.api.serializers.base as base


class Flight(base.Flight):
    route = CharField(source="route.name", read_only=True)
    airplane = CharField(source="airplane.name", read_only=True)
    crew = SlugRelatedField(many=True, read_only=True, slug_field="full_name")


class Airplane(base.Airplane):
    airplane_type = CharField(source="airplane_type.name", read_only=True)

    class Meta(base.Airplane.Meta):
        fields = ("id", "name", "airplane_type", "rows", "seats_in_row")


class Route(base.Route):
    source = CharField(source="source.closest_big_city", read_only=True)
    destination = CharField(source="destination.closest_big_city", read_only=True)
