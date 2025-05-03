from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin

import airport.models
import airport.api.serializers as serializers


class Flight(ListModelMixin, GenericViewSet):
    queryset = airport.models.Flight.objects.all()
    serializer_class = serializers.Flight
