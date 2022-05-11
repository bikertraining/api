from rest_framework import serializers

from admin.coach.models import models


class CreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Coach

        fields = '__all__'


class EditSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Coach

        fields = '__all__'


class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Coach

        fields = '__all__'


class MsfExpirationSerializer(serializers.Serializer):
    def create(self, validated_data):
        result = models.Coach.objects.all()

        return result
