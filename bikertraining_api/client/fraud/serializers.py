from rest_framework import serializers

from client.fraud import models


class SearchSerializer(serializers.ModelSerializer):
    fraud_type_name = serializers.CharField(
        read_only=True,
        source='get_fraud_type_display'
    )

    class Meta:
        model = models.FraudString

        fields = '__all__'

    def to_representation(self, instance):
        """
        Transforms the instance into a dictionary representation.

        Args:
            instance (obj): The instance to be transformed.

        Returns:
            dict: The dictionary representing the instance with encrypted fields decrypted.
        """

        data = super(SearchSerializer, self).to_representation(instance)

        if instance.fraud_type == 'credit_card':
            data.update({
                'name': instance.decrypt_credit_card()
            })

        return data
