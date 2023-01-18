import requests
from urllib.parse import urljoin
from typing import List, Dict, Tuple, Optional, Union

import urllib
from requests.models import Response


class ZetaService(object):

    base_url_create_account_holder = 'account-holder/create'
    base_url_get_account_holder = 'account-holder/{account_holder_id}'
    base_url_get_account_holder_type = 'account-holder/vector/{type}/{value}'
    base_url_account_holder_otp_action = 'account-holder/otp'

    base_url_get_accounts = 'account/account-holder/{account_holder_id}'
    base_url_get_resources = 'account-holder/{account_holder_id}/resources'

    base_url_create_account = 'account/create'
    base_url_get_account = 'account/{account_id}/details'

    base_url_get_account_balance = 'account/{account_id}/balance'
    base_url_get_account_balance_job = 'account/{account_id}/balance/job'
    base_url_get_funding_account_balance = 'account/funding/balance'
    base_url_get_account_credit_limit = 'account/{account_id}/credit-limit'
    base_url_get_account_credit_limit_job = 'account/{account_id}/credit-limit/job'
    base_url_get_account_debit_limit = 'account/{account_id}/debit-limit'
    base_url_get_account_holder_balance = 'account/account-holder/{account_holder_id}/balance'
    base_url_get_account_holder_token = 'account-holder/{account_holder_id}/token'

    base_url_create_resource = 'account/payment-instrument/create'
    base_url_get_resource = 'account/payment-instrument/{resource_id}'
    base_url_resource_id_status = 'account/payment-instrument/{resource_id}/status'
    base_url_resource_id_delete = 'account/payment-instrument/{resource_id}/delete'
    base_url_account_transactions = "v2/account/{account_id}/transactions"

    base_url_get_resource_via_account_id = "account/{account_id}/payment-instrument"

    base_url_form_factor_id = 'payment-instrument/{resource_id}/form-factors/{form_factor_id}'

    base_url_update_account = 'account/{account_id}/update'

    base_url_account_debit = "transactions/debit"
    base_url_account_credit = "transactions/credit"
    base_url_account_intra_transfer = "transactions/intra-transfer"
    base_url_txn_reversal = "transactions/{txn_id}/reversal"
    base_url_txn_get = "transactions/{txn_id}/details"

    base_url_create_phone_number = "account/{account_id}/payment-instrument/phone-number/create"
    base_url_delete_phone_number = "account/{account_id}/payment-instrument/phone-number/delete"

    base_url_create_card = "account/{account_id}/payment-instrument/card/create"
    base_url_delete_card = "account/{account_id}/payment-instrument/card/delete"

    base_url_get_card = "card/{card_id}/resource"
    base_url_get_card_status = "card/{card_id}/status"
    base_url_update_card_status = "card/{card_id}/status"
    base_url_get_card_view = "card/view"
    base_url_get_card_set_pin = "card/set-pin"

    base_url_get_txns = "card/resource/{resource_id}/transactions"

    base_url_fetch_txn_limit = "accounts/{account_id}/fetch-limit"

    base_url_person_account_holder = "person/{person_id}/account-holder"
    base_url_person_account_holder_job = "person/{person_id}/account-holder/job"
    base_url_person_account = "person/{person_id}/account"
    base_url_person_account_details = "person/{person_id}/account/details"
    base_url_person_account_job = "person/{person_id}/account/job"
    base_url_person_bundle = "person/{person_id}/bundle"
    base_url_person_bundle_job = "person/{person_id}/bundle/job"
    base_url_person_account_transactions = "person/{person_id}/transactions"
    base_url_person_payment_instrument_addon = "person/{person_id}/payment-instrument/add"
    base_url_person_payment_instrument_dummy_swap = "person/{person_id}/payment-instrument/dummy-swap"

    base_url_workflow_create_card_dispatch = "workflow/dispatch/card/create"
    base_url_workflow_find_card_dispatch = "workflow/dispatch/card/find"
    base_url_workflow_get_card_dispatch = "workflow/dispatch/card/{card_dispatch_id}"
    base_url_workflow_get_card_dispatch_edit_action = "workflow/dispatch/card/{card_dispatch_id}/edit/action"
    base_url_workflow_check_zipcode = "workflow/dispatch/zipcode/status"

    base_url_create_txn_policy = "policy/{account_holder_id}/{card_id}/create"
    base_url_get_txn_policy = "policy/get/{card_id}"
    base_url_update_txn_policy = "policy/update/{card_id}"

    base_url_card_policy = "card/policy"
    base_url_product_inventory = "audit/payment-instrument/inventory"


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

    def get_account_holder_via_id(self, ach_id: str):
        response = self.request.get(
            url=urljoin(self.base_url,
                        self.base_url_get_account_holder.format(account_holder_id=ach_id)),
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

    def get_resource_via_account_id(self, account_id: str, *args, **kwargs) -> Tuple[Optional[int], Dict]:
        response = self.request.get(
            url=urljoin(self.base_url, self.base_url_get_resource_via_account_id.format(
                account_id=account_id)),
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
    
    def get_txn(self, **kwargs) -> Tuple[Optional[int], Dict]:
        response = self.request.get(url=urljoin(self.base_url,
                                                 self.base_url_txn_get.format(txn_id=kwargs.get('txn_id'))),
                                     headers=self.base_headers)
        return self.process_response(response)

    def get_balance(self, **kwargs) -> Tuple[Optional[int], Dict]:
        response = self.request.get(url=urljoin(self.base_url,
                                                self.base_url_get_account_balance.format(account_id=kwargs.get('account_id'))),
                                    headers=self.base_headers)
        return self.process_response(response)
    
    def get_balance_job(self, params: Optional[Dict] = None, **kwargs) -> Tuple[Optional[int], Dict]:
        response = self.request.get(url=urljoin(self.base_url,
                                                self.base_url_get_account_balance_job.format(account_id=kwargs.get('account_id'))),
                                    headers=self.base_headers,
                                    params=params)
        return self.process_response(response)
    
    def get_funding_account_balance(self) -> "Tuple[Optional[int], Dict]":
        response = self.request.get(url=urljoin(self.base_url, self.base_url_get_funding_account_balance),
                                    headers=self.base_headers)
        return response
    
    def get_credit_limit(self, **kwargs) -> Tuple[Optional[int], Dict]:
        response = self.request.get(url=urljoin(self.base_url,
                                                self.base_url_get_account_credit_limit.format(account_id=kwargs.get('account_id'))),
                                    headers={**self.base_headers, 'X-API-VERSION': 'v1'})
        return self.process_response(response)
    
    def get_credit_limit_job(self, params: Optional[Dict] = None, **kwargs) -> Tuple[Optional[int], Dict]:
        response = self.request.get(url=urljoin(self.base_url,
                                                self.base_url_get_account_credit_limit_job.format(account_id=kwargs.get('account_id'))),
                                    headers={**self.base_headers, 'X-API-VERSION': 'v1'},
                                    params=params)
        return self.process_response(response)
    
    def get_debit_limit(self, **kwargs) -> Tuple[Optional[int], Dict]:
        response = self.request.get(url=urljoin(self.base_url,
                                                self.base_url_get_account_debit_limit.format(account_id=kwargs.get('account_id'))),
                                    headers={**self.base_headers, 'X-API-VERSION': 'v1'})
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
                self.base_url_create_phone_number.format(
                    account_holder_id=account_id)
            ),
            json=req_body,
            headers=self.base_headers)
        return self.process_response(response)

    def delete_phone_number(self, account_id) -> Tuple[Optional[int], Dict]:
        req_body = {}
        response = self.request.post(
            url=urljoin(
                self.base_url,
                self.base_url_delete_phone_number.format(
                    account_holder_id=account_id)
            ),
            json=req_body,
            headers=self.base_headers)
        return self.process_response(response)

    def get_account_transactions(self, account_id: str, params: Optional[Dict] = None) -> Tuple[Optional[int], Union[List, Dict]]:
        response = self.request.get(
            url=urljoin(
                self.base_url,
                self.base_url_account_transactions.format(
                    account_id=account_id)
            ),
            headers=self.base_headers,
            params=params
        )
        return self.process_response(response)

    def get_account_transactions_v2(self, account_id: str, params: Optional[Dict] = None) -> Tuple[Optional[int], Union[List, Dict]]:
        url = urljoin(
            self.base_url,
            self.base_url_account_transactions.format(
                account_id=account_id)
        )
        if params:
            url = url + "?" + urllib.parse.urlencode(params)
        response = self.request.get(
            url=url,
            headers=self.base_headers,
        )
        return self.process_response(response)

    def get_person_account_transactions(self, person_id: str, params: Optional[Dict] = None) -> Tuple[Optional[int], Union[List, Dict]]:
        url = urljoin(
            self.base_url,
            self.base_url_person_account_transactions.format(person_id=person_id)
        )
        if params:
            url = url + "?" + urllib.parse.urlencode(params)
        response = self.request.get(
            url=url,
            headers=self.base_headers,
        )
        return self.process_response(response)

    def create_card(self, account_id) -> Tuple[Optional[int], Dict]:
        response = self.request.post(
            url=urljoin(
                self.base_url,
                self.base_url_create_card.format(account_id=account_id)
            ),
            json={},
            headers=self.base_headers)
        return self.process_response(response)

    def delete_card(self, account_id) -> Tuple[Optional[int], Dict]:
        req_body = {}
        response = self.request.post(
            url=urljoin(
                self.base_url,
                self.base_url_delete_card.format(account_id=account_id)
            ),
            json=req_body,
            headers=self.base_headers)
        return self.process_response(response)

    def get_card(self, card_id: str) -> Tuple[Optional[int], Dict]:
        response = self.request.get(
            url=urljoin(
                self.base_url,
                self.base_url_get_card.format(card_id=card_id)
            ),
            headers=self.base_headers)
        return self.process_response(response)
    
    def get_card_view(self, card_id: str) -> Tuple[Optional[int], Dict]:
        response = self.request.get(
            url=urljoin(
                self.base_url,
                self.base_url_get_card.format(card_id=card_id)
            ),
            headers=self.base_headers)
        return self.process_response(response)
    
    def get_card_view(self, card_id: str) -> Tuple[Optional[int], Dict]:
        response = self.request.get(
            url=urljoin(
                self.base_url,
                self.base_url_get_card_view + "?card_id={card_id}".format(card_id=card_id)
            ),
            headers=self.base_headers)
        return self.process_response(response)
    
    def get_card_set_pin(self, card_id: str) -> Tuple[Optional[int], Dict]:
        response = self.request.get(
            url=urljoin(
                self.base_url,
                self.base_url_get_card_set_pin + "?card_id={card_id}".format(card_id=card_id)
            ),
            headers=self.base_headers)
        return self.process_response(response)

    def get_card_status(self, card_id) -> Tuple[Optional[int], Dict]:
        response = self.request.get(
            url=urljoin(
                self.base_url,
                self.base_url_get_card_status.format(card_id=card_id)
            ),
            headers=self.base_headers)
        return self.process_response(response)

    def update_card_status(self, card_id, status) -> Tuple[Optional[int], Dict]:
        req_body = {
            "card_status": status
        }
        response = self.request.post(
            url=urljoin(
                self.base_url,
                self.base_url_update_card_status.format(card_id=card_id)
            ),
            json=req_body,
            headers=self.base_headers)
        return self.process_response(response)

    def fetch_txn_limit(self, account_id: str) -> Tuple[Optional[int], Dict]:
        response = self.request.get(
            url=urljoin(
                self.base_url,
                self.base_url_fetch_txn_limit.format(account_id=account_id)
            ),
            headers=self.base_headers
        )
        return self.process_response(response)

    def get_person_account_holder(self, person_id: "UUID"):
        response = self.request.get(
            url=urljoin(self.base_url, self.base_url_person_account_holder.format(
                person_id=person_id)),
            headers=self.base_headers
        )
        return self.process_response(response)

    def get_person_account(self, person_id: "UUID"):
        response = self.request.get(
            url=urljoin(self.base_url, self.base_url_person_account.format(
                person_id=person_id)),
            headers=self.base_headers
        )
        return self.process_response(response)

    def get_person_account_details(self, person_id: "UUID", account_id: str = None):
        response = self.request.get(
            url=urljoin(self.base_url, self.base_url_person_account_details.format(
                person_id=person_id)),
            params={'account_id': account_id},
            headers=self.base_headers
        )
        return self.process_response(response)

    def get_person_bundle(self, person_id: "UUID"):
        response = self.request.get(
            url=urljoin(self.base_url, self.base_url_person_bundle.format(
                person_id=person_id)),
            headers=self.base_headers
        )
        return self.process_response(response)

    def get_person_account_holder_job(self, person_id: "UUID"):
        response = self.request.get(
            url=urljoin(self.base_url, self.base_url_person_account_holder_job.format(
                person_id=person_id)),
            headers=self.base_headers
        )
        return self.process_response(response)

    def get_person_account_job(self, person_id: "UUID"):
        response = self.request.get(
            url=urljoin(self.base_url, self.base_url_person_account_job.format(
                person_id=person_id)),
            headers=self.base_headers
        )
        return self.process_response(response)

    def get_person_bundle_job(self, person_id: "UUID"):
        response = self.request.get(
            url=urljoin(self.base_url, self.base_url_person_bundle_job.format(
                person_id=person_id)),
            headers=self.base_headers
        )
        return self.process_response(response)

    def create_person_account_holder_job(self, person_id: "UUID" = None, **data: dict):
        response = self.request.post(
            url=urljoin(self.base_url, self.base_url_person_account_holder_job.format(
                person_id=person_id)),
            headers=self.base_headers,
            json={"attributes": {
                "kyc": {
                    **data,
                    "dob": data.get('dob').strftime('%Y-%m-%d')
                },
                "proxy": {
                    "account_holder_id": data.get('proxy_ach')
                }
            }}
        )
        return self.process_response(response)

    def create_person_account_job(self, person_id: "UUID" = None, **data: dict):
        response = self.request.post(
            url=urljoin(self.base_url, self.base_url_person_account_job.format(
                person_id=person_id)),
            headers=self.base_headers,
            json={"attributes": {
                "account_holder_id": data.get("account_holder_id"),
                "account": {
                    "name": data.get("name"),
                }
            }}
        )
        return self.process_response(response)

    def create_person_bundle_job(self, person_id: "UUID" = None, **data: dict):
        response = self.request.post(
            url=urljoin(self.base_url, self.base_url_person_bundle_job.format(
                person_id=person_id)),
            headers=self.base_headers,
            json={
                "attributes": {
                    "account_holder_id": data.get("account_holder_id"),
                    "account": {
                        "name": data.get("name"),
                        "account_id": data.get("account_id")
                    },
                    "payment_instrument": {
                        "mobile_number": data.get("mobile_number"),
                    },
                    "session_id": data.get("session_id"),
                    "session_date": data.get("session_date")
                }
            }
        )
        return self.process_response(response)

    def create_person_payment_instrument_addon(self, person_id: "UUID" = None, payment_instrument_product_code: "str"=None, request_ref_id: "str"=None):
        response = self.request.post(
            url=urljoin(self.base_url, self.base_url_person_payment_instrument_addon.format(person_id=person_id)),
            headers=self.base_headers,
            json={
                "payment_instrument_product_code": payment_instrument_product_code,
                "request_ref_id": request_ref_id
            }
        )
        return self.process_response(response)
    
    def create_card_dispatch(self, **data: dict):
        request = self.request.post(
            url=urljoin(self.base_url, self.base_url_workflow_create_card_dispatch),
            headers=self.base_headers,
            json=data
        )
        return self.process_response(request)
    
    def find_card_dispatch(self, **params: dict):
        request = self.request.get(
            url=urljoin(self.base_url, self.base_url_workflow_find_card_dispatch),
            headers=self.base_headers,
            params=params
        )
        return self.process_response(request)
    
    def get_card_dispatch(self, card_dispatch_id: str):
        request = self.request.get(
            url=urljoin(self.base_url,
                        self.base_url_workflow_get_card_dispatch.format(card_dispatch_id=card_dispatch_id)),
            headers=self.base_headers
        )
        return self.process_response(request)
    
    def check_zipcode(self, params):
        request = self.request.get(
            url=urljoin(self.base_url,
                        self.base_url_workflow_check_zipcode),
            headers={**self.base_headers, 'X-Api-Version': 'v1' },
            params=params
        )
        return self.process_response(request)

    def create_txn_policy(self, account_holder_id, card_id, txn_policy_rules):
        base_url_create_txn_policy = self.base_url_create_txn_policy.format(
            account_holder_id=account_holder_id,
            card_id=card_id
        )
        response = self.request.post(
            url=urljoin(self.base_url,
                        base_url_create_txn_policy),
            headers=self.base_headers,
            json=txn_policy_rules
        )
        return self.process_response(response)

    def get_txn_policy(self, card_id):
        base_url_get_txn_policy = self.base_url_get_txn_policy.format(
            card_id=card_id)
        response = self.request.get(
            url=urljoin(self.base_url,
                        base_url_get_txn_policy),
            headers=self.base_headers
        )
        return self.process_response(response)

    def update_txn_policy(self, card_id, txn_policy_list):
        base_url_update_txn_policy = self.base_url_update_txn_policy.format(
            card_id=card_id)
        response = self.request.post(
            url=urljoin(self.base_url,
                        base_url_update_txn_policy),
            headers=self.base_headers,
            json=txn_policy_list
        )
        return self.process_response(response)


    def get_card_policy(self, card_id, account_holder_id):
        base_url = self.base_url_card_policy
        response = self.request.get(
            url=urljoin(self.base_url, base_url),
            headers=self.base_headers,
            params={
                'card_id': card_id,
                'account_holder_id': account_holder_id
            }
        )
        return self.process_response(response)
    
    def set_card_policy(self, card_id, account_holder_id, rules):
        base_url = self.base_url_card_policy
        response = self.request.post(
            url=urljoin(self.base_url, base_url),
            headers={**self.base_headers, 'X-API-VERSION': 'v1' },
            json={
                'card_id': card_id,
                'account_holder_id': account_holder_id,
                'data': rules
            }
        )
        return self.process_response(response)


    def generate_otp(self, mobile_number):
        base_url = self.base_url_account_holder_otp_action
        response = self.request.post(
            url=urljoin(self.base_url, base_url),
            headers={**self.base_headers, 'X-API-VERSION': 'v1' },
            json={
                'action': 'GENERATE',
                'request':  {
                    "mobile_number": mobile_number
                }
            }
        )
        return self.process_response(response)
    
    def validate_otp(self, mobile_number, session_id, user_response):
        base_url = self.base_url_account_holder_otp_action
        response = self.request.post(
            url=urljoin(self.base_url, base_url),
            headers={**self.base_headers, 'X-API-VERSION': 'v1' },
            json={
                'action': 'VALIDATE',
                'request':  {
                    'mobile_number': mobile_number
                },
                'response': {
                    'user_response': user_response,
                    'session_id': session_id
                }
            }
        )
        return self.process_response(response)

    def edit_action_card_dispatch_action(self, card_dispatch_id, action, attributes):
        base_url = self.base_url_workflow_get_card_dispatch_edit_action.format(card_dispatch_id=card_dispatch_id)
        response = self.request.post(url=urljoin(self.base_url, base_url),
                                     headers={**self.base_headers, 'X-API-VERSION': 'v1' },
                                     json={
                                        'action': action,
                                        'attributes': attributes
                                     })
        return self.process_response(response)
    
    def get_product_inventory(self):
        base_url = self.base_url_product_inventory
        response = self.request.get(
            url=urljoin(self.base_url, base_url),
            headers={**self.base_headers, 'X-API-VERSION': 'v1' })
        return self.process_response(response)
    
    def perform_payment_instrument_dummy_swap(self, person_id=None, payment_instrument_product_code=None, ref_id=None, next_ref_id=None):
        url_fragment = self.base_url_person_payment_instrument_dummy_swap.format(person_id=person_id)
        response = self.request.post(
            url=urljoin(self.base_url, url_fragment),
            headers={**self.base_headers, 'X-API-VERSION': 'v1' },
            json={
                'payment_instrument_product_code': payment_instrument_product_code,
                'ref_id': ref_id,
                'next_ref_id': next_ref_id
            }
        )
        return self.process_response(response)