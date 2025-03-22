import requests
import centralize_config

# Define the API server URL and token for authentication
api_server , token = centralize_config.kube_config()
def eye_main():
    namespace = "default"
    headers = {
        "Authorization": f"Bearer {token}",
    }
    headers2 = {
        'Content-Type': 'application/merge-patch+json',
        "Authorization": f"Bearer {token}",
    }
    try:
        # Watch for changes in Deployments
        tbas_response = requests.get(
            #f"{api_server}/apis/apps/v1/namespaces/default/deployments",
            f"{api_server}/apis/sre.exalab.co/v1/timebaseautoscaler",
            headers=headers,
            verify=False,  # Set verify=True if you have a valid SSL certificate
            # stream=True  # Enable streaming for watch
        )
    except:
        return "**Error!!** There is a problem to connecting to kubernetes api-server. Please check your token"

    # print(response.json())
    result_list = []
    all_items = tbas_response.json().get("items")
    for item in all_items :
        tbas_name = item.get("metadata").get("name")
        tbas_namespace = item.get("metadata").get("namespace")
        spec_item = item.get("spec")
        deployment_name = spec_item.get("deploymentName")
        scale_down_replica = spec_item.get("scaleDownReplica")
        scale_down_time = spec_item.get("scaleDownTime")
        scale_up_replica = spec_item.get("scaleUpReplica")
        scale_up_time = spec_item.get("scaleUpTime")
        if spec_item.get("targetNodes"):
            target_nodes = spec_item.get("targetNodes")
        else:
            target_nodes = "all_available_nodes"
        if spec_item.get("waveOfScale"):
                wave_of_scale = spec_item.get("waveOfScale")
        else:
            wave_of_scale = 10
        if item.get("status") :
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
        try:
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
        except:
            result_list.append(f"error_deployment_wrong---{tbas_name}---{deployment_name}---{tbas_namespace}")


    return result_list


