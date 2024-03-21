from rest_framework import serializers

from client.schedule.models import models


class SearchSerializer(serializers.ModelSerializer):
    amount = serializers.StringRelatedField(
        read_only=True,
        source='price.amount'
    )

    class_type = serializers.StringRelatedField(
        read_only=True,
        source='price.class_type'
    )

    class_type_name = serializers.StringRelatedField(
        read_only=True,
        source='price.get_class_type_display'
    )

    day_type_name = serializers.StringRelatedField(
        read_only=True,
        source='get_day_type_display'
    )

    class Meta:
        model = models.Schedule

        fields = '__all__'
