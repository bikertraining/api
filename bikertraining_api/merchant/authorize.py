import json

import environ
import requests
from django.core.serializers.json import DjangoJSONEncoder

from utils import filters

env = environ.Env(
    MERCHANT_LOGIN_ID=(str, ''),
    MERCHANT_TEST_MODE=(bool, False),
    MERCHANT_TRANSACTION_KEY=(str, '')
)

environ.Env.read_env()


class Authorize(object):
    def __init__(self, data: dict):
        self.data = data

    def charge(self):
        """
        Charge

        :return: dict
        """

        formated_date = filters.format_date(self.data['schedule'].date_from, self.data['schedule'].date_to)

        request = {
            "createTransactionRequest": {
                "merchantAuthentication": {
                    "name": env('MERCHANT_LOGIN_ID'),
                    "transactionKey": env('MERCHANT_TRANSACTION_KEY')
                },
                "transactionRequest": {
                    "transactionType": 'authCaptureTransaction',
                    "amount": self.data['schedule'].price.amount,
                    "payment": {
                        "creditCard": {
                            "cardNumber": self.data['credit_card_number'],
                            "expirationDate": f"{self.data['credit_card_year']}-{self.data['credit_card_month']}",
                            "cardCode": self.data['credit_card_cvv2']
                        }
                    },
                    "lineItems": {
                        "lineItem": {
                            "itemId": self.data['schedule'].pk,
                            "name": self.data['schedule'].price.get_class_type_display(),
                            "description": f"{self.data['schedule'].get_day_type_display()} / {formated_date}",
                            "quantity": "1",
                            "unitPrice": self.data['schedule'].price.amount
                        }
                    },
                    "customer": {
                        "type": "individual",
                        "email": self.data['email']
                    },
                    "billTo": {
                        "firstName": self.data['first_name'],
                        "lastName": self.data['last_name'],
                        "address": self.data['address'],
                        "city": self.data['city'],
                        "state": self.data['state'],
                        "zip": self.data['zipcode'],
                        "country": "US",
                        "phoneNumber": self.data['phone']
                    },
                    "retail": {
                        "marketType": "2",
                        "deviceType": "8"
                    },
                    "transactionSettings": {
                        "setting": {
                            "settingName": "emailCustomer",
                            "settingValue": "true"
                        },
                        "setting": {
                            "settingName": "duplicateWindow",
                            "settingValue": "0"
                        }
                    },
                    "userFields": {
                        "userField": [
                            {
                                "name": "Class",
                                "value": self.data['schedule'].price.get_class_type_display()
                            },
                            {
                                "name": "Schedule",
                                "value": f"{self.data['schedule'].get_day_type_display()} / {formated_date}"
                            },
                            {
                                "name": "Total",
                                "value": self.data['schedule'].price.amount
                            },
                            {
                                "name": "Student Name",
                                "value": f"{self.data['first_name']} {self.data['last_name']}"
                            }
                        ]
                    },
                    "authorizationIndicatorType": {
                        "authorizationIndicator": "final"
                    }
                }
            }
        }

        return self.get_response('post', request)

    def get_response(self, method: str, request: dict):
        """
        Response

        :param str method: get, post
        :param dict request: data

        :return: dict | None
        """

        if method == 'post':
            response = requests.post(
                self.get_url(),
                data=json.dumps(
                    request,
                    cls=DjangoJSONEncoder
                )
            )

            result = json.loads(response.content)

            # Something bad happened
            if result.get('messages') is not None and result.get('messages').get('resultCode') == 'Error':
                return {
                    'error': True,
                    'message': result['messages']['message'][0]['text']
                }

            # Probably declined
            elif result.get('transactionResponse').get('errors') is not None:
                return {
                    'error': True,
                    'message': result['transactionResponse']['errors'][0]['errorText']
                }

            # Transaction OK
            else:
                return {
                    'error': False,
                    'result': result
                }

        else:
            return None

    @staticmethod
    def get_url():
        """
        End point URL

        :return: str
        """

        if env('MERCHANT_TEST_MODE'):
            return 'https://apitest.authorize.net/xml/v1/request.api'
        else:
            return 'https://api.authorize.net/xml/v1/request.api'
