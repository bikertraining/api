from rest_framework import serializers

from client.price import models


class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Price

        fields = '__all__'
