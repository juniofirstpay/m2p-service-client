import pytest
from zeta_micro_client import ZetaClient


class TestAccountHolderToken:
    def test_account_holder_token(self):
        account_holder_id = "0caad7ed-74e1-4999-9418-aaf0fbee93b5"
        with ZetaClient().open() as client:
            (error, response) = client.get_account_holder_token(account_holder_id)
            print(error, response)
            assert error is None
