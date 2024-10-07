from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from admin.register import models
from admin.register import serializers


class Print(generics.RetrieveAPIView):
    """
    Print registration
    """

    permission_classes = (
        IsAdminUser,
    )

    serializer_class = serializers.PrintSerializer

    def get_queryset(self):
        return models.Register.objects.filter(
            pk=self.kwargs['pk'],
            schedule=self.kwargs['schedule']
        )


class Search(generics.ListAPIView):
    """
    Search registrations
    """

    permission_classes = (
        IsAdminUser,
    )

    serializer_class = serializers.SearchSerializer

    def get_queryset(self):
        return models.Register.objects.filter(schedule=self.kwargs['schedule'])
