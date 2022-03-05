from rest_framework import generics
from rest_framework.permissions import AllowAny

from client.register import models
from client.register import serializers


class Index(generics.CreateAPIView):
    """
    Register
    """

    permission_classes = (
        AllowAny,
    )

    serializer_class = serializers.RegisterSerializer


class Price(generics.RetrieveUpdateAPIView):
    """
    Price
    """

    permission_classes = (
        AllowAny,
    )

    serializer_class = serializers.PriceSerializer

    def get_object(self):
        return models.Schedule.objects.get(
            pk=self.kwargs['pk']
        )
