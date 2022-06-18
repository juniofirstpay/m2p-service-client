from .main import ZetaMicroClient
from .service import ZetaService
from .env import __m2p_config, __zeta_config

def ZetaClient(onboarding_partner: str):
    if onboarding_partner == "ZETA_RBL":
        zeta_service = ZetaService(__zeta_config.get('endpoint'),
                                   __zeta_config.get('clientid'),
                                   __zeta_config.get('clientsecret'),
                                   __zeta_config.get('apikey'))
        zeta_client = ZetaMicroClient(zeta_service)

    if onboarding_partner == "M2P_TRANSCORP":
        zeta_service = ZetaService(__m2p_config.get('endpoint'),
                                   __m2p_config.get('clientid'),
                                   __m2p_config.get('clientsecret'),
                                   __m2p_config.get('apikey'))
        zeta_client = ZetaMicroClient(zeta_service)

    return zeta_client