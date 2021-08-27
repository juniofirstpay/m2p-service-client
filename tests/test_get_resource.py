from zeta_micro_client import zeta_client


def test_get_resource():
    with zeta_client.open() as client:
        error, response = client.get_resource(
            "30608488-f5c0-4f5f-b4f4-676d01f38913")
