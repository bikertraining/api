from django.core.mail import mail_managers
from django.template import loader
from rest_framework import serializers

from client.contact import models


class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contact

        fields = '__all__'


class SendEmailSerializer(serializers.Serializer):
    can_email = serializers.BooleanField(
        required=False
    )

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
        validated_can_email = validated_data['can_email']

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

        # Email managers
        mail_managers(
            subject='New submission from Contact Us',
            html_message=html_message,
            message=None
        )

        # Subscribe to newsletter
        if validated_can_email and not models.Contact.objects.filter(email=validated_email).exists():
            models.Contact.objects.create(
                email=validated_email,
                name=validated_name
            )

        return validated_data
