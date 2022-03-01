from urllib import response
from flask import Flask, request, render_template, url_for
from flask_cors import CORS
import qrcode
import uuid

# app = Flask(__name__, template_folder='templates')
app = Flask(__name__, template_folder='templates', static_url_path='/static')
CORS(app, resources={r"/*":{"origins": "*"}})
BASEURL = 'http://127.0.0.1:5000'

user_data = {}

@app.route('/', methods = ['GET', 'POST'])
def index():
    print("user_dict: ", user_data)
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        id = uuid.uuid4()
        print("id: ", id)
        user_data[str(id)] = data
        print("user_data: ", user_data)
        return {"data" : (BASEURL + '/getqrcode' + '/' + str(id))}
    else:
        return "Hello world"

@app.route('/getqrcode/<id>')
def retQr(id):
    text = ("Your id is: ", str(id))
    img = qrcode.make(user_data[id])
    img.save("./static/" + str(id) + ".png")
    img_name = str(id) + ".png"
    return render_template("test.html", data = text, image_name = img_name)

if __name__ == "__main__":
    app.run(debug=True)