from rest_framework import generics
from rest_framework.permissions import AllowAny

from client.schedule import models
from client.schedule import serializers


class Search(generics.ListAPIView):
    """
    Search schedules
    """

    permission_classes = (
        AllowAny,
    )

    queryset = models.Schedule.objects.all()

    serializer_class = serializers.SearchSerializer
