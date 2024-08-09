from zeta_micro_client import zeta_client, ZetaClient


class TestCardDispatch:
    def test_edit_action(self):
        card_dispatch_id = "62418e17d5d19b8bd135d54b"
        action = "NAME_ADDRESS_UPDATE"
        attributes = {
            "card_attributes": {"card_name_1": "Baazigar1", "card_name_2": ""},
            "delivery_address": {
                "address_line_1": "puyada puranpani",
                "address_line_2": "puyada",
                "address_line_3": "puyada school",
                "address_line_4": "",
                "state": "West Bengal",
                "city": "Bankura",
                "zipcode": "722148",
            },
        }
        with ZetaClient().open() as client:
            error, response = client.edit_card_dispatch_action(
                card_dispatch_id, action, attributes
            )
            print(error)
            assert error is None
            assert isinstance(response, dict)
