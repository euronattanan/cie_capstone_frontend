import json
import time

def json_to_excel(excelFileName, jsonData):
    file = excelFileName
    print("file",file)
    f = open(file,"a")
    str = jsonData.replace("\'","\"")
    jsonDict = json.loads(str)
    data_to_write = ""
    for key in jsonDict["data"][0]:
        data_to_write += jsonDict["data"][0][key]+","
        print(jsonDict["data"][0][key])
    f.write("\n")
    f.write(data_to_write)
    time.sleep(5)
    f.close()

