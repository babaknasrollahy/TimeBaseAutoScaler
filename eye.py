# import requests
import json
# import datetime

# # Define the API server URL and token for authentication
# api_server = "https://172.16.1.71:6443"
# namespace = "default"
# headers = {
#     "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6ImJPWkdJdUtBLThOcWpEM194bEFJeDRQY1ZfZHBCdzNuTEIybkJMTkRIREUifQ.eyJhdWQiOlsiaHR0cHM6Ly9rdWJlcm5ldGVzLmRlZmF1bHQuc3ZjLmNsdXN0ZXIubG9jYWwiLCJrM3MiXSwiZXhwIjoxNzU4OTc5MzE0LCJpYXQiOjE3Mjc0NDMzMTQsImlzcyI6Imh0dHBzOi8va3ViZXJuZXRlcy5kZWZhdWx0LnN2Yy5jbHVzdGVyLmxvY2FsIiwianRpIjoiZGQ2Mzc1MjMtN2U1YS00YmU5LTg0ZTItM2Q1NGQ1ZTBlMjhhIiwia3ViZXJuZXRlcy5pbyI6eyJuYW1lc3BhY2UiOiJkZWZhdWx0Iiwibm9kZSI6eyJuYW1lIjoibmx1dm0iLCJ1aWQiOiI1ZjcwYjM2Ni1hZTUwLTQ3NDktYTlmNy1lMGQwMGI3NGE0ODgifSwicG9kIjp7Im5hbWUiOiJuZ2lueCIsInVpZCI6IjU2MjI5NjVhLTExNWQtNDU2OC1iYzBmLTMyZjczMTY3MmY1NCJ9LCJzZXJ2aWNlYWNjb3VudCI6eyJuYW1lIjoiZGVmYXVsdCIsInVpZCI6ImJlYzBkNWE1LTUyOGItNDU2ZS1iZDFkLWY4YjcyZmVmMWFkMCJ9LCJ3YXJuYWZ0ZXIiOjE3Mjc0NDY5MjF9LCJuYmYiOjE3Mjc0NDMzMTQsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDpkZWZhdWx0OmRlZmF1bHQifQ.o_d2Nt9DFlObX559T_vYKeaGF6NmgLi3yPq6HgdRvZQfVfe_Kz3Ovz_21lc0GLOupP0vsbouIOPUl0DY3IJRLLmfQS-itiO3lVlHQwnGt3XU6aRhSKC26LELtrhKj1B3OveQEL5ODd2IyM6uGp0qErUB990jsYEVsJl2dp_f5wglOcBDg1cTXZDAVinxuQLD4Nb3LGrkyU5tddcafXGp3kT13VLsH748dAnyABtONyNS3tDE9gApfPyQyBqT9r-yhwIGblw9J0pjRw_2yfx8ygsGhhJZKIoiREw1t1GvUbzGNYQi_Ft0z8fuODTo5VleuxpS7-h9SAfUIvDgfgEM2Q",
# }
# headers2 = {
#     'Content-Type': 'application/merge-patch+json',
#     "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6ImJPWkdJdUtBLThOcWpEM194bEFJeDRQY1ZfZHBCdzNuTEIybkJMTkRIREUifQ.eyJhdWQiOlsiaHR0cHM6Ly9rdWJlcm5ldGVzLmRlZmF1bHQuc3ZjLmNsdXN0ZXIubG9jYWwiLCJrM3MiXSwiZXhwIjoxNzU4OTc5MzE0LCJpYXQiOjE3Mjc0NDMzMTQsImlzcyI6Imh0dHBzOi8va3ViZXJuZXRlcy5kZWZhdWx0LnN2Yy5jbHVzdGVyLmxvY2FsIiwianRpIjoiZGQ2Mzc1MjMtN2U1YS00YmU5LTg0ZTItM2Q1NGQ1ZTBlMjhhIiwia3ViZXJuZXRlcy5pbyI6eyJuYW1lc3BhY2UiOiJkZWZhdWx0Iiwibm9kZSI6eyJuYW1lIjoibmx1dm0iLCJ1aWQiOiI1ZjcwYjM2Ni1hZTUwLTQ3NDktYTlmNy1lMGQwMGI3NGE0ODgifSwicG9kIjp7Im5hbWUiOiJuZ2lueCIsInVpZCI6IjU2MjI5NjVhLTExNWQtNDU2OC1iYzBmLTMyZjczMTY3MmY1NCJ9LCJzZXJ2aWNlYWNjb3VudCI6eyJuYW1lIjoiZGVmYXVsdCIsInVpZCI6ImJlYzBkNWE1LTUyOGItNDU2ZS1iZDFkLWY4YjcyZmVmMWFkMCJ9LCJ3YXJuYWZ0ZXIiOjE3Mjc0NDY5MjF9LCJuYmYiOjE3Mjc0NDMzMTQsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDpkZWZhdWx0OmRlZmF1bHQifQ.o_d2Nt9DFlObX559T_vYKeaGF6NmgLi3yPq6HgdRvZQfVfe_Kz3Ovz_21lc0GLOupP0vsbouIOPUl0DY3IJRLLmfQS-itiO3lVlHQwnGt3XU6aRhSKC26LELtrhKj1B3OveQEL5ODd2IyM6uGp0qErUB990jsYEVsJl2dp_f5wglOcBDg1cTXZDAVinxuQLD4Nb3LGrkyU5tddcafXGp3kT13VLsH748dAnyABtONyNS3tDE9gApfPyQyBqT9r-yhwIGblw9J0pjRw_2yfx8ygsGhhJZKIoiREw1t1GvUbzGNYQi_Ft0z8fuODTo5VleuxpS7-h9SAfUIvDgfgEM2Q",
# }
# # Watch for changes in Deployments
# response = requests.get(
#     # f"{api_server}/apis/apps/v1/namespaces/{namespace}/deployments",
#     f"{api_server}/apis/sre.exalab.co/v1/namespaces/default/timebaseautoscaler",
#     headers=headers,
#     verify=False,  # Set verify=True if you have a valid SSL certificate
#     stream=True  # Enable streaming for watch
# )

# all_items = response.json().get("items")
# for index in range( 0, (len(all_items)) ):
#     item = all_items[index].get("spec")
#     deployment_name = item.get("deploymentName")
#     scale_down_replica = item.get("scaleDownReplica")
#     scale_down_time = item.get("scaleDownTime")
#     scale_up_replica = item.get("scaleUpReplica")
#     scale_up_time = item.get("scaleUpTime")
#     if item.get("targetNodes"):
#         target_nodes = item.get("targetNodes")
#     else:
#         target_nodes = "all_available_nodes"
#     if item.get("waveOfScale"):
#             wave_of_scale = item.get("waveOfScale")
#     else:
#         wave_of_scale = 10

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
#     print(deployment_name, scale_down_replica , scale_up_replica, scale_down_time , scale_up_time, target_nodes, wave_of_scale)
#     print(all_items[index].get("status"))
#     print(datetime.datetime.now().strftime("%D-%H:%M:%S"))
#     print("test", test)
#     # print(item)



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


