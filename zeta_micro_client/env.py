import json
from yaml import FullLoader as loader, load
from warnings import warn

__variant = None
__zeta_config = None
__m2p_config = None

try:
    env = load(open("config.yaml"), Loader=loader)

    zeta_env = env.get("zeta_client")
    if zeta_env:
        __zeta_config = zeta_env.get("service")
        __variant = zeta_env.get("variant")

        if __zeta_config is None:
            warn("Config Object Not Found")
        if __zeta_config.get("endpoint") is None:
            warn("Zeta Client Enpoint Not Configured")
        if __zeta_config.get("clientid") is None:
            warn("Zeta Client Id Configured")
        if __zeta_config.get("clientsecret") is None:
            warn("Zeta Client Secret Configured")

    if __variant is None:
        warn("Without variant no call will be made")

    m2p_env = env.get("m2p_client")
    if m2p_env:
        __m2p_config = m2p_env.get("service")
        __variant = m2p_env.get("variant")

        if __m2p_config is None:
            warn("Config Object Not Found")
        if __m2p_config.get("endpoint") is None:
            warn("Zeta Client Enpoint Not Configured")
        if __m2p_config.get("clientid") is None:
            warn("Zeta Client Id Configured")
        if __m2p_config.get("clientsecret") is None:
            warn("Zeta Client Secret Configured")

        if __variant is None:
            warn("Without variant no call will be made")

except Exception as e:
    print(e)


def setup_client(env):
    global __zeta_config
    global __m2p_config
    global __variant
    try:
        # env = load(open('config.yaml'), Loader=loader)

        zeta_env = env.get("zeta_client")
        if zeta_env:
            __zeta_config = zeta_env.get("service")
            __variant = zeta_env.get("variant")

            if __zeta_config is None:
                warn("Config Object Not Found")
            if __zeta_config.get("endpoint") is None:
                warn("Zeta Client Enpoint Not Configured")
            if __zeta_config.get("clientid") is None:
                warn("Zeta Client Id Configured")
            if __zeta_config.get("clientsecret") is None:
                warn("Zeta Client Secret Configured")

        if __variant is None:
            warn("Without variant no call will be made")

        m2p_env = env.get("m2p_client")
        if m2p_env:
            __m2p_config = m2p_env.get("service")
            __variant = m2p_env.get("variant")

            if __m2p_config is None:
                warn("Config Object Not Found")
            if __m2p_config.get("endpoint") is None:
                warn("Zeta Client Enpoint Not Configured")
            if __m2p_config.get("clientid") is None:
                warn("Zeta Client Id Configured")
            if __m2p_config.get("clientsecret") is None:
                warn("Zeta Client Secret Configured")

            if __variant is None:
                warn("Without variant no call will be made")

    except Exception as e:
        print(e)


def get_config(onboarding_partner_name: str):
    if onboarding_partner_name == "ZETA_RBL":
        return __zeta_config
    elif onboarding_partner_name == "M2P_TRANSCORP":
        return __m2p_config
