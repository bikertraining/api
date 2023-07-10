from rest_framework import serializers

from admin.contact.models import models


class CreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contact

        fields = '__all__'


class EditSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contact

        fields = '__all__'


class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contact

        fields = '__all__'
