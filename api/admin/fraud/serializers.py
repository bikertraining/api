import ipaddress
import re

import validators as python_validators
from rest_framework import serializers

from admin.fraud import models
from utils import security


class CreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FraudString

        fields = '__all__'

    def validate(self, attrs):
        # Address
        if attrs['fraud_type'] == 'address':
            if models.FraudString.objects.filter(
                    name__iexact=attrs['name'],
                    fraud_type='address'
            ).exists():
                raise serializers.ValidationError(
                    {
                        'name': 'Address already exists.'
                    },
                    code='exists'
                )

        # Credit Card
        if attrs['fraud_type'] == 'credit_card':
            for item in models.FraudString.objects.filter(fraud_type='credit_card'):
                if item.decrypt_credit_card() == attrs['name']:
                    raise serializers.ValidationError(
                        {
                            'name': 'Credit Card already exists.'
                        },
                        code='exists'
                    )

        # Email Address
        if attrs['fraud_type'] == 'email':
            if not python_validators.email(attrs['name']):
                raise serializers.ValidationError(
                    {
                        'name': 'Email address is not a valid format.'
                    },
                    code='malformed'
                )

            elif models.FraudString.objects.filter(
                    name__iexact=attrs['name'],
                    fraud_type='email'
            ).exists():
                raise serializers.ValidationError(
                    {
                        'name': 'Email address already exists.'
                    },
                    code='exists'
                )

        # IP Address
        if attrs['fraud_type'] == 'ipaddress':
            try:
                ipaddress.ip_address(attrs['name'])
            except ValueError:
                raise serializers.ValidationError(
                    {
                        'name': 'IP Address is not a valid format.'
                    },
                    code='malformed'
                )

            if models.FraudString.objects.filter(
                    name__iexact=attrs['name'],
                    fraud_type='ipaddress'
            ).exists():
                raise serializers.ValidationError(
                    {
                        'name': 'IP Address already exists.'
                    },
                    code='exists'
                )

        # Phone Number
        if attrs['fraud_type'] == 'phone':
            if not re.match('^[0-9]+$', attrs['name']):
                raise serializers.ValidationError(
                    {
                        'name': 'Phone number is not a valid format. Must only contain numbers.'
                    },
                    code='malformed'
                )

            elif models.FraudString.objects.filter(
                    name__iexact=attrs['name'],
                    fraud_type='phone'
            ).exists():
                raise serializers.ValidationError(
                    {
                        'name': 'Phone number already exists.'
                    },
                    code='exists'
                )

        return attrs

    def validate_name(self, value):
        if self.initial_data['fraud_type'] == 'credit_card':
            return security.encrypt_string(value)
        else:
            return value


class ProfileSerializer(serializers.ModelSerializer):
    fraud_type_name = serializers.CharField(
        read_only=True,
        source='get_fraud_type_display'
    )

    class Meta:
        model = models.FraudString

        fields = '__all__'

    def to_representation(self, instance):
        data = super(ProfileSerializer, self).to_representation(instance)

        if instance.fraud_type == 'credit_card':
            data.update({
                'name': instance.decrypt_credit_card()
            })

        return data

    def validate_name(self, value):
        if self.instance.fraud_type == 'credit_card':
            return security.encrypt_string(value)
        else:
            return value


class SearchSerializer(serializers.ModelSerializer):
    fraud_type_name = serializers.CharField(
        read_only=True,
        source='get_fraud_type_display'
    )

    class Meta:
        model = models.FraudString

        fields = '__all__'

    def to_representation(self, instance):
        data = super(SearchSerializer, self).to_representation(instance)

        if instance.fraud_type == 'credit_card':
            data.update({
                'name': instance.decrypt_credit_card()
            })

        return data
