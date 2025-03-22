## This is the main of tbas controller, it is going to handle all component and feachers .
import time
from check_status_brain import check_status
import eye 
from set_status_brain import set_status
import hand
import logging
import os

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='########[%(levelname)s]########\n[%(asctime)s]\n[%(message)s]\n#######################\n',
    handlers=[logging.StreamHandler()]  # Writes to stdout
)

proper_sleep_time = int(os.environ.get("sleep_time"))
while True :
    start_time = time.time()
    ## First step - getting data from eyes :
    # call eye function to create a dictionary from all datas in etcd .
    all_tbases = eye.eye_main() 
    ## Second step - set running status for each one is in ScaleUP or ScaleDown time . 
    # (function only returns new running tbas name and namespace)
    # call set_status function to find new running tbases :
    for tbase in all_tbases:
        # checking for any problem in tbase and its releated deployment
        if type(tbase) == str:
            error = tbase.split("---")
            if error[0] == "error_deployment_wrong":
              error_message = f"""
**Error** There is problem in tbase: 
tbase-name: {error[1]}
tbase_namespace: {error[3]}
deployment: {error[2]}
**Note**: It seems you have a wrong *deployment_name* in your tbase. Please check and fix it !!
"""
              logging.error(error_message)
              continue
        val = set_status(tbase)
        if val != None :
            val = val.split("---")
        else: 
            continue
        #=> if new running exist ----> call `hand` function to change status of tbas
        if val != [] :
            logging.info(f"New tbase send to *running* state\ntabse-name: {val[0]}\ntbase_namespace: {val[1]}")
            if val[3]:
                status_set_replica = int(val[3])
                hand.set_status_and_type(status_set_replica,val[2],"running","Status section fill by set_status_brain",val[0], val[1])
            else:
                hand.set_status_and_type(None,val[2],"running","Status section fill by set_status_brain",val[0], val[1])

        #=> if doesn't exit -----> continue 
        else:
            continue

    ## Third step - check running tbases and do something :
    # call `check_status` function . it will be return several orders :
    for tbase in all_tbases:
        if type(tbase) == str:
            continue
        order = check_status(tbase)
        if order == None:
            # logging.info("There was no running tbase")
            continue
        order = order.split("---")
        if (order[0] == "ScaleUp") or (order[0] == "ScaleDown"):
            # scale up ----> tbase: order[0] , count: order[2]
            logging.info(f"*{order[0]}*, *{order[4]}* scaled to *{order[3]}*")
            hand.set_replica(order[1],order[2], int(order[3]))
            hand.set_deployment_replica(order[4], order[2], int(order[3]))
            pass
        elif order[0] == "setting":
            # status of tbase need to be change . tbase: order[0] , status: order[2]
            logging.warning(f"The *status* of *{order[1]}* tbase changed to *{order[3]}*")
            hand.set_status(order[1], order[2], order[3])
            pass
        elif order[0] == "pending_state":
            # It's the pending state . tbase: order[0]
            logging.warning(f"The *{order[1]}* tbase is in *pending* state")
            pass
        elif order[0] == "warning":
            if order[3] == "different_eplicas" :
                if order[4] == "tbase_replica_only":
                    print("warning ----> different replica in tbase. fixing it ...")
                    logging.critical("Different replicas in tbase side !!\nI'm trying to fix it ...")
                    hand.set_replica(order[1],order[2],int(order[5]))
                elif order[4] == "deployment_replica_only":
                    logging.critical("Different replicas in deployment side !!\nI'm trying to fix it ...")
                    hand.set_deployment_replica(order[6],order[2],int(order[5]))
                    pass
            elif order[3] == "different type" :
                # status need to be change to debug . tbase: [0], status: [3]
                logging.critical("Different type problem!!\nChanging type to debug for fixing ...")
                hand.set_status(order[1], order[2], order[4])
                pass
    #=> 1 ) ScaleUp - count
    #=> 2 ) ScaleDown - count
    #=> 3 ) Setting complete in status
    #=> 4 ) Warning - Debug sulotion ( 2-3 optionn )
    #=> 6 ) None - no running tbas find 
    # Do proper task by hand



    ## Forth step - sleep zZ :
    # A dynamic sleep . 
    end_time = time.time()
    duration_time = int(end_time - start_time)
    if 40 <= duration_time < 60 :
        logging.warning("Duration time was more than 40s . please check it")
    elif duration_time >= 60 :
        logging.critical("Duration time was more than 60s . please check it")
    elif duration_time > proper_sleep_time :
        pass
    elif duration_time < proper_sleep_time :
        time.sleep(proper_sleep_time - duration_time)
