## This is the main of tbas controller, it is going to handle all component and feachers .
import time
from check_status_brain import check_status
from eye import sample_eye
from set_status_brain import set_status
import hand
i = 1
while True :

    ## First step - getting data from eyes :
    # call eye function to create a dictionary from all datas in etcd .
    all_tbases = sample_eye() 


    ## Second step - set running status for each one is in ScaleUP or ScaleDown time . 
    # (function only returns new running tbas name and namespace)
    # call set_status function to find new running tbases :
    for tbase in all_tbases:
        val = set_status(tbase)
        if val != None :
            val = val.split("---")
        else: 
            print("before continue")
            continue
        #=> if new running exist ----> call `hand` function to change status of tbas
        if val != [] :
            print(f"{val[0]}-------{val[2]}")
            hand.set_status_and_type(None,val[2],"running","Status section fill by set_status_brain",val[0], val[1])
        #=> if doesn't exit -----> continue 
        else:
            print("before continue")
            continue

    ## Third step - check running tbases and do something :
    # call `check_status` function . it will be return several orders :
    for tbase in all_tbases:

        order = check_status(tbase)
        if order == None:
            print("There was not running tbase")
            continue
        print("============", order)
        order = order.split("---")
        if (order[0] == "ScaleUp") or (order[0] == "ScaleDown"):
            # scale up ----> tbase: order[0] , count: order[2]
            hand.set_replica(order[1],order[2], order[3])
            pass
        elif order[0] == "setting":
            # status of tbase need to be change . tbase: order[0] , status: order[2]
            hand.set_status(order[1], order[2], order[3])
            pass
        elif order[0] == "pending_state":
            # It's the pending state . tbase: order[0]
            print(order[1], "pending ...")
            pass
        elif order[0] == "warning":
            if order[3] == "different_eplicas" and order[4] == "":
                # main need to check replicas an fix it by hand. tbase: [0], current_rep: [3], set_rep: [4]
                print("warning-different_replica")
                pass
            elif order[3] == "different type" :
                # status need to be change to debug . tbase: [0], status: [3]
                hand.set_status(order[1], order[2], order[4])
                pass
    #=> 1 ) ScaleUp - count
    #=> 2 ) ScaleDown - count
    #=> 3 ) Setting complete in status
    #=> 4 ) Warning - Debug sulotion ( 2-3 optionn )
    #=> 6 ) None - no running tbas find 
    # Do proper task by hand



    ## Forth step - create log :
    # writing log about done tasks 
    print("-------------", i)
    time.sleep(15)
    i += 1

