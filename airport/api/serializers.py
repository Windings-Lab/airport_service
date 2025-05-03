from rest_framework.serializers import ModelSerializer

import airport.models


class Flight(ModelSerializer[airport.models.Flight]):
    class Meta:
        model = airport.models.Flight
        fields = "__all__"
