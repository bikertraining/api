from django.core.mail import mail_managers
from django.template import loader
from rest_framework import serializers


class SendEmailSerializer(serializers.Serializer):
    email = serializers.CharField(
        required=True
    )

    message = serializers.CharField(
        required=True
    )

    name = serializers.CharField(
        required=True
    )

    phone = serializers.CharField(
        allow_blank=True,
        allow_null=True,
        required=False
    )

    def create(self, validated_data):
        validated_email = validated_data['email']

        validated_message = validated_data['message']

        validated_name = validated_data['name']

        validated_phone = validated_data['phone'] if validated_data.get('phone') is not None else ''

        html_message = loader.render_to_string(
            'contact.html',
            {
                'email': validated_email,
                'message': validated_message,
                'name': validated_name,
                'phone': validated_phone
            }
        )

        mail_managers(
            subject='New submission from Contact Us',
            html_message=html_message,
            message=None
        )

        return validated_data
