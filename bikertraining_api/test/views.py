import requests
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.permissions import AllowAny

from test import serializers


class Index(generics.CreateAPIView):
    """
    Index
    """

    permission_classes = (
        AllowAny,
    )

    serializer_class = serializers.TestSerializer


def test(request):
    """
    Test eProcessing Response

    :return: HttpResponse
    """

    data = {}

    result = requests.post(
        'https://diemuzi.pythonanywhere.com/test/index',
        # headers=headers,
        json=data
    )

    return HttpResponse(result)
