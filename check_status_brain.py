import json
from set_status_brain import findout_status
def check_status(tbas_dict):
        tbas_name = tbas_dict.get("tbas_name")
        deployment_name =  tbas_dict.get("deployment_name")
        scale_down_replica = tbas_dict.get("scale_down_replica")
        scale_down_time = tbas_dict.get("scale_down_time")
        scale_up_replica = tbas_dict.get("scale_up_replica")
        scale_up_time = tbas_dict.get("scale_up_time")
        if (scale_up_replica <= scale_down_replica) and (scale_up_replica - scale_down_replica < wave_of_scale):
            return "error. There is a bug in replica count or wave of scale that you set"
        wave_of_scale = tbas_dict.get("wave_of_scale")
        target_nodes = tbas_dict.get("target_nodes")
        try:
            status =  tbas_dict.get("status").get("status")
            type = tbas_dict.get("status").get("type")
            current_replica =  tbas_dict.get("status").get("current_replica")
            set_replica = tbas_dict.get("status").get("set_replica")
            last_transition_time = tbas_dict.get("status").get("last_transition_time")
            message = tbas_dict.get("status").get("message")
        except:
            return "This tbas has not status section !!!"

        if status == "running" :
            check_type = findout_status(scale_up_time, scale_down_time)
            if ( check_type == "ScaleUp" and type == "ScaleUp" ) :
                if message != "1": # It sets by replicas checker and return 1 if any of pods has pending stat.
                    if (current_replica == set_replica) : 
                        if (scale_up_replica > current_replica):
                            if ( scale_up_replica - current_replica >= wave_of_scale):
                                # Scale up based on wave_of_scale
                                return f"{tbas_name}---ScaleUp---{wave_of_scale}"
                                pass
                            else:
                                # Scale up based on (scalue_up_replica - current_replica)
                                return f"{tbas_name}---ScaleUp---{scale_up_replica - current_replica}"
                                pass
                        else:
                            # Setting "complete" in status section . 
                            return f"{tbas_name}---setting---complete"
                            pass    
                    else:
                        # Check set_replica from hand and Set again if doesn't set yet . 
                        return f"{tbas_name}---warning---different replicas---{current_replica}---{set_replica}"
                        pass
                else:
                    # Some pods are not health or are in pending stat . So sleep some seconds and check again.
                    return f"{tbas_name}---pending state---sleep"
                    pass
            elif (check_type == "ScaleDown" and type == "ScaleDown"):
                if message != "1": # It sets by replicas checker and return 1 if any of pods has pending stat.
                    if (current_replica == set_replica) : 
                        if (current_replica > scale_down_replica ):
                            if ( current_replica - scale_down_replica >= wave_of_scale):
                                # Scale down based on wave_of_scale
                                return f"{tbas_name}---ScaleDown---{wave_of_scale}"
                                pass
                            else:
                                # Scale down based on (current_replica - scale_down_replica)
                                return f"{tbas_name}---ScaleDown---{current_replica - scale_down_replica}"
                                pass
                        else:
                            # Setting "complete" in status section . 
                            return f"{tbas_name}---setting---complete"
                            pass    
                    else:
                        # Check set_replica from hand and Set again if doesn't set yet . 
                        return f"{tbas_name}---warning---different replicas---{current_replica}---{set_replica}"
                        pass
                else:
                    # Some pods are not health or are in pending stat . So sleep some seconds and check again.
                    return f"{tbas_name}---pending state---sleep"
                    pass
            
            else:
                # There was a problem with status.type . It is not correct 
                return f"{tbas_name}---warning---different type---debug"
        else:        
            # The status is not "running" , so ignore this one .
            return None 
            pass

    # return f"{tbas_name}  {deployment_name}  {scale_down_replica}  {scale_down_time}  {scale_up_replica}  {scale_up_time}  {status}  {type}  {current_replica}  {set_replica}  {last_transition_time}  {message} {target_nodes} {wave_of_scale}"
