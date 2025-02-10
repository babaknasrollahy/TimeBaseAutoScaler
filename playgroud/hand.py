import requests
import json
import datetime


#unavailableReplicas
#availableReplicas
#readyReplicas
#updatedReplicas
#replicas
# Define the API server URL and token for authentication
def set_status(status_set_replicas, status_type, status_status, status_message):
    api_server = "https://127.0.0.1:6443"
    token = "eyJhbGciOiJSUzI1NiIsImtpZCI6InozamppX0ltdzVyZ1F6R1M3MkFxR3Y5UmRwcWdpWUVuTjhkb20yQTBPRXMifQ.eyJhdWQiOlsiaHR0cHM6Ly9rdWJlcm5ldGVzLmRlZmF1bHQuc3ZjLmNsdXN0ZXIubG9jYWwiXSwiZXhwIjoxNzcwNzQ4NTQ0LCJpYXQiOjE3MzkyMTI1NDQsImlzcyI6Imh0dHBzOi8va3ViZXJuZXRlcy5kZWZhdWx0LnN2Yy5jbHVzdGVyLmxvY2FsIiwianRpIjoiYjIwZWNmY2YtOTA3Mi00YzQwLWE5YTYtOWU1YTJkZWM4MGI4Iiwia3ViZXJuZXRlcy5pbyI6eyJuYW1lc3BhY2UiOiJkZWZhdWx0Iiwibm9kZSI6eyJuYW1lIjoibm9kZTAxIiwidWlkIjoiZmQzYjVlMmEtMWY4NS00ODVkLTkyOWItNGUyMDc3YjU4MGMyIn0sInBvZCI6eyJuYW1lIjoidGVzdC02Nzc4NGQ4NzgtZHJ6NzYiLCJ1aWQiOiIxZjMwYjQ3NC01MDhlLTQ1ZWUtYjQ2NC04OTgwNjZlODgzNDMifSwic2VydmljZWFjY291bnQiOnsibmFtZSI6InRlc3QiLCJ1aWQiOiI3NDFkZmRlZC01ZTk2LTRlNGUtYjc0Ny1jYzc3ZGI4YTVlMTgifSwid2FybmFmdGVyIjoxNzM5MjE2MTUxfSwibmJmIjoxNzM5MjEyNTQ0LCJzdWIiOiJzeXN0ZW06c2VydmljZWFjY291bnQ6ZGVmYXVsdDp0ZXN0In0.LwxJ-QIXqvQUgnxLsx1enb43OXWHxRoHtudiSFpvXgc4eFFTBS1BvZHqQTCpown78pXAtk9nF6pxwRXh4ZZ9qMKMsSI4v1QDrr2_q3RClq8gY7euu1PP6oHju3lMurs6CYkptU9YxRIUUSygUXa5ZZgetwCeZjQLDZ5XWxOTMYvG6F83jgxfw7tRZFn-WqKaPG10D3S1vCgbBoF7mAijVzaXF5nN6w9qOGcmm1lKfwjaBfNsY0BNoA05NUvgjJ4w4MNYswjxfiofJLxQ481xaJvs-YlCL7ikka0gJ5vr3atv3GVSPm_NZDueaRCa1s5pN4YGHI-ETtjXdb8ULOiZow"
    namespace = "default"
    headers = {
        "Authorization": f"Bearer {token}",
    }
    headers2 = {
        'Content-Type': 'application/merge-patch+json',
        "Authorization": f"Bearer {token}",
    }

    status_payload = {
        "status": {
            'set_replicas': status_set_replicas,
            'type': status_type,
            'status': status_status,
            'last_transition_time': datetime.datetime.utcnow().isoformat() + "Z",
            'message': status_message
        }
    }
    response = requests.patch(
        # f"{api_server}/apis/apps/v1/namespaces/{namespace}/deployments",
        f"{api_server}/apis/sre.exalab.co/v1/namespaces/default/timebaseautoscaler/first-test/status",
        headers=headers2,
        verify=False,
        data=json.dumps(status_payload)  # Set verify=True if you have a valid SSL certificate
    )

    print(response.json())