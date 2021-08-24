import pytest
from zeta_micro_client import zeta_client
from datetime import datetime

class TestAccountTransfer:

    def test_account_debit(self):
        debit_account_id = "f51d8a57-3b72-4dc8-964d-3fcf12d20155"
        with zeta_client.open() as client:
            (error, response) = client.debit_account(debit_account_id, 1, "Test", {})
            print(error, response)
            assert response.get('isPosted') == True

    def test_account_credit(self):
        credit_account_id = "f51d8a57-3b72-4dc8-964d-3fcf12d20155"
        with zeta_client.open() as client:
            (error, response) = client.credit_account(credit_account_id, 1, "Test", {})
            print(error, response)
            assert response.get('isPosted') == True
    
    def test_account_transfer(self):
        credit_account_id = "f51d8a57-3b72-4dc8-964d-3fcf12d20155"
        debit_account_id = "2e6627da-1f65-438b-846b-6d3b34f6bd09"
        with zeta_client.open() as client:
            (error, response) = client.account_transfer(debit_account_id, credit_account_id, 1, "Test", {})
            print(error, response)
            assert response.get('isPosted') == True
            # response = client.get_account_holder("id", response.get('individual_id'))
            # assert response.get('individual_id') == '3ae7912c-013e-4c98-b004-a9c416285126'

    # def test_get_account(self):
    #     account_id = "ed5bedb7-9ac5-448e-9e6c-6f4c7f5eb149"
    #     with zeta_client.open() as client:
    #         (error, response) = client.get_account(account_id)
    #         assert error is None
    #         assert isinstance(response, dict)
    #         assert response.get('zeta_ref_id') == "ed5bedb7-9ac5-448e-9e6c-6f4c7f5eb149"


    # def test_get_accounts(self):
    #     account_holder_id = "3ae7912c-013e-4c98-b004-a9c416285126"
    #     with zeta_client.open() as client:
    #         (error, response) = client.get_accounts(account_holder_id)
    #         print(error, response)
    #         assert error is None
    #         assert isinstance(response, list)