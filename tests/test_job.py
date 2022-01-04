import pytest
from zeta_micro_client import ZetaClient
from datetime import datetime
import uuid

class TestJob:

    def test_get_person_account_holder(self):
        with ZetaClient().open() as client:
            person_id = "fdafaf06-b400-4ada-ab25-89af882886e4"
            error, response = client.get_person_account_holder(person_id)
            assert error is None
            assert str(response.get('person_id')) == person_id
            assert str(response.get('zeta_ref_id')) == "ad2cbf27-4ea3-4bbc-afa2-0e1a8c8551ff"
        
    def test_get_person_account(self):
        with ZetaClient().open() as client:
            person_id = "61f9c355-39e8-4135-aa91-4646b026764f"
            error, response = client.get_person_account(person_id)
            assert error is None
            assert str(response.get('person_id')) == person_id
            assert str(response.get('zeta_ref_id')
                       ) == "35304b65-60ce-4b1c-8958-535dac340e0c"

    def test_get_person_account_job(self):
        with ZetaClient().open() as client:
            person_id = "61f9c355-39e8-4135-aa91-4646b026764f"
            error, response = client.get_person_account_job(person_id)
            assert error is None
            assert str(response.get('type')) == "ACCOUNT"
            assert str(response.get('status')) == "COMPLETED"
            assert str(response.get('result').get('person_id')) == person_id
            assert str(response.get('result').get('zeta_ref_id')
                       ) == "35304b65-60ce-4b1c-8958-535dac340e0c"
    
    def test_create_person_account_holder_job(self):
        with ZetaClient().open() as client:
            person_id = "bc283c2c-5345-47f8-b7e1-8d3fc9029461"
            error, response = client.create_person_account_holder_job(
                person_id,
                "Rajesh",
                "",
                "Agarwal",
                "1993-12-19",
                "Male",
                "1819001212",
                "PAN",
                "PIP123PP"
            )
            assert error is None
            assert str(response.get('person_id')) == person_id
            assert str(response.get('type')) == "ACCOUNT_HOLDER"
            assert str(response.get('status')) == "COMPLETED"
            # assert str(response.get('result').get('person_id')) == person_id
            # assert str(response.get('result').get('zeta_ref_id')
            #            ) == "35304b65-60ce-4b1c-8958-535dac340e0c"



    def test_create_person_account_job(self):
        with ZetaClient().open() as client:
            person_id = "0302d4ef-c842-4539-a09a-4544c893d930"
            error, response = client.create_person_account_job(
                person_id, "ad2cbf27-4ea3-4bbc-afa2-0e1a8c8551ff", "Save_UI_2")
            assert error is None
            assert str(response.get('person_id')) == person_id
            assert str(response.get('type')) == "ACCOUNT"
            assert str(response.get('status')) == "COMPLETED"
            # assert str(response.get('result').get('person_id')) == person_id
            # assert str(response.get('result').get('zeta_ref_id')
            #            ) == "35304b65-60ce-4b1c-8958-535dac340e0c"

    def test_create_person_bundle_job(self):
        with ZetaClient().open() as client:
            person_id = "0302d4ef-c842-4539-a09a-4544c893d930"
            error, response = client.create_person_bundle_job(
                person_id, "ad2cbf27-4ea3-4bbc-afa2-0e1a8c8551ff", "Save_UI_3", "1819001213")
            assert error is None
            assert str(response.get('person_id')) == person_id
            assert str(response.get('type')) == "BUNDLE"
            assert str(response.get('status')) == "COMPLETED"

    def test_get_person_bundle(self):
        with ZetaClient().open() as client:
            person_id = "0302d4ef-c842-4539-a09a-4544c893d930"
            error, response = client.get_person_bundle(person_id)
            assert error is None
            assert str(response.get('account').get('zeta_ref_id')
                       ) == "2348df09-b781-4c38-9498-cee7a4667919"
            
