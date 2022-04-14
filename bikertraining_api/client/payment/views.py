from rest_framework import generics
from rest_framework.permissions import AllowAny

from client.payment import serializers


class Index(generics.CreateAPIView):
    """
    Payment
    """

    permission_classes = (
        AllowAny,
    )

    serializer_class = serializers.PaymentSerializer
