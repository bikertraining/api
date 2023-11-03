from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from admin.coach import models
from admin.coach import serializers


class Create(generics.CreateAPIView):
    """
    Create coach
    """

    permission_classes = (
        IsAdminUser,
    )

    queryset = models.Coach.objects.all()

    serializer_class = serializers.CreateSerializer


class Delete(generics.RetrieveDestroyAPIView):
    """
    Delete coach
    """

    permission_classes = (
        IsAdminUser,
    )

    queryset = models.Coach.objects.all()

    serializer_class = serializers.SearchSerializer

    def perform_destroy(self, instance):
        instance.delete()


class Edit(generics.RetrieveUpdateAPIView):
    """
    Edit coach
    """

    permission_classes = (
        IsAdminUser,
    )

    queryset = models.Coach.objects.all()

    serializer_class = serializers.EditSerializer


class Search(generics.ListAPIView):
    """
    Search coaches
    """

    permission_classes = (
        IsAdminUser,
    )

    queryset = models.Coach.objects.all()

    serializer_class = serializers.SearchSerializer
