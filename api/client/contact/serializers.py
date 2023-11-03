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
        # Compose HTML Message
        html_message = loader.render_to_string(
            'contact.html',
            {
                'email': validated_data['email'],
                'message': validated_data['message'],
                'name': validated_data['name'],
                'phone': validated_data['phone'] if validated_data.get('phone') is not None else ''
            }
        )

        # Email Managers
        mail_managers(
            subject='New submission from Contact Us',
            message=None,
            fail_silently=False,
            html_message=html_message
        )

        # Subscribe to newsletter
        if validated_data['can_email'] and not models.Contact.objects.filter(email=validated_data['email']).exists():
            models.Contact.objects.create(
                email=validated_data['email'],
                name=validated_data['name']
            )

        return validated_data
