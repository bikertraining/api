from rest_framework import generics
from rest_framework.exceptions import APIException
from rest_framework.permissions import AllowAny

from client.coupon import models
from client.coupon import serializers


class Search(generics.ListAPIView):
    """
    Search
    """

    permission_classes = (
        AllowAny,
    )

    queryset = models.Coupon.objects.all()

    serializer_class = serializers.SearchSerializer


class Validate(generics.RetrieveAPIView):
    """
    Validate
    """

    permission_classes = (
        AllowAny,
    )

    queryset = models.Coupon.objects.all()

    serializer_class = serializers.SearchSerializer

    def get_object(self):
        try:
            return models.Coupon.objects.get(
                name=self.kwargs['name'],
                class_type=self.kwargs['class_type'],
                is_active=True
            )
        except models.Coupon.DoesNotExist:
            from django.http import JsonResponse
            raise ServiceUnavailable(
                {
                    'error': True,
                    'errors': {
                        'coupon_code': [
                            'Invalid coupon'
                        ]
                    }
                }
            )


class ServiceUnavailable(APIException):
    status_code = 200
    default_detail = 'Service temporarily unavailable, try again later.'
    default_code = 'service_unavailable'
