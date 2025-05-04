from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin

import airport.models
import airport.api.serializers.list as serializer_list


class Flight(ListModelMixin, GenericViewSet):
    queryset = airport.models.Flight.objects.all()
    serializer_class = serializer_list.Flight
