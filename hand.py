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
import centralize_config

api_server , token = centralize_config.kube_config()
#unavailableReplicas
#availableReplicas
#readyReplicas
#updatedReplicas
#replicas
# Define the API server URL and token for authentication
def set_status_and_type(status_set_replicas, status_type, status_status, status_message, tbase_name, tbase_namespace):
    namespace = "default"
    headers = {
        "Authorization": f"Bearer {token}",
    }
    headers2 = {
        'Content-Type': 'application/merge-patch+json',
        "Authorization": f"Bearer {token}",
    }
    if status_set_replicas == None:
        status_payload = {
            "status": {
                'type': status_type,
                'status': status_status,
                'last_transition_time': datetime.datetime.utcnow().isoformat() + "Z",
                'message': status_message
            }
        }
    else:
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


def set_replica(tbase_name,tbase_namespace , count_of_replica ):
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



def set_status(tbase_name, tbase_namespace ,status_status):
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


def set_deployment_replica(deployment_name,deployment_namespace,count_of_replica):
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

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
