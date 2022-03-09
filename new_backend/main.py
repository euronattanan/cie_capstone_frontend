from urllib import response
from flask import Flask, request, render_template, url_for
from flask_cors import CORS
import uuid

# app = Flask(__name__, template_folder='templates')
app = Flask(__name__, template_folder='/templates', static_url_path='/static')
CORS(app, resources={r"/*":{"origins": "*"}})
BASEURL = 'http://127.0.0.1:5000'

user_data = {}

@app.route('/', methods = ['GET','POST'])
def index():
    print("user_dict: ", user_data)
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        id = uuid.uuid4()
        print("id: ", id)
        user_data[str(id)] = data
        print("user_data: ", user_data)
        return {1: data}
    else:
        return 'Hello world'


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)