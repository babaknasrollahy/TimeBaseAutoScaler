import json
from set_status_brain import findout_status
import datetime
def check_status(tbas_dict):
        tbas_name = tbas_dict.get("tbas_name")
        tbase_namespace = tbas_dict.get("tbas_namespace")
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
            ready_replicas = tbas_dict.get("status").get("ready_replicas")
            available_replicas = tbas_dict.get("status").get("available_replicas")
            unavailable_replicas = tbas_dict.get("status").get("unavailable_replicas")
            set_replica = tbas_dict.get("status").get("set_replica")
            #2025-02-13T10:33:21.832299Z
            utc_time  = str(datetime.datetime.utcnow().isoformat())
            utc_time = dt_object = datetime.datetime.fromisoformat(utc_time).timestamp()
            last_transition_time = str(tbas_dict.get("status").get("last_transition_time")).split("Z")
            last_transition_time = dt_object = datetime.datetime.fromisoformat(last_transition_time).timestamp()

            message = tbas_dict.get("status").get("message")
        except:
            return "This tbas has not status section !!!"

        if status == "running" :
            check_type = findout_status(scale_up_time, scale_down_time)
            if ( check_type == "ScaleUp" and type == "ScaleUp" ) :
                if (ready_replicas == available_replicas == current_replica) and unavailable_replicas == None :
                    if (current_replica == set_replica) : 
                        if (scale_up_replica > current_replica):
                            if ( scale_up_replica - current_replica >= wave_of_scale):
                                # Scale up based on wave_of_scale
                                return f"ScaleUp---{tbas_name}---{tbase_namespace}---{set_replica + wave_of_scale}"
                                pass
                            else:
                                # Scale up based on (scalue_up_replica - current_replica)
                                return f"ScaleUp---{tbas_name}---{tbase_namespace}---{set_replica + (scale_up_replica - current_replica)}"
                                pass
                        else:
                            # Setting "complete" in status section . 
                            return f"setting---{tbas_name}---{tbase_namespace}---complete"
                            pass    
                    else:
                        # Check set_replica from hand and Set again if doesn't set yet . 
                        if current_replica > set_replica :
                            # Increasing set_replica only
                            return f"warning---{tbas_name}---{tbase_namespace}---different_replicas---tbase_replica_only---{current_replica}"  
                            pass
                        elif set_replica > current_replica :
                            if ( utc_time - last_transition_time ) <= 180 :
                                # sleep for times short than 3 minute
                                return f"pending_state---{tbas_name}"
                            else:
                                # Increasing Deployment Replica
                                return f"warning---{tbas_name}---{tbase_namespace}---different_replicas---deployment_replica_only---{set_replica}"
                else:
                    if ( utc_time - last_transition_time ) <= 300  :
                        # sleep
                        return f"pending_state---{tbas_name}"
                        pass
                    else: 
                        return f"setting---{tbas_name}---{tbase_namespace}---error"
                        pass

            elif (check_type == "ScaleDown" and type == "ScaleDown"):
                if (ready_replicas == available_replicas == current_replica) and unavailable_replicas == None:
                    if (current_replica == set_replica) : 
                        if (current_replica > scale_down_replica ):
                            if ( current_replica - scale_down_replica >= wave_of_scale):
                                # Scale down based on wave_of_scale
                                return f"ScaleDown---{tbas_name}---{tbase_namespace}---{set_replica - wave_of_scale}"
                                pass
                            else:
                                # Scale down based on (current_replica - scale_down_replica)
                                return f"ScaleDown---{tbas_name}---{tbase_namespace}---{set_replica - (current_replica - scale_down_replica)}"
                                pass
                        else:
                            # Setting "complete" in status section . 
                            return f"setting---{tbas_name}---{tbase_namespace}---complete"
                            pass    
                    else:
                        # Check set_replica from hand and Set again if doesn't set yet . 
                        if current_replica > set_replica :
                            # Decreasing dep_replica only
                            if ( utc_time - last_transition_time ) <= 180 :
                                # sleep for times short than 3 minute
                                return f"pending_state---{tbas_name}"
                            else:
                                # Decreasing Deployment Replica
                                return f"warning---{tbas_name}---{tbase_namespace}---different_replicas---deployment_replica_only---{set_replica}"
                        elif set_replica > current_replica :
                            return f"warning---{tbas_name}---{tbase_namespace}---different_replicas---tbase_replica_only---{current_replica}"


                else:
                    # Some pods are not health or are in pending stat . So sleep some seconds and check again.
                    if ( utc_time - last_transition_time ) <= 300  :
                        # sleep
                        return f"pending_state---{tbas_name}"
                        pass
                    else: 
                        return f"setting---{tbas_name}---{tbase_namespace}---error"
                    pass
            
            else:
                # There was a problem with status.type . It is not correct 
                return f"warning---{tbas_name}---{tbase_namespace}---different type---debug"
        else:        
            # The status is not "running" , so ignore this one .
            return None 
            pass

    # return f"{tbas_name}  {deployment_name}  {scale_down_replica}  {scale_down_time}  {scale_up_replica}  {scale_up_time}  {status}  {type}  {current_replica}  {set_replica}  {last_transition_time}  {message} {target_nodes} {wave_of_scale}"


test = {"tbas_name": "test", "deployment_name": "testdeployment", "scale_down_replica": 5, "scale_down_time": "23:10", "scale_up_replica": 100, "scale_up_time": "17:44", "target_nodes": "", "wave_of_scale": 35, "status": {"current_replica": 5, "set_replica": 5, "type": "ScaleDown", "status": "running", "last_transition_time": "2020-11-12T00:00:00Z", "message": "gfhf"}}

print(check_status(test))
