from rest_framework.viewsets import ModelViewSet
from django.db.models import Prefetch

import airport.models
from airport.api.serializers import (
    base as serializers_base,
    list as serializers_list,
    detail as serializers_detail,
    post as serializers_post,
)
from app.permissions import IsAdminOrIfAuthenticatedReadOnly


class BaseViewMixin:
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)


class Flight(BaseViewMixin, ModelViewSet):
    queryset = airport.models.Flight.objects.all()
    serializer_class = serializers_base.Flight

    def get_queryset(self):
        queryset = self.queryset

        queryset = queryset.select_related(
            "route", "route__source", "route__destination", "airplane"
        )
        queryset = queryset.prefetch_related("crew")

        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return serializers_list.Flight

        if self.action == "retrieve":
            return serializers_detail.Flight

        if self.action == "create":
            return serializers_post.Flight

        return self.serializer_class


class Crew(BaseViewMixin, ModelViewSet):
    queryset = airport.models.Crew.objects.all()
    serializer_class = serializers_base.Crew


class Airplane(BaseViewMixin, ModelViewSet):
    queryset = airport.models.Airplane.objects.all()
    serializer_class = serializers_base.Airplane

    def get_queryset(self):
        queryset = self.queryset

        queryset = queryset.select_related("airplane_type")

        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return serializers_list.Airplane

        if self.action == "retrieve":
            return serializers_detail.Airplane

        return self.serializer_class


class AirplaneType(BaseViewMixin, ModelViewSet):
    queryset = airport.models.AirplaneType.objects.all()
    serializer_class = serializers_base.AirplaneType


class Order(BaseViewMixin, ModelViewSet):
    queryset = airport.models.Order.objects.all()
    serializer_class = serializers_base.Order

    def get_queryset(self):
        queryset = self.queryset
        ticket_qs = airport.models.Ticket.objects.select_related(
            "flight__route__source",
            "flight__route__destination",
            "flight__route",
            "flight",
        )
        queryset = queryset.select_related("user")
        queryset = queryset.prefetch_related(Prefetch("tickets", queryset=ticket_qs))

        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return serializers_list.Order

        if self.action == "create":
            return serializers_post.Order

        return self.serializer_class


class Airport(BaseViewMixin, ModelViewSet):
    queryset = airport.models.Airport.objects.all()
    serializer_class = serializers_base.Airport


class Route(BaseViewMixin, ModelViewSet):
    queryset = airport.models.Route.objects.all()
    serializer_class = serializers_base.Route

    def get_queryset(self):
        queryset = self.queryset

        queryset = queryset.select_related("source", "destination")

        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return serializers_list.Route

        if self.action == "retrieve":
            return serializers_detail.Route

        if self.action == "create":
            return serializers_post.Route

        return self.serializer_class
