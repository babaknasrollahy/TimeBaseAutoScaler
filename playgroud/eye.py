import requests
import json
import datetime


#unavailableReplicas
#availableReplicas
#readyReplicas
#updatedReplicas
#replicas
# Define the API server URL and token for authentication
def eye_main():
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
    # Watch for changes in Deployments
    tbas_response = requests.get(
        #f"{api_server}/apis/apps/v1/namespaces/default/deployments",
        f"{api_server}/apis/sre.exalab.co/v1/timebaseautoscaler",
        headers=headers,
        verify=False,  # Set verify=True if you have a valid SSL certificate
        # stream=True  # Enable streaming for watch
    )

    dep_response = requests.get(
        f"{api_server}/apis/apps/v1/namespaces/default/deployments",
        #f"{api_server}/apis/sre.exalab.co/v1/timebaseautoscaler",
        headers=headers,
        verify=False,  # Set verify=True if you have a valid SSL certificate
        # stream=True  # Enable streaming for watch
    )
    # print(response.json())
    result_list = []
    all_items = tbas_response.json().get("items")
    for item in all_items :
        tbas_name = item.get("metadata").get("name")
        tbas_namespace = item.get("metadata").get("namespace")
        item = item.get("spec")
        deployment_name = item.get("deploymentName")
        scale_down_replica = item.get("scaleDownReplica")
        scale_down_time = item.get("scaleDownTime")
        scale_up_replica = item.get("scaleUpReplica")
        scale_up_time = item.get("scaleUpTime")
        if item.get("targetNodes"):
            target_nodes = item.get("targetNodes")
        else:
            target_nodes = "all_available_nodes"
        if item.get("waveOfScale"):
                wave_of_scale = item.get("waveOfScale")
        else:
            wave_of_scale = 10
        if item.get("status") :
            print("in the if ")
            status_set_replica = item.get("status").get("set_replicas")
            status_type = item.get("status").get("type")
            status_status = item.get("status").get("status")
            status_last_transition_time= item.get("status").get("last_transition_time")
            status_message= item.get("status").get("message")
        else:
            status_set_replica = None
            status_type = None
            status_status = None
            status_last_transition_time = None
            status_message = None
        dep_response = requests.get(
            f"{api_server}/apis/apps/v1/namespaces/{tbas_namespace}/deployments/{deployment_name}",
            #f"{api_server}/apis/sre.exalab.co/v1/timebaseautoscaler",
            headers=headers,
            verify=False,  # Set verify=True if you have a valid SSL certificate
            # stream=True  # Enable streaming for watch
        )
    #     dep_replicas = dep_response.json().get(items)[0].get("status").get("replicas")
        dep_replicas = dep_response.json().get("status").get("replicas")
        dep_updated_replicas = dep_response.json().get("status").get("updatedReplicas")
        dep_ready_replicas = dep_response.json().get("status").get("readyReplicas")
        dep_available_replicas = dep_response.json().get("status").get("availableReplicas")
        dep_unavailable_replicas = dep_response.json().get("status").get("unavailableReplicas")
        result_dict = {"tbas_name": tbas_name, "tbas_namespace": tbas_namespace,"deployment_name": deployment_name, "scale_down_replica": scale_down_replica, "scale_down_time": scale_down_time, "scale_up_replica": scale_up_replica, "scale_up_time": scale_up_time, "target_nodes": target_nodes, "wave_of_scale": wave_of_scale, "status": {"current_replicas": dep_replicas, "ready_replicas": dep_ready_replicas, "available_replicas": dep_available_replicas, "unavailable_replicas": dep_unavailable_replicas, "set_replica": status_set_replica, "type": status_type, "status": status_status, "last_transition_time": status_last_transition_time, "message": status_message}}
        result_list.append(result_dict)


    #     status_payload = {
    #         "status": {
    #             "currentReplicas": 10,
    #             "scaleDownReplicas": 5,
    #             "scaleUpReplicas": 10,
    #             "conditions": [
    #                 {
    #                     "type": "running",
    #                     "status": "ok",
    #                     "lastTransitionTime": "2020-11-12T00:00:00Z",
    #                     "message": "Scaling operation is in progress."
    #                 }
    #             ]
    #         }
    #     }
    #     test = response = requests.patch(
    #         # f"{api_server}/apis/apps/v1/namespaces/{namespace}/deployments",
    #         f"{api_server}/apis/sre.exalab.co/v1/namespaces/default/timebaseautoscaler/first-test/status",
    #         headers=headers2,
    #         verify=False,
    #         data=json.dumps(status_payload)  # Set verify=True if you have a valid SSL certificate
    #     )
        # print(deployment_name, scale_down_replica , scale_up_replica, scale_down_time , scale_up_time, target_nodes, wave_of_scale)
        # print(all_items[index].get("status"))
        # print(datetime.datetime.now().strftime("%D-%H:%M:%S"))
        # print("test", test)

    return result_list


def sample_eye():
    final_list = []
    with open("./test-opjects.txt" , "r") as file:
        val = file.readlines()
        for item in val :
            if item == "\n":
                print("#######################################33")
            else: 
                item = json.loads(item)
                final_list.append(item)
    return final_list