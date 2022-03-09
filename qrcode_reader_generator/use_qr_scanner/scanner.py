import pyrebase
import json 
from datetime import date, datetime 

#firebase configuration variables
firebaseConfig = {
  "apiKey": "AIzaSyCNrL7UCpZ4L-QGG9E_kjJQ_bxY1d4BGlw",
  "authDomain": "novid19-screening-system.firebaseapp.com",
  "databaseURL": "https://novid19-screening-system-default-rtdb.firebaseio.com",
  "projectId": "novid19-screening-system",
  "storageBucket": "novid19-screening-system.appspot.com",
  "messagingSenderId": "310126395740",
  "appId": "1:310126395740:web:8597fa89e9847870204199"
}

#initializing firebase app and database
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

scanning = 1

while scanning:
    qr_input = input("----Waiting for QR Code input-----\n")
    date_now = str(date.today())
    time_now = str(datetime.now().strftime("%H:%M:%S"))

    if qr_input == "exit" or qr_input =="q":
        print("Exiting program...")
        break

    json_data = json.loads(qr_input)
    user_data = {
        "firstname": json_data["firstName"],
        "lastname": json_data["lastName"],
        "contact": json_data["contact"],
        "vaccineNum": json_data["numberOfVaccines"],
        "firstDose": json_data["doses"][0],
        "secondDose": json_data["doses"][1],
        "thirdDose": "none",
        "date": date_now,
        "time": time_now
    }

    if len(json_data["doses"]) > 2:
        user_data["thirdDose"] = json_data["doses"][2]

    db.child("user_data").push(user_data)
