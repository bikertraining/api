from rest_framework import generics
from rest_framework import views
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from admin.fraud import models
from admin.fraud import serializers


class Choices(views.APIView):
    permission_classes = (
        IsAdminUser,
    )

    @staticmethod
    def get(request):
        return Response(dict(models.FraudString.Type.choices))


class Create(generics.CreateAPIView):
    permission_classes = (
        IsAdminUser,
    )

    queryset = models.FraudString.objects.all()

    serializer_class = serializers.CreateSerializer


class Delete(generics.RetrieveDestroyAPIView):
    permission_classes = (
        IsAdminUser,
    )

    queryset = models.FraudString.objects.all()

    serializer_class = serializers.SearchSerializer


class Edit(generics.RetrieveUpdateAPIView):
    permission_classes = (
        IsAdminUser,
    )

    queryset = models.FraudString.objects.all()

    serializer_class = serializers.ProfileSerializer


class Search(generics.ListAPIView):
    permission_classes = (
        IsAdminUser,
    )

    queryset = models.FraudString.objects.all()

    serializer_class = serializers.SearchSerializer
