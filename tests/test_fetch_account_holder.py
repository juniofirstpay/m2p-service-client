import pytest
from zeta_micro_client import zeta_client
from datetime import datetime


class TestCreateAccountHolder:
    def test_get_account_holder(self):

        with zeta_client.open() as client:
            (error, response) = client.get_account_holder(
                "id", "3ae7912c-013e-4c98-b004-a9c416285126"
            )
            assert (
                response.get("individual_id") == "3ae7912c-013e-4c98-b004-a9c416285126"
            )
            # response = client.get_account_holder("id", response.get('individual_id'))
            # assert response.get('individual_id') == '3ae7912c-013e-4c98-b004-a9c416285126'

    # def test_create_account_holder_with_same_information(self):
    #     first_name = 'Nirbhay'
    #     middle_name = ''
    #     last_name = 'Gupta'
    #     date_of_birth = "1993-01-22"
    #     gender = 'Male'
    #     kyc_type = 'PAN'
    #     kyc_value = 'TSET90909090'
    #     mobile_number = '1895000001'
    #     with zeta_client.open() as client:
    #         response = client.create_account_holder(first_name,
    #                                     middle_name,
    #                                     last_name,
    #                                     date_of_birth,
    #                                     gender,
    #                                     kyc_type,
    #                                     kyc_value,
    #                                     mobile_number)
    #         response = client.get_account_holder("id", response.get('individual_id'))
    #         assert response.get('individual_id') == '3ae7912c-013e-4c98-b004-a9c416285126'

    # def test_create_account_holder_with_same_mobile_number(self):
    #     first_name = 'Nirbhay'
    #     middle_name = ''
    #     last_name = 'Gupta'
    #     date_of_birth = "1993-01-22"
    #     gender = 'Male'
    #     kyc_type = 'PAN'
    #     kyc_value = 'TSET90909091'
    #     mobile_number = '1895000001'
    #     with zeta_client.open() as client:
    #         response = client.create_account_holder(first_name,
    #                                     middle_name,
    #                                     last_name,
    #                                     date_of_birth,
    #                                     gender,
    #                                     kyc_type,
    #                                     kyc_value,
    #                                     mobile_number)
    #         response = client.get_account_holder("id", response.get('individual_id'))
    #         assert response.get('individual_id') == '3ae7912c-013e-4c98-b004-a9c416285126'

    # def test_create_account_holder_with_same_kyc(self):
    #     first_name = 'Nirbhay'
    #     middle_name = ''
    #     last_name = 'Gupta'
    #     date_of_birth = "1993-01-22"
    #     gender = 'Male'
    #     kyc_type = 'PAN'
    #     kyc_value = 'TSET90909090'
    #     mobile_number = '1895000002'
    #     with zeta_client.open() as client:
    #         response = client.create_account_holder(first_name,
    #                                     middle_name,
    #                                     last_name,
    #                                     date_of_birth,
    #                                     gender,
    #                                     kyc_type,
    #                                     kyc_value,
    #                                     mobile_number)
    #         response = client.get_account_holder("id", response.get('individual_id'))
    #         assert response.get('individual_id') != '3ae7912c-013e-4c98-b004-a9c416285126'
