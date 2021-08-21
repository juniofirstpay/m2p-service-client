import json
from yaml import FullLoader as loader, load
from warnings import warn

__variant = None
__config = None
try:
    env = load(open('config.yaml'), Loader=loader)
    __config = env.get('service')
    __variant= env.get('variant')

    if __config is None:
        warn("Config Object Not Found")
    if __config.get('endpoint') is None:
        warn("Zeta Client Enpoint Not Configured")
    if __config.get('clientid') is None:
        warn("Zeta Client Id Configured")
    if __config.get('clientsecret') is None:
        warn("Zeta Client Secret Configured")
    
    if __variant is None:
        warn("Without variant no call will be made")

    
except Exception as e:
    print(e)
    