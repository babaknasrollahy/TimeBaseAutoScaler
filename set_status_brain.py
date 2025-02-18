import json
from datetime import datetime, timedelta

def findout_status(up_time, down_time):
    scale_up_time = up_time.split(":")
    scale_up_time = datetime.strptime(f"{scale_up_time[0]}:{scale_up_time[1]}", "%H:%M") - datetime(1900, 1, 1)

    scale_down_time = down_time.split(":")
    scale_down_time = datetime.strptime(f"{scale_down_time[0]}:{scale_down_time[1]}", "%H:%M") - datetime(1900, 1, 1)

    now_time = datetime.now().strftime("%H:%M").split(":")
    now_time = datetime.strptime(f"{now_time[0]}:{now_time[1]}","%H:%M") - datetime(1900, 1, 1)

    if scale_up_time > scale_down_time :
        scale_down_time = scale_down_time + timedelta(days=1)
    if (now_time < scale_up_time) and (now_time < scale_down_time):
        now_time = now_time + timedelta(days=1)
    if ( scale_up_time < now_time ) and ( now_time < scale_down_time ) :
        return "ScaleUp"
    else:
        return "ScaleDown"
    # After 24:00 the now_time is smaller than scale_up_time, and result is the function return False always . 
    # val = f"{now_time[0]}"
    # while True:
    #     if int(val) == int(scale_up_time[0]):
    #         return True
    #     else:
    #         if int(val) < int(scale_down_time[0]):
    #            if val != "23" :
    #                val = f"{int(val) + 1}"
    #             else:




# def set_status():
#     with open("./objects.txt" , "r") as file :
#         val = file.readlines()
#     for item in val:
#         data = json.loads(item)
#         tbas_name = "test"
#         deployment_name =  data.get("deployment_name")
#         scale_down_replica = data.get("scale_down_replica")
#         scale_down_time = data.get("scale_down_time")
#         scale_up_replica = data.get("scale_up_replica")
#         scale_up_time = data.get("scale_up_time")
#         try:
#             status =  data.get("status").get("status")
#             type = data.get("status").get("type")
#         except: 
#             status = "Doesn't set yet ."
#             pass
#         i = findout_status(scale_up_time, scale_down_time)
#         if status == "running" :
#             if (i == False and type == "ScaleDown") or (i == True and type == "ScaleUp"):
#                 continue
#             else: 
#                 pass
#         if (scale_down_time == -1 or scale_down_replica == -1 or scale_up_time == -1) and scale_up_replica != -1 :
#             print("$$$$$$$$$$$$$$")
#             pass # setting status=running and type=ScaleUp
#         elif scale_down_time != -1 and scale_up_time != -1 and scale_down_replica != -1 and scale_up_replica != -1 : 
#             print("---------------")
#             i = findout_status(scale_up_time, scale_down_time) 
#             if i == True:
#                 print("scale_up")
#                 pass # setting status=running and type=ScaleUp
#             else:
#                 print("scale_down")
#                 pass # setting status=running and type=ScaleDown
#         print(f"{tbas_name} {deployment_name} {scale_down_replica} {scale_down_time} {scale_up_replica} {scale_up_time} {status}")
#     return True




def set_status(tbase_dict):
        tbas_name = tbase_dict.get("tbas_name")
        tbase_namespace = tbase_dict.get("tbas_namespace")
        deployment_name =  tbase_dict.get("deployment_name")
        scale_down_replica = tbase_dict.get("scale_down_replica")
        scale_down_time = tbase_dict.get("scale_down_time")
        scale_up_replica = tbase_dict.get("scale_up_replica")
        scale_up_time = tbase_dict.get("scale_up_time")
        try:
            status =  tbase_dict.get("status").get("status")
            status_type = tbase_dict.get("status").get("type")
            current_replica = tbase_dict.get("status").get("current_replicas")

            has_status = True
        except: 
            status = "Doesn't set yet ."
            has_status = False
            pass
        # i = findout_status(scale_up_time, scale_down_time)
        # if status == "running" :
        #     if (i == "ScaleDown" and type == "ScaleDown") or (i == "ScaleUp" and type == "ScaleUp"):
        #         pass
        #     else: 
        #         pass
        if status == "running":
            return None
        elif status == "complete":
            if (scale_down_time == -1 or scale_down_replica == -1 or scale_up_time == -1) and scale_up_replica != -1 :
                # return f"{tbas_name}---{tbase_namespace}---ignore"
                pass # Ignore this tbase
            elif scale_down_time != -1 and scale_up_time != -1 and scale_down_replica != -1 and scale_up_replica != -1 : 
                print("---------------")
                i = findout_status(scale_up_time, scale_down_time) 
                if i == "ScaleUp" and status_type == "ScaleDown":
                    print("scale_up")
                    return f"{tbas_name}---{tbase_namespace}---ScaleUp"
                    pass # setting status=running and type=ScaleUp
                elif i == "ScaleDown" and status_type == "ScaleUp":
                    print("scale_down")
                    return f"{tbas_name}---{tbase_namespace}---ScaleDown" 
        elif status == "error" : 
            # ignore this tbase
            return None      
        
        # elif status == "debug":
        #     if (scale_down_time == -1 or scale_down_replica == -1 or scale_up_time == -1) and scale_up_replica != -1 :
        #         print("$$$$$$$$$$$$$$")
        #         pass # setting status=running and type=ScaleUp
        #     elif scale_down_time != -1 and scale_up_time != -1 and scale_down_replica != -1 and scale_up_replica != -1 : 
        #         print("---------------")
        #         i = findout_status(scale_up_time, scale_down_time) 
        #         if i == "ScaleUp":
        #             print("scale_up")
        #             return f"{tbas_name}---{tbase_namespace}---ScaleUp"
        #             pass # setting status=running and type=ScaleUp
        #         else:
        #             print("scale_down")
        #             return f"{tbas_name}---{tbase_namespace}---ScaleDown"
        #             pass # setting status=running and type=ScaleDown
                
        else:
            # only scale_up set 
            if (scale_down_time == -1 or scale_down_replica == -1 or scale_up_time == -1) and scale_up_replica != -1 :
                print("$$$$$$$$$$$$$$")
                pass # setting status=running and type=ScaleUp
            elif scale_down_time != -1 and scale_up_time != -1 and scale_down_replica != -1 and scale_up_replica != -1 : 
                print("---------------")
                i = findout_status(scale_up_time, scale_down_time) 
                if i == "ScaleUp" :
                    if status == None:
                        print("scale_up")
                        return f"{tbas_name}---{tbase_namespace}---ScaleUp---{current_replica}"
                        pass # setting status=running and type=ScaleUp
                    else:
                        print("scale_up")
                        return f"{tbas_name}---{tbase_namespace}---ScaleUp"
                else:
                    if status == None :
                        print("scale_down")
                        return f"{tbas_name}---{tbase_namespace}---ScaleDown---{current_replica}"
                        pass # setting status=running and type=ScaleDown
                    else:
                        print("scale_down")
                        return f"{tbas_name}---{tbase_namespace}---ScaleDown"
                        pass # setting status=running and type=ScaleDown 
            # print(f"{tbas_name} {deployment_name} {scale_down_replica} {scale_down_time} {scale_up_replica} {scale_up_time} {status}")
