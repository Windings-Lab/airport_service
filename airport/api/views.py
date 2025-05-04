from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin

import airport.models
import airport.api.serializers.list as serializer_list
import airport.api.serializers.base as serializer_base


class Flight(ListModelMixin, GenericViewSet):
    queryset = airport.models.Flight.objects.all()
    serializer_class = serializer_list.Flight

    def get_queryset(self):
        queryset = self.queryset

        queryset = queryset.select_related(
            "route",
            "route__source",
            "route__destination",
            "airplane"
        )
        queryset = queryset.prefetch_related("crew")

        return queryset


class Crew(ListModelMixin, GenericViewSet):
    queryset = airport.models.Crew.objects.all()
    serializer_class = serializer_base.Crew


class Airplane(ListModelMixin, GenericViewSet):
    queryset = airport.models.Airplane.objects.all()
    serializer_class = serializer_base.Airplane


class AirplaneType(ListModelMixin, GenericViewSet):
    queryset = airport.models.AirplaneType.objects.all()
    serializer_class = serializer_base.AirplaneType


class Order(ListModelMixin, GenericViewSet):
    queryset = airport.models.Order.objects.all()
    serializer_class = serializer_base.Order


class Ticket(ListModelMixin, GenericViewSet):
    queryset = airport.models.Ticket.objects.all()
    serializer_class = serializer_base.Ticket


class Airport(ListModelMixin, GenericViewSet):
    queryset = airport.models.Airport.objects.all()
    serializer_class = serializer_base.Airport


class Route(ListModelMixin, GenericViewSet):
    queryset = airport.models.Route.objects.all()
    serializer_class = serializer_list.Route

    def get_queryset(self):
        queryset = self.queryset

        queryset = queryset.select_related("source", "destination")

        return queryset
