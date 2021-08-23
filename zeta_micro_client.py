from src.main import ZetaMicroClient
from src.service import ZetaService
from src.env import __config


zeta_service = ZetaService(__config.get('endpoint'), 
                        __config.get('clientid'), 
                        __config.get('clientsecret'), 
                        __config.get('apikey'))
                        
zeta_client = ZetaMicroClient(zeta_service)