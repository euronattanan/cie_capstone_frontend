from urllib import response
from flask import Flask, request, render_template, url_for
from flask_cors import CORS
import qrcode

app = Flask(__name__, template_folder='templates')
CORS(app, resources={r"/*":{"origins": "*"}})
BASEURL = 'http://127.0.0.1:5000/'

@app.route('/', methods=['POST','GET'])
def index():
    return "Hello world"
@app.route('/displayqrcode', methods=['GET','POST'])
def qr():
    user_data = request.form.get("firstname")
    # qr = qrcode.make(user_data)
    # qr.save("qrcode.png")
    print("User Data: ", user_data)
    return render_template("test.html", qr_img = "/qrcode.png")
    # return (BASE + url_for('.qr'))
    # return user_data

if __name__ == "__main__":
    app.run(debug=True)