from rest_framework import serializers

from merchant import eprocessing
from test import models


class TestSerializer(serializers.Serializer):
    address = serializers.CharField(
        required=True
    )

    city = serializers.CharField(
        required=True
    )

    comment = serializers.CharField(
        allow_blank=True,
        allow_null=True,
        required=False
    )

    credit_card_cvv2 = serializers.RegexField(
        allow_null=False,
        min_length=3,
        max_length=4,
        regex='^[0-9]+$',
        required=True
    )

    credit_card_month = serializers.RegexField(
        allow_null=False,
        min_length=2,
        max_length=2,
        regex='^[0-9]+$',
        required=True
    )

    credit_card_name = serializers.CharField(
        required=True
    )

    credit_card_number = serializers.CharField(
        allow_null=False,
        min_length=15,
        max_length=16,
        required=True
    )

    credit_card_year = serializers.RegexField(
        allow_null=False,
        min_length=4,
        max_length=4,
        regex='^[0-9]+$',
        required=True
    )

    dln = serializers.CharField(
        required=True
    )

    dls = serializers.CharField(
        required=True
    )

    dob = serializers.CharField(
        required=True
    )

    email = serializers.EmailField(
        required=True
    )

    first_name = serializers.CharField(
        required=True
    )

    last_name = serializers.CharField(
        required=True
    )

    phone = serializers.CharField(
        required=True
    )

    schedule = serializers.PrimaryKeyRelatedField(
        queryset=models.Schedule.objects.all(),
        required=True
    )

    state = serializers.RegexField(
        allow_null=False,
        max_length=3,
        regex='^[a-zA-Z]+$',
        required=True
    )

    xpl = serializers.CharField(
        required=False
    )

    zipcode = serializers.CharField(
        allow_null=False,
        max_length=28,
        required=True
    )

    def validate_schedule(self, value):
        try:
            models.Schedule.objects.get(
                pk=value.pk
            )
        except models.Schedule.DoesNotExist:
            raise serializers.ValidationError(
                'Schedule does not exist.',
                code='not_found'
            )

        return value

    def create(self, validated_data):
        # Charge credit card
        payment = eprocessing.Eprocessing(validated_data).charge()

        if payment['error']:
            raise serializers.ValidationError(
                {
                    'error': True,
                    'non_field_errors': payment['message']
                },
                code='error'
            )

        return validated_data
