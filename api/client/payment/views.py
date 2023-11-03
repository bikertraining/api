from rest_framework import generics
from rest_framework.permissions import AllowAny

from client.payment import models
from client.payment import serializers


class Index(generics.CreateAPIView):
    """
    Payment
    """

    permission_classes = (
        AllowAny,
    )

    serializer_class = serializers.PaymentSerializer


class Price(generics.RetrieveUpdateAPIView):
    """
    Price
    """

    permission_classes = (
        AllowAny,
    )

    serializer_class = serializers.PriceSerializer

    def get_object(self):
        return models.Price.objects.get(
            class_type=self.kwargs['class_type']
        )
