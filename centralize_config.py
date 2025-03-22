import os
def kube_config():
    api_server = os.environ.get("api_server")
    token = os.environ.get("token")
    api_server  = api_server
    token = token
    return api_server, token