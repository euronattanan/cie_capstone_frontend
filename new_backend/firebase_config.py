import pyrebase

config = {
    "apiKey": "AIzaSyCNrL7UCpZ4L-QGG9E_kjJQ_bxY1d4BGlw",
    "authDomain": "novid19-screening-system.firebaseapp.com",
    "projectId": "novid19-screening-system",
    "storageBucket": "novid19-screening-system.appspot.com",
    "messagingSenderId": "310126395740",
    "appId": "1:310126395740:web:8597fa89e9847870204199"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

