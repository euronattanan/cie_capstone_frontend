import json
import time

def json_to_list(jsonData):
    #replace single quote with double quote (syntax purpose)
    str = jsonData.replace("\'","\"")

    #load json
    jsonDict = json.loads(str)

    #loop through json and append each value to a list
    data_to_write = []
    for key in jsonDict["data"][0]:
        data_to_write.append(jsonDict["data"][0][key])
        # print(jsonDict["data"][0][key])
    return data_to_write
