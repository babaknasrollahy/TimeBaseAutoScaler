# import json

# def set_status_and_type(tbas_name, tbas_type, tbase_status):
#     with open("./test-opjects.txt", "r") as file :
#         data = file.readlines()
#     i = 0
#     for item in data:
#         item = json.loads(item)
#         if item.get("tbas_name") == tbas_name :
#             item['status']['status'] = tbase_status
#             item['status']['type'] = tbas_type
#             data[i] = json.dumps(item) + "\n"
#         i += 1
#     with open("./test-opjects.txt" , "w") as file:
#         file.writelines(data)
#         file.close()
#     return True




# def set_replica(tbas_name,count):
#     with open("./test-opjects.txt", "r") as file :
#         data = file.readlines()
#     i = 0
#     for item in data:
#         item = json.loads(item)
#         if item.get("tbas_name") == tbas_name :
#             val = item['status']['set_replica']
#             val2 = item['status']['current_replica']
#             item['status']['set_replica'] = int(val) + int(count)
#             item['status']['current_replica'] = int(val2) + int(count)
#             data[i] = json.dumps(item) + "\n"
#         i += 1
#     with open("./test-opjects.txt" , "w") as file:
#         file.writelines(data)
#         file.close()
#     return True


# def set_status(tbas_name, tbase_status):
#     with open("./test-opjects.txt", "r") as file :
#         data = file.readlines()
#     i = 0
#     for item in data:
#         item = json.loads(item)
#         if item.get("tbas_name") == tbas_name :
#             item['status']['status'] = tbase_status
#             data[i] = json.dumps(item) + "\n"
#         i += 1
#     with open("./test-opjects.txt" , "w") as file:
#         file.writelines(data)
#         file.close()
#     return True

#==========================================================================


import requests
import json
import datetime


#unavailableReplicas
#availableReplicas
#readyReplicas
#updatedReplicas
#replicas
# Define the API server URL and token for authentication
def set_status_and_type(status_set_replicas, status_type, status_status, status_message, tbase_name, tbase_namespace):
    api_server = "https://127.0.0.1:6443"
    token = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjRFdFNTSHFRSXgzaXM4TGJmWkxhWHF1ZjdFWXhNdjItaDRzUmlqYkc1bmcifQ.eyJhdWQiOlsiaHR0cHM6Ly9rdWJlcm5ldGVzLmRlZmF1bHQuc3ZjLmNsdXN0ZXIubG9jYWwiLCJrM3MiXSwiZXhwIjoxNzcwOTc2NzQxLCJpYXQiOjE3Mzk0NDA3NDEsImlzcyI6Imh0dHBzOi8va3ViZXJuZXRlcy5kZWZhdWx0LnN2Yy5jbHVzdGVyLmxvY2FsIiwianRpIjoiODIwZTQ4ZmMtNjU3My00Yzg2LTgzMDYtNDMyMGY1YmM0OGNmIiwia3ViZXJuZXRlcy5pbyI6eyJuYW1lc3BhY2UiOiJkZWZhdWx0Iiwibm9kZSI6eyJuYW1lIjoibm9kZS0wMiIsInVpZCI6IjUwNTY2ZjFlLWVlOWYtNDk3NS1iNTcxLWU3ZTQ5NDgxZDUxZSJ9LCJwb2QiOnsibmFtZSI6InRlc3QtNzc3OTVjZDY4Ni1qbXFwcyIsInVpZCI6IjA4NjFhMzgwLWJjZGMtNGE2NS05YWU3LWZjNGFlN2Y3NDhkMiJ9LCJzZXJ2aWNlYWNjb3VudCI6eyJuYW1lIjoidGVzdCIsInVpZCI6IjZkNTkyZmM1LTQ1MjYtNDQ5Ny04NWUwLWU2MDJmNDM0ODQ1NCJ9LCJ3YXJuYWZ0ZXIiOjE3Mzk0NDQzNDh9LCJuYmYiOjE3Mzk0NDA3NDEsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDpkZWZhdWx0OnRlc3QifQ.nTnUB3RPeuJPxIf94YQ6v-xj0JUXLEVybru6AWoEFEob4KUQwfQdYavtq3p6-q2eFqUpJIpPZ93eyUIwkedxaoyTYTd1HQs6n_SQXV7jRwO9MfI3--RqDrga91tZoFyG5QtqyfHjzh8b9Nm0VjRfQ9U2dO9Klgn4ImkiYZ0CiN1gCHSz2Wmg3dbUMnRFWz31QsPnbd6-Yhc8aBQlN4mJLOMztN6DVsl_zZwzSOl1epUiuki8H8pVp1lBAst7ky_18FxI4Q-us7IoeMCtGaeJArH1E3hIY_pcXpZqCND3kojsu4g6zVsv2mK3hg_GH9-4KQEXxRs3zw-m-qbFTMRepA"
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
        f"{api_server}/apis/sre.exalab.co/v1/namespaces/{tbase_namespace}/timebaseautoscaler/{tbase_name}/status",
        headers=headers2,
        verify=False,
        data=json.dumps(status_payload)  # Set verify=True if you have a valid SSL certificate
    )

    print(response.json())


