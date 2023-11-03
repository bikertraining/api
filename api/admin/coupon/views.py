from rest_framework import generics
from rest_framework import views
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from admin.coupon import models
from admin.coupon import serializers


class Choices(views.APIView):
    """
    Choices
    """

    permission_classes = (
        IsAdminUser,
    )

    @staticmethod
    def get(request):
        result = {
            'class': {}
        }

        # Class
        for key, value in models.Coupon.ClassType.choices:
            result['class'].update({
                key: value
            })

        return Response(result)


class Create(generics.CreateAPIView):
    """
    Create coupon
    """

    permission_classes = (
        IsAdminUser,
    )

    queryset = models.Coupon.objects.all()

    serializer_class = serializers.CreateSerializer


class Delete(generics.RetrieveDestroyAPIView):
    """
    Delete coupon
    """

    permission_classes = (
        IsAdminUser,
    )

    queryset = models.Coupon.objects.all()

    serializer_class = serializers.SearchSerializer

    def perform_destroy(self, instance):
        instance.delete()


class Edit(generics.RetrieveUpdateAPIView):
    """
    Edit coupon
    """

    permission_classes = (
        IsAdminUser,
    )

    queryset = models.Coupon.objects.all()

    serializer_class = serializers.EditSerializer


class Search(generics.ListAPIView):
    """
    Search coupons
    """

    permission_classes = (
        IsAdminUser,
    )

    queryset = models.Coupon.objects.all()

    serializer_class = serializers.SearchSerializer
