import qrcode
import json
import sys, os 

#open json file
file = "qrcode_reader_generator\data.json"
f = open(file)

#load json
jsonReader = json.load(f)

#call qrcode.make and parse the loaded json to create a qrcode from json data
qr = qrcode.make(jsonReader)

#save qr code as testqr.png
qr.save("testqr.png")

# print(jsonReader)