def set_replica(tbase_name,tbase_namespace , count_of_replica ):
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
            'set_replicas': count_of_replica,
        }
    }
    response = requests.patch(
        # f"{api_server}/apis/apps/v1/namespaces/{namespace}/deployments",
        f"{api_server}/apis/sre.exalab.co/v1/namespaces/{tbase_namespace}/timebaseautoscaler/{tbase_name}/status",
        headers=headers2,
        verify=False,
        data=json.dumps(status_payload)  # Set verify=True if you have a valid SSL certificate
    )

    print(response.json())



def set_status(tbase_name, tbase_namespace ,status_status):
    api_server = "https://127.0.0.1:6443"
    token = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjRFdFNTSHFRSXgzaXM4TGJmWkxhWHF1ZjdFWXhNdjItaDRzUmlqYkc1bmcifQ.eyJhdWQiOlsiaHR0cHM6Ly9rdWJlcm5ldGVzLmRlZmF1bHQuc3ZjLmNsdXN0ZXIubG9jYWwiLCJrM3MiXSwiZXhwIjoxNzcwOTc2NzQxLCJpYXQiOjE3Mzk0NDA3NDEsImlzcyI6Imh0dHBzOi8va3ViZXJuZXRlcy5kZWZhdWx0LnN2Yy5jbHVzdGVyLmxvY2FsIiwianRpIjoiODIwZTQ4ZmMtNjU3My00Yzg2LTgzMDYtNDMyMGY1YmM0OGNmIiwia3ViZXJuZXRlcy5pbyI6eyJuYW1lc3BhY2UiOiJkZWZhdWx0Iiwibm9kZSI6eyJuYW1lIjoibm9kZS0wMiIsInVpZCI6IjUwNTY2ZjFlLWVlOWYtNDk3NS1iNTcxLWU3ZTQ5NDgxZDUxZSJ9LCJwb2QiOnsibmFtZSI6InRlc3QtNzc3OTVjZDY4Ni1qbXFwcyIsInVpZCI6IjA4NjFhMzgwLWJjZGMtNGE2NS05YWU3LWZjNGFlN2Y3NDhkMiJ9LCJzZXJ2aWNlYWNjb3VudCI6eyJuYW1lIjoidGVzdCIsInVpZCI6IjZkNTkyZmM1LTQ1MjYtNDQ5Ny04NWUwLWU2MDJmNDM0ODQ1NCJ9LCJ3YXJuYWZ0ZXIiOjE3Mzk0NDQzNDh9LCJuYmYiOjE3Mzk0NDA3NDEsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDpkZWZhdWx0OnRlc3QifQ.nTnUB3RPeuJPxIf94YQ6v-xj0JUXLEVybru6AWoEFEob4KUQwfQdYavtq3p6-q2eFqUpJIpPZ93eyUIwkedxaoyTYTd1HQs6n_SQXV7jRwO9MfI3--RqDrga91tZoFyG5QtqyfHjzh8b9Nm0VjRfQ9U2dO9Klgn4ImkiYZ0CiN1gCHSz2Wmg3dbUMnRFWz31QsPnbd6-Yhc8aBQlN4mJLOMztN6DVsl_zZwzSOl1epUiuki8H8pVp1lBAst7ky_18FxI4Q-us7IoeMCtGaeJArH1E3hIY_pcXpZqCND3kojsu4g6zVsv2mK3hg_GH9-4KQEXxRs3zw-m-qbFTMRepA"
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
            'status': status_status,
            'last_transition_time': datetime.datetime.utcnow().isoformat() + "Z",
        }
    }
    response = requests.patch(
        # f"{api_server}/apis/apps/v1/namespaces/{namespace}/deployments",
        f"{api_server}/apis/sre.exalab.co/v1/namespaces/{tbase_namespace}/timebaseautoscaler/{tbase_name}/status",
        headers=headers2,
        verify=False,
        data=json.dumps(status_payload)  # Set verify=True if you have a valid SSL certificate
    )

    print(response.json())


