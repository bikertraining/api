from rest_framework import generics
from rest_framework.permissions import AllowAny

from client.price import models
from client.price import serializers


class Search(generics.ListAPIView):
    """
    Search prices
    """

    permission_classes = (
        AllowAny,
    )

    queryset = models.Price.objects.all()

    serializer_class = serializers.SearchSerializer
