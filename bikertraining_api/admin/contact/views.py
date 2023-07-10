from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from admin.contact import models
from admin.contact import serializers


class Create(generics.CreateAPIView):
    """
    Create contact
    """

    permission_classes = (
        IsAdminUser,
    )

    queryset = models.Contact.objects.all()

    serializer_class = serializers.CreateSerializer


class Delete(generics.RetrieveDestroyAPIView):
    """
    Delete contact
    """

    permission_classes = (
        IsAdminUser,
    )

    queryset = models.Contact.objects.all()

    serializer_class = serializers.SearchSerializer

    def perform_destroy(self, instance):
        instance.delete()


class Edit(generics.RetrieveUpdateAPIView):
    """
    Edit contact
    """

    permission_classes = (
        IsAdminUser,
    )

    queryset = models.Contact.objects.all()

    serializer_class = serializers.EditSerializer


class Search(generics.ListAPIView):
    """
    Search contacts
    """

    permission_classes = (
        IsAdminUser,
    )

    queryset = models.Contact.objects.all().order_by('name')

    serializer_class = serializers.SearchSerializer