def set_deployment_replica(deployment_name,deployment_namespace,count_of_replica):
    api_server = "https://127.0.0.1:6443"
    token = "eyJhbGciOiJSUzI1NiIsImtpZCI6InMxT2RDT0s0bng1N1lrbjFFZEVUVVdPNXc1SlJGQjZXN29GWHlGaVRpR3MifQ.eyJhdWQiOlsiaHR0cHM6Ly9rdWJlcm5ldGVzLmRlZmF1bHQuc3ZjLmNsdXN0ZXIubG9jYWwiXSwiZXhwIjoxNzcxMDA4OTI5LCJpYXQiOjE3Mzk0NzI5MjksImlzcyI6Imh0dHBzOi8va3ViZXJuZXRlcy5kZWZhdWx0LnN2Yy5jbHVzdGVyLmxvY2FsIiwianRpIjoiYmMzNjVjNmItZjgyNC00ZWUwLTk4OTYtM2VmNTllNDIxMmE2Iiwia3ViZXJuZXRlcy5pbyI6eyJuYW1lc3BhY2UiOiJkZWZhdWx0Iiwibm9kZSI6eyJuYW1lIjoibm9kZTAxIiwidWlkIjoiMWRiZmRiMGYtMDAxNi00MjdjLThjN2EtYWQwYTc0ZDYxM2E4In0sInBvZCI6eyJuYW1lIjoidGVzdC02Nzc4NGQ4NzgtbjhrbnQiLCJ1aWQiOiI3YjBlMGZkMy1iZDk1LTQ5MTgtOTllYS0yM2FlN2M5Mjg0MzQifSwic2VydmljZWFjY291bnQiOnsibmFtZSI6InRlc3QiLCJ1aWQiOiIwMGY4YjNiYS0yYjEzLTRmNWItOGVmOS1mMjJiMjNlZWYyOWUifSwid2FybmFmdGVyIjoxNzM5NDc2NTM2fSwibmJmIjoxNzM5NDcyOTI5LCJzdWIiOiJzeXN0ZW06c2VydmljZWFjY291bnQ6ZGVmYXVsdDp0ZXN0In0.EhZkyCxLE7mS3Q8ZfIUEOETaVgPeP4hgewDBVtLDbOleuWdrJ1JuG_9kpaAfjv4Pzl0T-KRaPdSXvf4C3E1K2mSW8qRi_6lIW6-UTc423piLye4Z0FdE0UphOIjXwUGywJGfuGkYxxRP82Hg1D7mlI7Mxc4DVRqt9getoYyGod8xSfmZEJH-vLH-93_nHdqSrNXDEHSQTH6KHOc3U2EnVfOAfhXkNq4VfHj6I3x-_MHmHk9gPYjyTcPeq-c0tEbIb-ZhuJ5_B1KRJLQeMGFkFup1BxSYeKYUDP2TSAA8i8BAoWqz_qUOBLVVwSwqcBjgm4W3zk31UT9sKH_3fg-DEQ"  # Replace with your token
    namespace = deployment_namespace
    deployment_name = deployment_name  # Replace with your Deployment name

    # Headers for the request
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/merge-patch+json",
    }

    # Payload to update the replicas
    replica_payload = {
        "spec": {
            "replicas": count_of_replica  # Set the desired number of replicas
        }
    }

    # Send the PATCH request to update the Deployment
    try:
        response = requests.patch(
            f"{api_server}/apis/apps/v1/namespaces/{namespace}/deployments/{deployment_name}",
            headers=headers,
            verify=False,  # Replace with the path to your CA certificate in production
            data=json.dumps(replica_payload),
        )

        print(response.json())
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")