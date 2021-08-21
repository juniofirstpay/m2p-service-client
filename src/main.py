from typing import ContextManager, Dict, List
from contextlib import contextmanager
from schema import (CreateAccountSchema, 
                    CreateAccountHolderSchema, 
                    CreateResourceSchema, UpdateFormFactorStatusSchema,
                    UpdateResourceStatusSchema)
from service import ZetaService


class ZetaMicroClient(object):

    def __init__(self, zeta_service: ZetaService):
        self.zeta_service = zeta_service 

    @contextmanager
    def open(self):
        try:
            self.zeta_service.open()
            yield self
        finally:
            self.zeta_service.close()
    
    def close(self):
        self.zeta_service.close()
       

    # Makes a call to zeta micro service and issues account holder
    def create_account_holder(self, 
                            first_name: str,
                            middle_name: str,
                            last_name: str,
                            date_of_birth: str,
                            gender: str,
                            kyc_type: str,
                            kyc_value: str,
                            mobile_number: str) -> Dict:
        data = {
            'first_name': first_name,
            'middle_name': middle_name,
            'last_name': last_name,
            'date_of_birth': date_of_birth,
            'gender': gender,
            'kyc_type': kyc_type,
            'kyc_value': kyc_value,
            'mobile_number': mobile_number
        }
        valid_data = CreateAccountHolderSchema().load(data)
        response = self.zeta_service.create_account_holder(**valid_data)
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
    
    # Make the 
    def create_account(self, 
                        account_holder_id: str,
                        account_name: str) -> Dict:
        data={
            'account_holder_id': account_holder_id,
            'accounts': account_name
        }
        valid_data = CreateAccountSchema().load(data)
        response = self.zeta_service.create_account(**valid_data)
        return response

    def get_resources(self, account_holder_id: str) -> List[Dict]:
        response = self.zeta_service.get_resources(account_holder_id)
        return response

    def get_resource(self, resource_id: str) -> List[Dict]:
        response = self.zeta_service.get_resource(resource_id)
        return response

    def create_resource(self, 
                        account_holder_id: str,
                        account_id: str,
                        mobile_number: str) -> Dict:
        
        data = {
            'account_holder_id': account_holder_id,
            'account_id': account_id,
            'mobile_number': mobile_number
        }
        valid_data = CreateResourceSchema().load(data)
        response = self.create_resource(**valid_data)    
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
        response = self.zeta_service.update_resource_status(resource_id, **valid_data)
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
        response = self.update_form_factor(resource_id, form_factor_id, **valid_data)
        return response