from rest_framework import views
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from client.fraud import models


class Search(views.APIView):
    permission_classes = (
        AllowAny,
    )

    @staticmethod
    def get(request, name, fraud_type):
        if fraud_type in ['address', 'email', 'ipaddress', 'phone']:
            obj = models.FraudString.objects.filter(
                name__iexact=name,
                fraud_type=fraud_type
            ).exists()

            return Response({'status': obj})

        if fraud_type == 'credit_card':
            for item in models.FraudString.objects.filter(fraud_type__exact='credit_card'):
                if item.decrypt_credit_card() == name:
                    return Response({'status': True})
                else:
                    return Response({'status': False})

        return Response({'status': False})
