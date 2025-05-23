from .main import ZetaMicroClient
from .service import ZetaService
from .env import get_config


def ZetaClient(onboarding_partner: str):
    if onboarding_partner == "ZETA_RBL":
        config = get_config(onboarding_partner)
        zeta_service = ZetaService(
            config.get("endpoint"),
            config.get("clientid"),
            config.get("clientsecret"),
            config.get("apikey"),
        )
        zeta_client = ZetaMicroClient(zeta_service, onboarding_partner=onboarding_partner)

    if onboarding_partner == "M2P_TRANSCORP":
        config = get_config(onboarding_partner)
        zeta_service = ZetaService(
            config.get("endpoint"),
            config.get("clientid"),
            config.get("clientsecret"),
            config.get("apikey"),
        )
        zeta_client = ZetaMicroClient(zeta_service, onboarding_partner=onboarding_partner)

    if onboarding_partner == "M2P_TRANSCORP_V2":
        config = get_config(onboarding_partner)
        zeta_service = ZetaService(
            config.get("endpoint"),
            config.get("clientid"),
            config.get("clientsecret"),
            config.get("apikey"),
        )
        zeta_client = ZetaMicroClient(zeta_service, onboarding_partner=onboarding_partner)

    return zeta_client
