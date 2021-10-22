from typing import ContextManager, Dict, List, Tuple, Optional
from contextlib import contextmanager

from marshmallow.utils import resolve_field_instance
from .schema import (CreateAccountSchema,
                     CreateAccountHolderSchema,
                     CreateResourceSchema, DeleteResourceStatusSchema, UpdateFormFactorStatusSchema,
                     UpdateResourceStatusSchema, AccountCreditSchema,
                     AccountDebitSchema, AccountTransferSchema)
from .service import ZetaService


class ZetaMicroClient(object):

    def __init__(self, zeta_service: ZetaService):
        self.zeta_service = zeta_service

    @contextmanager
    def open(self):
        try:
            self.zeta_service.open()
            yield self
            return self
        finally:
            self.zeta_service.close()

    def start(self):
        self.zeta_service.open()
        return self

    def finish(self):
        self.zeta_service.close()
        return self

    # Makes a call to zeta micro service and issues account holder
    def create_account_holder(self,
                              first_name: str,
                              middle_name: str,
                              last_name: str,
                              date_of_birth: str,
                              gender: str,
                              kyc_type: str,
                              kyc_value: str,
                              phone_number: str) -> Dict:
        data = {
            'first_name': first_name,
            'middle_name': middle_name,
            'last_name': last_name,
            'dob': date_of_birth,
            'gender': gender,
            'kyc_type': kyc_type,
            'kyc_value': kyc_value,
            'phone_number': phone_number
        }
        valid_data = CreateAccountHolderSchema().load(data)
        dob = valid_data.pop('dob')
        phone_number = '+91' + valid_data.pop('phone_number')
        response = self.zeta_service.create_account_holder(
            **valid_data, phone_number=phone_number, dob=dob.isoformat())
        return response

    def get_account_holder(self, type: str, value: str):
        response = self.zeta_service.get_account_holder(type, value)
        return response

    def get_accounts(self, account_holder_id: str) -> List[Dict]:
        response = self.zeta_service.get_accounts(account_holder_id)
        return response

    def get_account(self, account_id: str) -> List[Dict]:
        response = self.zeta_service.get_account(account_id)
        return response

    def update_account(self, account_id: str, status: str) -> List[Dict]:
        response = self.zeta_service.update_account(account_id, status=status)
        return response

    # Make the
    def create_account(self,
                       account_holder_id: str,
                       account_name: str) -> Dict:
        data = {
            'account_holder_id': account_holder_id,
            'accounts': [account_name]
        }
        valid_data = CreateAccountSchema().load(data)
        (error, response) = self.zeta_service.create_account(**valid_data)
        if error:
            return error, response
        return (None, response[0])

    def get_resources(self, account_holder_id: str) -> List[Dict]:
        response = self.zeta_service.get_resources(account_holder_id)
        return response

    def get_resource(self, resource_id: str) -> Tuple[Optional[int], Dict]:
        response = self.zeta_service.get_resource(resource_id)
        return response

    def create_resource(self,
                        account_id: str,
                        mobile_number: str) -> Dict:

        data = {
            'account_id': account_id,
            'phone_number': mobile_number
        }
        valid_data = CreateResourceSchema().load(data)
        response = self.zeta_service.create_resource(**valid_data)
        return response

    def get_resource(self, resource_id: str) -> Dict:
        response = self.zeta_service.get_resource(resource_id)
        return response

    def update_resource_status(self,
                               resource_id: str,
                               status: str,
                               description: str) -> Dict:
        data = {
            'status': status,
            'description': description
        }
        valid_data = UpdateResourceStatusSchema().load(data)
        response = self.zeta_service.update_resource_status(
            resource_id, **valid_data)
        return response

    def delete_resource(self,
                        resource_id: str,
                        description: str) -> Dict:
        data = {
            'status': "DELETED"
        }
        valid_data = DeleteResourceStatusSchema().load(data)
        response = self.zeta_service.delete_resource_status(
            resource_id, **valid_data)
        return response

    def update_form_factor(self,
                           resource_id: str,
                           form_factor_id: str,
                           status: str,
                           description: str) -> Dict:
        data = {
            'status': status,
            'description': description
        }
        valid_data = UpdateFormFactorStatusSchema().load(data)
        response = self.zeta_service.update_form_factor(
            resource_id, form_factor_id, **valid_data)
        return response

    def debit_account(self, txn_id: str, account_id: str, amount: int, remarks: str, attributes: dict):

        data = {
            'debit_account_id': account_id,
            'amount': amount,
            'remarks': remarks,
            'attributes': attributes,
            'txn_id': txn_id
        }
        valid_data = AccountDebitSchema().load(data)
        response = self.zeta_service.account_debit(**valid_data)
        return response

    def credit_account(self, txn_id: str, account_id: str, amount: int, remarks: str, attributes: dict,):

        data = {
            'credit_account_id': account_id,
            'amount': amount,
            'remarks': remarks,
            'attributes': attributes,
            'txn_id': txn_id
        }
        valid_data = AccountCreditSchema().load(data)
        response = self.zeta_service.account_credit(**valid_data)
        return response

    def account_transfer(self, txn_id: str, debit_account_id: str, credit_account_id: str, amount: int, remarks: str, attributes: dict):

        data = {
            'debit_account_id': debit_account_id,
            'credit_account_id': credit_account_id,
            'amount': amount,
            'remarks': remarks,
            'attributes': attributes,
            'txn_id': txn_id
        }
        valid_data = AccountTransferSchema().load(data)
        response = self.zeta_service.account_transfer(**valid_data)
        return response

    def reverse_txn(self, txn_id: str):
        response = self.zeta_service.reverse_txn(txn_id=txn_id)
        return response

    def get_balance(self, account_id: str):
        response = self.zeta_service.get_balance(account_id=account_id)
        return response

    def get_balance_accounts(self, account_holder_id: str):
        response = self.zeta_service.get_balance_accounts(
            account_holder_id=account_holder_id)
        return response

    def get_account_holder_token(self, account_holder_id: str):
        response = self.zeta_service.get_account_holder_token(
            account_holder_id=account_holder_id)
        return response

    def get_resource_txns(self, resource_id: str):
        response = self.zeta_service.fetch_resource_transactions(
            resource_id=resource_id)
        return response

    def create_phone_number(self, account_id: str, phone_number: str):
        response = self.zeta_service.create_phone_number(
            account_id=account_id, phone_number=phone_number)
        return response

    def delete_phone_number(self, account_id: str):
        response = self.zeta_service.delete_phone_number(
            account_id=account_id)
        return response

    def create_card(self, account_id: str, card: str):
        response = self.zeta_service.create_card(
            account_id=account_id, card=card)
        return response

    def delete_card(self, account_id: str):
        response = self.zeta_service.delete_card(
            account_id=account_id)
        return response

    def get_card_status(self, card_id):
        response = self.zeta_service.get_card_status(
            card_id=card_id)
        return response

    def update_card_status(self, card_id, status, reason=None):
        response = self.zeta_service.update_card_status(
            card_id=card_id,
            status=status,
            reason=reason
        )
        return response

    # def reissue_card_form_factor(
    #     self,
    #     child_account_id: str,
    #     parent_account_id: str,
    #     child_phone_number: str,
    #     resource_id: str
    # ):
    #     # Fetch old account
    #     error, old_account = self.get_account(child_account_id)
    #     print("error, old_account", error, old_account)
    #     if error:
    #         return error, "Child account not found."

    #     # Fetch old balance
    #     error, old_balance = self.get_balance(old_account["zeta_ref_id"])
    #     print("error, old_balance", error, old_balance)
    #     if error:
    #         return error, "Balance fetch error."

    #     # Get resource
    #     error, old_resource = self.get_resource(resource_id)
    #     print("error, old_resource", error, old_resource)
    #     if error:
    #         return error, "Old resource not found."

    #     if old_resource["account_id"] != child_account_id:
    #         return 400, "Resource mismatch error."

    #     # Delete old card
    #     # error, old_card = self.delete_card(child_account_id)
    #     # print("error, old_card", error, old_card)
    #     # if error:
    #     #     return error, "Old card deletion error."

    #     # Delete old number
    #     # error, old_phone_number = self.delete_phone_number(child_account_id)
    #     # print("error, old_phone_number", error, old_phone_number)
    #     # if error:
    #     #     return error, "Old phone number deletion error."

    #     # Create new account
    #     error, new_account = self.create_account(
    #         old_account["owner_ach_id"],
    #         f'{old_account["name"]}_1'
    #     )
