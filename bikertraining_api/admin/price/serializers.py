from rest_framework import serializers

from admin.price.models import models


class CreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Price

        fields = '__all__'


class EditSerializer(serializers.ModelSerializer):
    class_type_name = serializers.StringRelatedField(
        read_only=True,
        source='get_class_type_display'
    )

    class Meta:
        model = models.Price

        fields = '__all__'


class SearchSerializer(serializers.ModelSerializer):
    class_type_name = serializers.StringRelatedField(
        read_only=True,
        source='get_class_type_display'
    )

    class Meta:
        model = models.Price

        fields = '__all__'
