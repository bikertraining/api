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

    process_amount = serializers.StringRelatedField(
        read_only=True,
        source='price.process_amount'
    )

    class Meta:
        model = models.Schedule

        fields = [
            'amount',
            'class_type',
            'process_amount'
        ]


class RegisterSerializer(serializers.Serializer):
    address = serializers.CharField(
        required=True
    )

    city = serializers.CharField(
        required=True
    )

    class_type = serializers.CharField(
        required=True
    )

    comment = serializers.CharField(
        allow_blank=True,
        allow_null=True,
        required=False
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

    @staticmethod
    def validate_schedule(value):
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
        # If a Coupon Code was used, subtract the cost
        try:
            coupon = models.Coupon.objects.get(
                class_type=validated_data['class_type'],
                is_active=True,
                name=validated_data['coupon_code'] if validated_data.get('coupon_code') is not None else ''
            )

            final_amount = validated_data['schedule'].price.amount - coupon.amount
        except models.Coupon.DoesNotExist:
            final_amount = validated_data['schedule'].price.amount

        validated_data['amount'] = final_amount

        # Truncate Credit Card Details
        alter_credit_card_number = 'XXXX%s' % validated_data['credit_card_number'][-4:]

        # Charge Credit Card
        if validated_data['schedule'].price.is_active:
            # eProcessing Merchant
            payment = eprocessing.Eprocessing(validated_data).charge()

            # Declined
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
            'register.html',
            {
                'address': validated_data['address'],
                'amount': validated_data['amount'],
                'city': validated_data['city'],
                'class_type': validated_data['schedule'].price.get_class_type_display(),
                'comment': validated_data['comment'] if validated_data.get('comment') is not None else '',
                'coupon_code': validated_data['coupon_code'] if validated_data.get('coupon_code') is not None else '',
                'credit_card_number': alter_credit_card_number,
                'dln': validated_data['dln'],
                'dls': validated_data['dls'],
                'dob': validated_data['dob'],
                'email': validated_data['email'],
                'first_name': validated_data['first_name'],
                'last_name': validated_data['last_name'],
                'phone': validated_data['phone'],
                'schedule': filters.format_date(validated_data['schedule'].date_from,
                                                validated_data['schedule'].date_to),
                'schedule_day': validated_data['schedule'].get_day_type_display(),
                'state': validated_data['state'],
                'xpl': filters.format_xpl(validated_data['xpl'] if validated_data.get('xpl') is not None else 'none'),
                'zipcode': validated_data['zipcode']
            }
        )

        # Email Managers
        mail_managers(
            subject=f"Course Registration for {validated_data['schedule'].price.get_class_type_display()} - ${validated_data['amount']}",
            message=None,
            fail_silently=True,
            html_message=html_message
        )

        # Subtract seat from schedule
        validated_data['schedule'].seats = int(validated_data['schedule'].seats) - 1
        validated_data['schedule'].save(update_fields=['seats'])

        # Save Student Information - Will be removed once class is deleted
        # This is only here in case an email was not received, and we are missing information
        models.Register.objects.create(
            address=validated_data['address'],
            amount=validated_data['amount'],
            city=validated_data['city'],
            class_type=validated_data['schedule'].price.get_class_type_display(),
            comment=validated_data['comment'] if validated_data.get('comment') is not None else '',
            coupon_code=validated_data['coupon_code'] if validated_data.get('coupon_code') is not None else '',
            credit_card_number=alter_credit_card_number,
            dln=validated_data['dln'],
            dls=validated_data['dls'],
            dob=validated_data['dob'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone=validated_data['phone'],
            schedule_date=filters.format_date(validated_data['schedule'].date_from, validated_data['schedule'].date_to),
            schedule_day=validated_data['schedule'].get_day_type_display(),
            state=validated_data['state'],
            xpl=filters.format_xpl(validated_data['xpl'] if validated_data.get('xpl') is not None else 'none'),
            zipcode=validated_data['zipcode'],
            schedule=validated_data['schedule']
        )

        return validated_data
