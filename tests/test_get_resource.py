from zeta_micro_client import zeta_client, ZetaClient


class TestPaymentInstument:
    def test_get_resource(self):
        with zeta_client.open() as client:
            error, response = client.get_resource(
                "31cf2a9d-bf60-4537-b795-8f8c8e5a28b5"
            )

    def test_get_transactions(self):
        resource_id = "31cf2a9d-bf60-4537-b795-8f8c8e5a28b5"
        with ZetaClient().open() as client:
            error, response = client.get_resource_txns(resource_id)
            print(error, response)
            assert error is not None
            assert isinstance(response, list)
