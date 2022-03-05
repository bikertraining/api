from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from admin.price import models
from admin.price import serializers


class Create(generics.CreateAPIView):
    """
    Create price
    """

    permission_classes = (
        IsAdminUser,
    )

    queryset = models.Price.objects.all()

    serializer_class = serializers.CreateSerializer


class Delete(generics.RetrieveDestroyAPIView):
    """
    Delete price
    """

    permission_classes = (
        IsAdminUser,
    )

    queryset = models.Price.objects.all()

    serializer_class = serializers.SearchSerializer

    def perform_destroy(self, instance):
        instance.delete()


class Edit(generics.RetrieveUpdateAPIView):
    """
    Edit price
    """

    permission_classes = (
        IsAdminUser,
    )

    queryset = models.Price.objects.all()

    serializer_class = serializers.EditSerializer


class Search(generics.ListAPIView):
    """
    Search prices
    """

    permission_classes = (
        IsAdminUser,
    )

    queryset = models.Price.objects.all()

    serializer_class = serializers.SearchSerializer
