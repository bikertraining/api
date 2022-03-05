from rest_framework import generics
from rest_framework import views
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from admin.schedule import models
from admin.schedule import serializers


class Choices(views.APIView):
    """
    Choices
    """

    permission_classes = (
        IsAdminUser,
    )

    def get(self, request):
        result = {
            'class': {},
            'day': {},
            'price': {}
        }

        # Class
        for key, value in models.Price.ClassType.choices:
            result['class'].update({
                key: value
            })

        # Day
        for key, value in models.Schedule.DayType.choices:
            result['day'].update({
                key: value
            })

        # Price
        for item in models.Price.objects.all():
            result['price'].update({
                item.pk: item.get_class_type_display()
            })

        return Response(result)


class Create(generics.CreateAPIView):
    """
    Create schedule
    """

    permission_classes = (
        IsAdminUser,
    )

    queryset = models.Schedule.objects.all()

    serializer_class = serializers.CreateSerializer


class Delete(generics.RetrieveDestroyAPIView):
    """
    Delete schedule
    """

    permission_classes = (
        IsAdminUser,
    )

    queryset = models.Schedule.objects.all()

    serializer_class = serializers.SearchSerializer

    def perform_destroy(self, instance):
        instance.delete()


class Edit(generics.RetrieveUpdateAPIView):
    """
    Edit schedule
    """

    permission_classes = (
        IsAdminUser,
    )

    queryset = models.Schedule.objects.all()

    serializer_class = serializers.EditSerializer


class Search(generics.ListAPIView):
    """
    Search schedules
    """

    permission_classes = (
        IsAdminUser,
    )

    queryset = models.Schedule.objects.all()

    serializer_class = serializers.SearchSerializer
