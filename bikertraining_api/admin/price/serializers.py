import os

from rest_framework import serializers

from admin.price.models import models


class BuildPriceSerializer(serializers.Serializer):
    def validate(self, attrs):
        if not os.path.exists('/home/Diemuzi/api/bikertraining_api/application/.env'):
            raise serializers.ValidationError(
                '.env has not been installed.',
                code='not_found'
            )

        return attrs

    def create(self, validated_data):
        class_types = [
            'brc',
            'erc',
            '3wbrc'
        ]

        for item in class_types:
            result = models.Price.objects.filter(class_type=item)

            if not result.exists():
                models.Price.objects.create(
                    amount=0.00,
                    class_type=item
                )

        return validated_data


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
