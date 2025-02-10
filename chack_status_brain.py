import json
from set_status_brain import findout_status
def check_status():
    with open("./objects.txt" , "r") as file :
        val = file.readlines()
    for item in val:
        data = json.loads(item)
        tbas_name = data.get("tbas_name")
        deployment_name =  data.get("deployment_name")
        scale_down_replica = data.get("scale_down_replica")
        scale_down_time = data.get("scale_down_time")
        scale_up_replica = data.get("scale_up_replica")
        scale_up_time = data.get("scale_up_time")
        if (scale_up_replica <= scale_down_replica) and (scale_up_replica - scale_down_replica < wave_of_scale):
            return "error. There is a bug in replica count or wave of scale that you set"
        wave_of_scale = data.get("wave_of_scale")
        target_nodes = data.get("target_nodes")
        try:
            status =  data.get("status").get("status")
            type = data.get("status").get("type")
            current_replica =  data.get("status").get("current_replica")
            set_replica = data.get("status").get("set_replica")
            last_transition_time = data.get("status").get("last_transition_time")
            message = data.get("status").get("message")
        except:
            continue

        if status == "running" :
            check_type = findout_status(scale_up_time, scale_down_time)
            if ( check_type == True and type == "ScaleUp" ) :
                if message != "1": # It sets by replicas checker and return 1 if any of pods has pending stat.
                    if (current_replica == set_replica) : 
                        if (scale_up_replica > current_replica):
                            if ( scale_up_replica - current_replica >= wave_of_scale):
                                # Scale up based on wave_of_scale
                                pass
                            else:
                                # Scale up based on (scalue_up_replica - current_replica)
                                pass
                        else:
                            # Setting "complete" in status section . 
                            pass    
                    else:
                        # Check set_replica from hand and Set again if doesn't set yet . 
                        pass
                else:
                    # Some pods is not health or are in pending stat . So sleep some seconds and check again.
                    pass
            elif (check_type == False and type == "ScaleDown"):
                if message != "1": # It sets by replicas checker and return 1 if any of pods has pending stat.
                    if (current_replica == set_replica) : 
                        if (current_replica > scale_down_replica ):
                            if ( current_replica - scale_down_replica >= wave_of_scale):
                                # Scale down based on wave_of_scale
                                pass
                            else:
                                # Scale down based on (current_replica - scale_down_replica)
                                pass
                        else:
                            # Setting "complete" in status section . 
                            pass    
                    else:
                        # Check set_replica from hand and Set again if doesn't set yet . 
                        pass
                else:
                    # Some pods is not health or are in pending stat . So sleep some seconds and check again.
                    pass
        else:        
            # The status is not "running" , so ignore this one . 
            pass
                            
                            

            print("ok") 
            print(check_type , type , tbas_name)


    return f"{tbas_name}  {deployment_name}  {scale_down_replica}  {scale_down_time}  {scale_up_replica}  {scale_up_time}  {status}  {type}  {current_replica}  {set_replica}  {last_transition_time}  {message} {target_nodes} {wave_of_scale}"

print(check_status())