from zeta_micro_client import zeta_client, ZetaClient


class TestPaymentInstument:
    def test_get_txns(self):
        with zeta_client.open() as client:
            error, response = client.get_account_transactions(
                "c32ddbcd-031b-444f-acc3-a6ed8f32707a"
            )

            assert error is None
            assert isinstance(response, dict)
            assert response.get("count") is not None
            assert response.get("count") > 0
            print(response.get("count"))
