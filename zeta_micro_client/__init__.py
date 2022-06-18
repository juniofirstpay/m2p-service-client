from .main import ZetaMicroClient
from .service import ZetaService
from .env import __config
from .v2 import ZetaClient as ZetaClientV2

zeta_service = ZetaService(__config.get('endpoint'),
                           __config.get('clientid'),
                           __config.get('clientsecret'),
                           __config.get('apikey'))

zeta_client = ZetaMicroClient(zeta_service)


def ZetaClient():
    zeta_service = ZetaService(__config.get('endpoint'),
                               __config.get('clientid'),
                               __config.get('clientsecret'),
                               __config.get('apikey'))

    zeta_client = ZetaMicroClient(zeta_service)
    return zeta_client
