from rest_framework.serializers import CharField, SlugRelatedField

import airport.api.serializers.base as base


class Flight(base.Flight):
    route = CharField(source="route.name", read_only=True)
    airplane = CharField(source="airplane.name", read_only=True)
    crew = SlugRelatedField(many=True, read_only=True, slug_field="full_name")
