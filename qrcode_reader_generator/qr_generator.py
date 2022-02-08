import qrcode
import json

file = "testdata2.json"
f = open(file)
jsonReader = json.load(f)
qr = qrcode.make(jsonReader)
qr.save("testqr.png")

# print(jsonReader)

