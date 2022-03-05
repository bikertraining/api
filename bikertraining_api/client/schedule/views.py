from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from client.schedule import models
from client.schedule import serializers


class Search(generics.ListAPIView):
    """
    Search schedules
    """

    permission_classes = (
        IsAuthenticatedOrReadOnly,
    )

    queryset = models.Schedule.objects.all()

    serializer_class = serializers.SearchSerializer
