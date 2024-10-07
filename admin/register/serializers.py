from rest_framework import serializers

from admin.register.models import models


class PrintSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Register

        fields = '__all__'


class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Register

        fields = '__all__'
