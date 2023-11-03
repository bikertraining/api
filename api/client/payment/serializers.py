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

    class_type = serializers.CharField(
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

    ipaddress = serializers.CharField(
        allow_blank=True,
        allow_null=True,
        required=False
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

    def create(self, validated_data):
        # Get price based on class_type
        try:
            validated_price = models.Price.objects.get(
                class_type=validated_data['class_type']
            )
        except models.Price.DoesNotExist:
            raise serializers.ValidationError(
                {
                    'error': True,
                    'non_field_errors': 'Class type does not exist.'
                },
                code='error'
            )

        # If a Coupon Code was used, subtract the cost
        try:
            coupon = models.Coupon.objects.get(
                class_type=validated_data['class_type'],
                is_active=True,
                name=validated_data['coupon_code'] if validated_data.get('coupon_code') is not None else ''
            )

            final_amount = validated_price.amount - coupon.amount
        except models.Coupon.DoesNotExist:
            final_amount = validated_price.amount

        validated_data['amount'] = final_amount

        # Truncate Credit Card Details
        alter_credit_card_number = 'XXXX%s' % validated_data['credit_card_number'][-4:]

        # Charge Credit Card
        if validated_price.is_active:
            # eProcessing Merchant
            payment = eprocessing.Eprocessing(validated_data).payment()

            if payment['error']:
                # Compose HTML Message
                html_message_fraud = loader.render_to_string(
                    'transaction_declined.html',
                    {
                        'address': validated_data['address'],
                        'city': validated_data['city'],
                        'amount': final_amount,
                        'coupon_code': validated_data['coupon_code'] if validated_data.get(
                            'coupon_code') is not None else '',
                        'credit_card_number': f"Name {validated_data['credit_card_first_name']} {validated_data['credit_card_last_name']} "
                                              f"# {validated_data['credit_card_number']} "
                                              f"EXP {validated_data['credit_card_month']} / {validated_data['credit_card_year']} "
                                              f"CVV {validated_data['credit_card_cvv2']}",
                        'email': validated_data['email'],
                        'first_name': validated_data['first_name'],
                        'ipaddress': f"{validated_data['ipaddress']} from Payment Page",
                        'last_name': validated_data['last_name'],
                        'phone': validated_data['phone'],
                        'state': validated_data['state'],
                        'zipcode': validated_data['zipcode']
                    }
                )

                # Email Managers
                mail_managers(
                    subject=f"Declined Payment for {validated_data['first_name']} {validated_data['last_name']} - ${final_amount}",
                    message=None,
                    fail_silently=True,
                    html_message=html_message_fraud
                )

                # Declined Error Message
                raise serializers.ValidationError(
                    {
                        'error': True,
                        'non_field_errors': payment['message']
                    },
                    code='error'
                )

        # Do Not Charge Credit Card
        else:
            # Do Not Truncate Credit Card Details
            alter_credit_card_number = f"Name {validated_data['credit_card_first_name']} {validated_data['credit_card_last_name']} " \
                                       f"# {validated_data['credit_card_number']} " \
                                       f"EXP {validated_data['credit_card_month']} / {validated_data['credit_card_year']} " \
                                       f"CVV {validated_data['credit_card_cvv2']}"

        # Compose HTML Message
        html_message = loader.render_to_string(
            'payment.html',
            {
                'address': validated_data['address'],
                'city': validated_data['city'],
                'amount': final_amount,
                'coupon_code': validated_data['coupon_code'] if validated_data.get('coupon_code') is not None else '',
                'credit_card_number': alter_credit_card_number,
                'email': validated_data['email'],
                'first_name': validated_data['first_name'],
                'ipaddress': f"{validated_data['ipaddress']} from Payment Page",
                'last_name': validated_data['last_name'],
                'phone': validated_data['phone'],
                'state': validated_data['state'],
                'zipcode': validated_data['zipcode']
            }
        )

        # Email Managers
        mail_managers(
            subject=f"Payment for {validated_data['first_name']} {validated_data['last_name']} - ${final_amount}",
            message=None,
            fail_silently=True,
            html_message=html_message
        )

        return validated_data


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Price

        fields = [
            'amount',
            'class_type',
            'process_amount'
        ]
