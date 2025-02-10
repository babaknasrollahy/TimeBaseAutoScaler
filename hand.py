import json

def set_status_and_type(tbas_name, tbas_type, tbase_status):
    with open("./test-opjects.txt", "r") as file :
        data = file.readlines()
    i = 0
    for item in data:
        item = json.loads(item)
        if item.get("tbas_name") == tbas_name :
            item['status']['status'] = tbase_status
            item['status']['type'] = tbas_type
            data[i] = json.dumps(item) + "\n"
        i += 1
    with open("./test-opjects.txt" , "w") as file:
        file.writelines(data)
        file.close()
    return True




def set_replica(tbas_name,count):
    with open("./test-opjects.txt", "r") as file :
        data = file.readlines()
    i = 0
    for item in data:
        item = json.loads(item)
        if item.get("tbas_name") == tbas_name :
            val = item['status']['set_replica']
            val2 = item['status']['current_replica']
            item['status']['set_replica'] = int(val) + int(count)
            item['status']['current_replica'] = int(val2) + int(count)
            data[i] = json.dumps(item) + "\n"
        i += 1
    with open("./test-opjects.txt" , "w") as file:
        file.writelines(data)
        file.close()
    return True


def set_status(tbas_name, tbase_status):
    with open("./test-opjects.txt", "r") as file :
        data = file.readlines()
    i = 0
    for item in data:
        item = json.loads(item)
        if item.get("tbas_name") == tbas_name :
            item['status']['status'] = tbase_status
            data[i] = json.dumps(item) + "\n"
        i += 1
    with open("./test-opjects.txt" , "w") as file:
        file.writelines(data)
        file.close()
    return True