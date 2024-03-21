from rest_framework import generics
from rest_framework.permissions import AllowAny

from client.team import serializers


class Index(generics.CreateAPIView):
    """
    Send team email
    """

    permission_classes = (
        AllowAny,
    )

    serializer_class = serializers.SendEmailSerializer
