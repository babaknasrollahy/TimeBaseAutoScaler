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

        if status == "running":
            return None
        elif status == "complete":
            if (scale_down_time == "-1" or scale_down_replica == -1 or scale_up_time == "-1") and scale_up_replica != -1 :
                return None
            elif (scale_down_time == "-1" or scale_up_replica == -1 or scale_up_time == "-1") and scale_down_replica != -1:
                 return None
                 pass # Ignore this tbase
            elif scale_down_time != -1 and scale_up_time != -1 and scale_down_replica != -1 and scale_up_replica != -1 : 
                i = findout_status(scale_up_time, scale_down_time) 
                if i == "ScaleUp" and status_type == "ScaleDown":
                    return f"{tbas_name}---{tbase_namespace}---ScaleUp"
                    pass # setting status=running and type=ScaleUp
                elif i == "ScaleDown" and status_type == "ScaleUp":
                    return f"{tbas_name}---{tbase_namespace}---ScaleDown" 
        elif status == "error" : 
            # ignore this tbase
            return None      
                
        else:
            # only scale_up set 
            if (scale_down_time == "-1" or scale_down_replica == -1 ) and scale_up_replica != -1  :
                if scale_up_time == "-1" :
                    # Scaling up as soon as create
                    if status == None:
                        return f"{tbas_name}---{tbase_namespace}---ScaleUp---{current_replica}"
                    else:
                        return f"{tbas_name}---{tbase_namespace}---ScaleUp"
                else:
                    # scaling up base on time
                    pass # setting status=running and type=ScaleUp

            elif (scale_up_replica == -1 or scale_up_time == "-1" ) and scale_down_replica != -1 :
                if scale_down_time == "-1" :
                    # Scaling donw as soon as create
                    if status == None :
                        return f"{tbas_name}---{tbase_namespace}---ScaleDown---{current_replica}"
                    else:
                        return f"{tbas_name}---{tbase_namespace}---ScaleDown"
                else:
                    #Scaling dons base on time
                    pass # setting status=running and type=ScaleDown

            elif scale_down_time != "-1" and scale_up_time != "-1" and scale_down_replica != -1 and scale_up_replica != -1 : 
                i = findout_status(scale_up_time, scale_down_time) 
                if i == "ScaleUp" :
                    if status == None:
                        return f"{tbas_name}---{tbase_namespace}---ScaleUp---{current_replica}"
                        pass # setting status=running and type=ScaleUp
                    else:
                        return f"{tbas_name}---{tbase_namespace}---ScaleUp"
                else:
                    if status == None :
                        return f"{tbas_name}---{tbase_namespace}---ScaleDown---{current_replica}"
                        pass # setting status=running and type=ScaleDown
                    else:
                        return f"{tbas_name}---{tbase_namespace}---ScaleDown"
                        pass # setting status=running and type=ScaleDown 
