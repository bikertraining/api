from rest_framework import views
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from client.fraud import models


class Search(views.APIView):
    """
    The `Search` class is an API view that allows searching for fraud strings.
    It extends the `APIView` class from the `rest_framework.views` module.

    Attributes:
    - `permission_classes` (tuple): A tuple containing the permission classes applied to the view.
                                    In this case, it contains a single class, `AllowAny`, which allows any user to access the API.

    Methods:
    - `get(self, request, name, fraud_type)`: This method handles the GET request to the API endpoint.
                                              It takes two parameters, `name` and `fraud_type`, which are used to search for fraud strings.

      - If the `fraud_type` parameter is one of ['address', 'email', 'ipaddress', 'phone'], it filters the `FraudString` model for an exact match of `name` and `fraud_type`, and checks if any entries exist.
        The result is returned as a `Response` object.

      - If the `fraud_type` parameter is 'credit_card', it iterates over the `FraudString` entries with fraud type 'credit_card' and checks if the decrypted credit card value matches `name`.
        If a match is found, it returns `True` as a `Response` object. Otherwise, it returns `False` as a `Response` object.

      - If none of the conditionals are met, it returns `False` as a `Response` object.

    """

    permission_classes = (
        AllowAny,
    )

    def get(self, request, name, fraud_type):
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
