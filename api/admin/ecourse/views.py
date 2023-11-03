from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from admin.ecourse import models
from admin.ecourse import serializers


class Ecourse(generics.RetrieveUpdateAPIView):
    """
    Edit eCourse
    """

    permission_classes = (
        IsAdminUser,
    )

    queryset = models.Ecourse.objects.all()

    serializer_class = serializers.EcourseSerializer

    def get_object(self):
        return models.Ecourse.objects.last()
