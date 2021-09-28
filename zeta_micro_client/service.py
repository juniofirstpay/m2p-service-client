import requests
from urllib.parse import urljoin
from typing import List, Dict, Tuple, Optional

from requests.models import Response


class ZetaService(object):

    base_url_create_account_holder = '/account-holder/create'
    base_url_get_account_holder = '/account-holder/{account_holder_id}'
    base_url_get_account_holder_type = '/account-holder/vector/{type}/{value}'

    base_url_get_accounts = 'account/account-holder/{account_holder_id}'
    base_url_get_resources = '/account-holder/{account_holder_id}/resources'

    base_url_create_account = '/account/create'
    base_url_get_account = '/account/{account_id}/details'

    base_url_get_account_balance = '/account/{account_id}/balance'
    base_url_get_account_holder_balance = '/account/account-holder/{account_holder_id}/balance'
    base_url_get_account_holder_token = '/account-holder/{account_holder_id}/token'

    base_url_create_resource = 'account/payment-instrument/create'
    base_url_get_resource = 'account/payment-instrument/{resource_id}'
    base_url_resource_id_status = 'account/payment-instrument/{resource_id}/status'
    base_url_resource_id_delete = 'account/payment-instrument/{resource_id}/delete'

    base_url_form_factor_id = '/payment-instrument/{resource_id}/form-factors/{form_factor_id}'

    base_url_update_account = '/account/{account_id}/update'

    base_url_account_debit = "/transactions/debit"
    base_url_account_credit = "/transactions/credit"
    base_url_account_intra_transfer = "/transactions/intra-transfer"
    base_url_txn_reversal = "/transactions/{txn_id}/reversal"

    base_url_create_phone_number = "/account/{account_id}/payment-instrument/phone-number/create"
    base_url_delete_phone_number = "/account/{account_id}/payment-instrument/phone-number/delete"

    base_url_get_txns = "/card/resource/{resource_id}/transactions"

    def __init__(self, endpoint: str, client_id: str, client_secret: str, api_key: str):
        self.base_url = endpoint
        self.client_id = client_id
        self.client_secret = client_secret
        self.api_key = api_key
        self.base_headers = {
            'ClientId': self.client_id,
            'ClientSecret': self.client_secret,
            'X-Api-Key': self.api_key
        }

    def open(self):
        self.request = requests.Session()
        self.request.headers.update(self.base_headers)
        return self

    def close(self):
        self.request.close()
        self.request = None

    def process_response(sef, response: Response):
        if response.status_code == 200:
            return (None, response.json())
        else:
            try:
                return (response.status_code, response.json())
            except:
                return (response.status_code, response.text)

    def create_account_holder(self, *args, **kwargs):
        response = self.request.post(
            url=urljoin(self.base_url,
                        self.base_url_create_account_holder),
            headers=self.base_headers,
            json=kwargs
        )
        return self.process_response(response)

    def get_account_holder(self, type, value):
        response = self.request.get(
            url=urljoin(self.base_url,
                        self.base_url_get_account_holder_type.format(type=type, value=value)),
            headers=self.base_headers
        )
        return self.process_response(response)

    def get_accounts(self, account_holder_id: str) -> List[Dict]:
        response = self.request.get(
            url=urljoin(self.base_url,
                        self.base_url_get_accounts.format(account_holder_id=account_holder_id)),
            headers=self.base_headers
        )
        return self.process_response(response)

    def get_account(self, account_id: str) -> List[Dict]:
        response = self.request.get(
            url=urljoin(self.base_url,
                        self.base_url_get_account.format(account_id=account_id)),
            headers=self.base_headers
        )
        return self.process_response(response)

    # Make the
    def create_account(self, *args, **kwargs) -> Dict:
        response = self.request.post(
            url=urljoin(self.base_url,
                        self.base_url_create_account),
            headers=self.base_headers,
            json=kwargs
        )
        return self.process_response(response)

    def get_resources(self, account_holder_id: str, *args, **kwargs) -> List[Dict]:
        response = self.request.post(
            url=urljoin(self.base_url,
                        self.base_url_get_resources.format(account_holder_id=account_holder_id)),
            headers=self.base_headers
        )
        return self.process_response(response)

    def get_resource(self, resource_id: str, *args, **kwargs) -> Tuple[Optional[int], Dict]:
        response = self.request.get(
            url=urljoin(self.base_url, self.base_url_get_resource.format(
                resource_id=resource_id)),
            headers=self.base_headers
        )
        return self.process_response(response)

    def create_resource(self, *args, **kwargs) -> Dict:
        response = self.request.post(
            url=urljoin(self.base_url,
                        self.base_url_create_resource),
            headers=self.base_headers,
            json=kwargs
        )
        return self.process_response(response)

    # def get_resource(self, resource_id: str, *args, **kwargs) -> Dict:
    #     response = self.request.get(
    #         url=urljoin(self.base_url,
    #                     self.base_url_get_resource.format(resource_id=resource_id)),
    #         headers=self.base_headers
    #     )
    #     if response.status_code == 200:
    #         return (None, response.json())
    #     else:
    #         return (response.status_code, response.json())

    def update_resource_status(self, resource_id: str, *args, **kwargs) -> Dict:
        response = self.request.post(
            url=urljoin(self.base_url,
                        self.base_url_resource_id_status.format(resource_id=resource_id)),
            headers=self.base_headers,
            json=kwargs
        )
        return self.process_response(response)

    def delete_resource_status(self, resource_id: str, *args, **kwargs) -> Dict:
        response = self.request.post(
            url=urljoin(self.base_url,
                        self.base_url_resource_id_delete.format(resource_id=resource_id)),
            headers=self.base_headers,
            json=kwargs
        )
        return self.process_response(response)

    def update_form_factor(self,
                           resource_id: str,
                           form_factor_id: str,
                           **kwargs) -> Dict:
        response = self.request.put(
            url=urljoin(self.base_url,
                        self.base_url_form_factor_id.format(resource_id=resource_id,
                                                            form_factor_id=form_factor_id)),
            headers=self.base_headers,
            json=kwargs
        )
        return self.process_response(response)

    def update_account(self,
                       account_id: str,
                       **kwargs) -> Dict:
        response = self.request.post(url=urljoin(self.base_url,
                                                 self.base_url_update_account.format(account_id=account_id)),
                                     headers=self.base_headers,
                                     json=kwargs)
        return self.process_response(response)

    def account_debit(self, **kwargs) -> Dict:
        response = self.request.post(url=urljoin(self.base_url, self.base_url_account_debit),
                                     headers=self.base_headers,
                                     json=kwargs)
        return self.process_response(response)

    def account_credit(self, **kwargs) -> Dict:
        response = self.request.post(url=urljoin(self.base_url,
                                                 self.base_url_account_credit),
                                     headers=self.base_headers,
                                     json=kwargs)
        return self.process_response(response)

    def account_transfer(self, **kwargs) -> Dict:
        response = self.request.post(url=urljoin(self.base_url,
                                                 self.base_url_account_intra_transfer),
                                     headers=self.base_headers,
                                     json=kwargs)
        return self.process_response(response)

    def reverse_txn(self, **kwargs) -> Tuple[Optional[int], Dict]:
        response = self.request.post(url=urljoin(self.base_url,
                                                 self.base_url_txn_reversal.format(txn_id=kwargs.get('txn_id'))),
                                     headers=self.base_headers)
        return self.process_response(response)

    def get_balance(self, **kwargs) -> Tuple[Optional[int], Dict]:
        response = self.request.get(url=urljoin(self.base_url,
                                                self.base_url_get_account_balance.format(account_id=kwargs.get('account_id'))),
                                    headers=self.base_headers)
        return self.process_response(response)

    def get_balance_accounts(self, **kwargs) -> Tuple[Optional[int], Dict]:
        response = self.request.post(url=urljoin(self.base_url,
                                                 self.base_url_get_account_holder_balance.format(account_holder_id=kwargs.get('account_holder_id'))),
                                     headers=self.base_headers)
        return self.process_response(response)

    def get_account_holder_token(self, **kwargs) -> Tuple[Optional[int], Dict]:
        response = self.request.get(url=urljoin(self.base_url, self.base_url_get_account_holder_token.format(
            account_holder_id=kwargs.get("account_holder_id"))))
        return self.process_response(response)

    def fetch_resource_transactions(self, **kwargs) -> Tuple[Optional[int], Dict]:
        response = self.request.get(url=urljoin(self.base_url,
                                                self.base_url_get_txns.format(resource_id=kwargs.get("resource_id"))))

        return self.process_response(response)

    def create_phone_number(self, account_id, phone_number) -> Tuple[Optional[int], Dict]:
        req_body = {
            "phone_number": phone_number
        }
        response = self.request.post(
            url=urljoin(
                self.base_url,
                self.base_url_create_phone_number.format(account_holder_id=account_id)
            ),
            json=req_body,
            headers=self.base_headers)
        return self.process_response(response)

    def delete_phone_number(self, account_id) -> Tuple[Optional[int], Dict]:
        req_body = {}
        response = self.request.post(
            url=urljoin(
                self.base_url,
                self.base_url_delete_phone_number.format(account_holder_id=account_id)
            ),
            json=req_body,
            headers=self.base_headers)
        return self.process_response(response)
