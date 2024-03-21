from rest_framework import generics
from rest_framework.permissions import AllowAny

from client.ecourse import models
from client.ecourse import serializers


class Ecourse(generics.RetrieveAPIView):
    """
    View eCourse
    """

    permission_classes = (
        AllowAny,
    )

    queryset = models.Ecourse.objects.all()

    serializer_class = serializers.EcourseSerializer

    def get_object(self):
        return models.Ecourse.objects.last()
