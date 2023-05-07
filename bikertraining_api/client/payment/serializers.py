from django.core.mail import mail_managers
from django.template import loader
from rest_framework import serializers

from client.payment import models
from merchant import eprocessing


class PaymentSerializer(serializers.Serializer):
    address = serializers.CharField(
        required=True
    )

    city = serializers.CharField(
        required=True
    )

    coupon_code = serializers.CharField(
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

    state = serializers.RegexField(
        allow_null=False,
        max_length=3,
        regex='^[a-zA-Z]+$',
        required=True
    )

    zipcode = serializers.CharField(
        allow_null=False,
        max_length=28,
        required=True
    )

    def validate(self, attrs):
        try:
            models.Price.objects.get(
                class_type='brc'
            )
        except models.Price.DoesNotExist:
            raise serializers.ValidationError(
                'Price does not exist.',
                code='not_found'
            )

        return attrs

    def create(self, validated_data):
        validated_address = validated_data['address']

        validated_city = validated_data['city']

        validated_coupon_code = validated_data['coupon_code'] if validated_data.get('coupon_code') is not None else ''

        validated_credit_card_number = validated_data['credit_card_number']

        validated_credit_card_month = validated_data['credit_card_month']

        validated_credit_card_year = validated_data['credit_card_year']

        validated_credit_card_cvv2 = validated_data['credit_card_cvv2']

        validated_credit_card_first_name = validated_data['credit_card_first_name']

        validated_credit_card_last_name = validated_data['credit_card_last_name']

        validated_email = validated_data['email']

        validated_first_name = validated_data['first_name']

        validated_last_name = validated_data['last_name']

        validated_phone = validated_data['phone']

        validated_price = models.Price.objects.get(
            class_type='brc'
        )

        validated_state = validated_data['state']

        validated_zipcode = validated_data['zipcode']

        # validated_data['amount'] = validated_price.amount

        # If a Coupon Code was used, subtract the cost
        try:
            coupon = models.Coupon.objects.get(
                class_type='brc',
                is_active=True,
                name=validated_coupon_code
            )

            final_amount = validated_price.amount - coupon.amount
        except models.Coupon.DoesNotExist:
            final_amount = validated_price.amount

        validated_data['amount'] = final_amount

        # Should we actually charge the credit card or not?
        # This is only here in case there is too much carry-forward and the charge should happen at HD
        if validated_price.is_active:
            # Charge credit card
            payment = eprocessing.Eprocessing(validated_data).payment()

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

        # Send email
        html_message = loader.render_to_string(
            'payment.html',
            {
                'address': validated_address,
                'city': validated_city,
                'amount': final_amount,
                'coupon_code': validated_coupon_code,
                'credit_card_number': alter_credit_card_number,
                'email': validated_email,
                'first_name': validated_first_name,
                'last_name': validated_last_name,
                'phone': validated_phone,
                'state': validated_state,
                'zipcode': validated_zipcode
            }
        )

        # Email managers
        mail_managers(
            subject=f"Payment for {validated_first_name} {validated_last_name} - ${final_amount}",
            html_message=html_message,
            message=None
        )

        return validated_data
