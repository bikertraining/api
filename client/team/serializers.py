from django.core.mail import mail_managers
from django.template import loader
from rest_framework import serializers


class SendEmailSerializer(serializers.Serializer):
    email = serializers.CharField(
        required=True
    )

    message1 = serializers.CharField(
        required=True
    )

    message2 = serializers.CharField(
        required=True
    )

    message3 = serializers.CharField(
        required=True
    )

    message4 = serializers.CharField(
        required=True
    )

    message5 = serializers.CharField(
        required=True
    )

    message6 = serializers.CharField(
        required=True
    )

    message7 = serializers.CharField(
        required=True
    )

    name = serializers.CharField(
        required=True
    )

    phone = serializers.CharField(
        required=True
    )

    def create(self, validated_data):
        # Compose HTML Message
        html_message = loader.render_to_string(
            'team.html',
            {
                'email': validated_data['email'],
                'message1': validated_data['message1'],
                'message2': validated_data['message2'],
                'message3': validated_data['message3'],
                'message4': validated_data['message4'],
                'message5': validated_data['message5'],
                'message6': validated_data['message6'],
                'message7': validated_data['message7'],
                'name': validated_data['name'],
                'phone': validated_data['phone']
            }
        )

        # Email Managers
        mail_managers(
            subject='Interested in joining your team',
            message=None,
            fail_silently=False,
            html_message=html_message
        )

        return validated_data
