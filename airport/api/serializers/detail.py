from rest_framework.serializers import CharField

import airport.api.serializers.base as base


class Flight(base.Flight):
    route = base.Route()
    airplane = base.Airplane()
    crew = base.Crew(many=True)

    class Meta(base.Flight.Meta):
        fields = ("route", "airplane", "crew", "departure_time", "arrival_time")


class Airplane(base.Airplane):
    airplane_type = CharField(source="airplane_type.name", read_only=True)

    class Meta(base.Airplane.Meta):
        fields = ("name", "airplane_type", "rows", "seats_in_row")


class Route(base.Route):
    class Meta(base.Route.Meta):
        fields = ("source", "destination", "distance")
