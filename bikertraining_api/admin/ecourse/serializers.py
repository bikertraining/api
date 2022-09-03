from rest_framework import serializers

from admin.ecourse.models import models


class EcourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ecourse

        fields = '__all__'
