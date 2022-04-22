import json

import environ
import requests

from utils import filters

env = environ.Env(
    MERCHANT_LOGIN_ID=(str, ''),
    MERCHANT_TEST_MODE=(bool, False),
    MERCHANT_TRANSACTION_KEY=(str, '')
)

environ.Env.read_env()


class Eprocessing(object):
    def __init__(self, data: dict):
        self.data = data

    def charge(self):
        """
        Charge

        :return: dict
        """

        class_type = self.data['schedule'].price.get_class_type_display()

        day_type = self.data['schedule'].get_day_type_display()

        formated_date = filters.format_date(self.data['schedule'].date_from, self.data['schedule'].date_to)

        if env('MERCHANT_TEST_MODE'):
            merchant_login_id = env('MERCHANT_LOGIN_ID_TEST')

            merchant_transaction_key = env('MERCHANT_TRANSACTION_KEY_TEST')
        else:
            merchant_login_id = env('MERCHANT_LOGIN_ID_LIVE')

            merchant_transaction_key = env('MERCHANT_TRANSACTION_KEY_LIVE')

        request = {
            "ePNAccount": merchant_login_id,
            "RestrictKey": merchant_transaction_key,
            "RequestType": "transaction",
            "TranType": "Sale",
            "Total": f"{self.data['schedule'].price.amount}",
            "Address": self.data['address'],
            "Zip": self.data['zipcode'],
            "CardNo": self.data['credit_card_number'],
            "ExpMonth": self.data['credit_card_month'],
            "ExpYear": self.data['credit_card_year'][-2:],
            "CVV2Type": "1",
            "CVV2": self.data['credit_card_cvv2'],
            "FirstName": self.data['first_name'],
            "LastName": self.data['last_name'],
            "Phone": self.data['phone'],
            "Email": self.data['email'],
            "City": self.data['city'],
            "State": self.data['state'],
            "Description": f"{class_type} - {day_type} / {formated_date}"
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
                json=request
            )

            result = json.loads(response.content)

            # Probably declined
            if result['Success'].lower() != 'y':
                if result.get('RespText') is not None:
                    message = result['RespText']
                elif result.get('AVSText') is not None:
                    message = result['AVSText']
                elif result.get('CVV2Text') is not None:
                    message = result['CVV2Text']
                else:
                    message = 'Unknown error, please call and lets figure this out.'

                return {
                    'error': True,
                    'message': message
                }

            # Transaction OK
            else:
                return {
                    'error': False,
                    'result': result
                }

    @staticmethod
    def get_url():
        """
        End point URL

        :return: str
        """

        if env('MERCHANT_TEST_MODE'):
            return 'https://www.eprocessingnetwork.com/cgi-bin/epn/secure/tdbe/transact.pl'
        else:
            return 'https://www.eprocessingnetwork.com/cgi-bin/epn/secure/tdbe/transact.pl'

    def payment(self):
        """
        Payment

        :return: dict
        """

        if env('MERCHANT_TEST_MODE'):
            merchant_login_id = env('MERCHANT_LOGIN_ID_TEST')

            merchant_transaction_key = env('MERCHANT_TRANSACTION_KEY_TEST')
        else:
            merchant_login_id = env('MERCHANT_LOGIN_ID_LIVE')

            merchant_transaction_key = env('MERCHANT_TRANSACTION_KEY_LIVE')

        request = {
            "ePNAccount": merchant_login_id,
            "RestrictKey": merchant_transaction_key,
            "RequestType": "transaction",
            "TranType": "Sale",
            "Total": f"{self.data['amount']}",
            "Address": self.data['address'],
            "Zip": self.data['zipcode'],
            "CardNo": self.data['credit_card_number'],
            "ExpMonth": self.data['credit_card_month'],
            "ExpYear": self.data['credit_card_year'][-2:],
            "CVV2Type": "1",
            "CVV2": self.data['credit_card_cvv2'],
            "FirstName": self.data['first_name'],
            "LastName": self.data['last_name'],
            "Phone": self.data['phone'],
            "Email": self.data['email'],
            "City": self.data['city'],
            "State": self.data['state'],
            "Description": f"Student Payment for {self.data['first_name']} {self.data['last_name']}"
        }

        return self.get_response('post', request)
