import os
def kube_config():
    with open("/run/secrets/kubernetes.io/serviceaccount/token", "r") as file:
        token = file.read()
    api_server_host = os.environ.get("KUBERNETES_SERVICE_HOST")
    api_server_port = os.environ.get("KUBERNETES_SERVICE_PORT")
    api_server = f"https://{api_server_host}:{api_server_port}"
    return api_server, token