import pyrebase
import json 

firebaseConfig = {
  "apiKey": "AIzaSyCNrL7UCpZ4L-QGG9E_kjJQ_bxY1d4BGlw",
  "authDomain": "novid19-screening-system.firebaseapp.com",
  "databaseURL": "https://novid19-screening-system-default-rtdb.firebaseio.com",
  "projectId": "novid19-screening-system",
  "storageBucket": "novid19-screening-system.appspot.com",
  "messagingSenderId": "310126395740",
  "appId": "1:310126395740:web:8597fa89e9847870204199"
}

firebase = pyrebase.initialize_app(firebaseConfig)

text = '{"firstName":"Euro","lastName":"Euro","contact":"Euro","numberOfVaccines":2,"doses":["Pfizer","Pfizer"]}'
dict = {"firstName":"Euro","lastName":"Euro","contact":"Euro","numberOfVaccines":2,"doses":["Pfizer","Pfizer"]}


db = firebase.database()

scanning = 1

while scanning:
    qr_input = input("----Waiting for QR Code input-----\n")
    json_data = json.loads(qr_input)
    user_data = {
        "firstname": json_data["firstName"],
        "lastname": json_data["lastName"],
        "contact": json_data["contact"],
        "vaccineNum": json_data["numberOfVaccines"],
        "firstDose": json_data["doses"][0],
        "secondDose": json_data["doses"][1],
    }
    if len(json_data["doses"]) > 2:
        user_data["thirdDose"] = json_data["doses"][2]

    db.child("user_data").push(user_data)
