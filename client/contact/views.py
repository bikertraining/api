from rest_framework import generics
from rest_framework.permissions import AllowAny

from client.contact import models
from client.contact import serializers


class Index(generics.CreateAPIView):
    """
    Send contact email
    """

    permission_classes = (
        AllowAny,
    )

    serializer_class = serializers.SendEmailSerializer


class Delete(generics.RetrieveDestroyAPIView):
    """
    Delete contact
    """

    permission_classes = (
        AllowAny,
    )

    lookup_field = 'email'

    queryset = models.Contact.objects.all()

    serializer_class = serializers.DeleteSerializer

    def perform_destroy(self, instance):
        instance.delete()
