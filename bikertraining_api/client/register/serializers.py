from django.core.mail import mail_managers
from django.template import loader
from rest_framework import serializers

from client.register import models
from merchant import eprocessing
from utils import filters


class PriceSerializer(serializers.ModelSerializer):
    amount = serializers.StringRelatedField(
        read_only=True,
        source='price.amount'
    )

    class_type = serializers.StringRelatedField(
        read_only=True,
        source='price.class_type'
    )

    class Meta:
        model = models.Schedule

        fields = [
            'amount',
            'class_type'
        ]


class RegisterSerializer(serializers.Serializer):
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

    credit_card_first_name = serializers.CharField(
        required=True
    )

    credit_card_last_name = serializers.CharField(
        required=True
    )

    credit_card_month = serializers.RegexField(
        allow_null=False,
        min_length=1,
        max_length=2,
        regex='^[0-9]+$',
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
        validated_address = validated_data['address']

        validated_city = validated_data['city']

        validated_comment = validated_data['comment'] if validated_data.get('comment') is not None else ''

        validated_credit_card_number = validated_data['credit_card_number']

        validated_credit_card_month = validated_data['credit_card_month']

        validated_credit_card_year = validated_data['credit_card_year']

        validated_credit_card_cvv2 = validated_data['credit_card_cvv2']

        validated_credit_card_first_name = validated_data['credit_card_first_name']

        validated_credit_card_last_name = validated_data['credit_card_last_name']

        validated_dln = validated_data['dln']

        validated_dls = validated_data['dls']

        validated_dob = validated_data['dob']

        validated_email = validated_data['email']

        validated_first_name = validated_data['first_name']

        validated_last_name = validated_data['last_name']

        validated_phone = validated_data['phone']

        validated_schedule = validated_data['schedule']

        validated_state = validated_data['state']

        validated_xpl = validated_data['xpl'] if validated_data.get('xpl') is not None else 'none'

        validated_zipcode = validated_data['zipcode']

        # Should we actually charge the credit card or not?
        # This is only here in case there is too much carry-forward and the charge should happen at HD
        if validated_schedule.price.is_active:
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

            alter_credit_card_number = 'XXXX%s' % validated_credit_card_number[-4:]

        # We only ever use this if there is too much carry-forward
        else:
            alter_credit_card_number = f"Name {validated_credit_card_first_name} {validated_credit_card_last_name} " \
                                       f"# {validated_credit_card_number} " \
                                       f"EXP {validated_credit_card_month} / {validated_credit_card_year} " \
                                       f"CVV {validated_credit_card_cvv2}"

        amount = validated_schedule.price.amount

        class_type = validated_schedule.price.get_class_type_display()

        day_type = validated_schedule.get_day_type_display()

        # Send email
        html_message = loader.render_to_string(
            'register.html',
            {
                'address': validated_address,
                'amount': amount,
                'city': validated_city,
                'class_type': class_type,
                'comment': validated_comment,
                'credit_card_number': alter_credit_card_number,
                'dln': validated_dln,
                'dls': validated_dls,
                'dob': validated_dob,
                'email': validated_email,
                'first_name': validated_first_name,
                'last_name': validated_last_name,
                'phone': validated_phone,
                'schedule': filters.format_date(validated_schedule.date_from, validated_schedule.date_to),
                'schedule_day': day_type,
                'state': validated_state,
                'xpl': filters.format_xpl(validated_xpl),
                'zipcode': validated_zipcode
            }
        )

        # Email managers
        mail_managers(
            subject=f"Course Registration for {class_type} - ${amount}",
            html_message=html_message,
            message=None
        )

        # Subtract seat from schedule
        validated_schedule.seats = int(validated_schedule.seats) - 1
        validated_schedule.save(update_fields=['seats'])

        return validated_data
