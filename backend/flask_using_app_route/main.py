from urllib import response
from flask import Flask, request, send_file
from flask_cors import CORS

import qrcode

from io import BytesIO

app = Flask(__name__)
CORS(app)

@app.route('/getqrcode', methods=['Post'])
def get_qr():
    buffer = BytesIO()
    user_data = request.form.get('user_data')
    qr = qrcode.make(user_data)
    qr.save(buffer)
    buffer.seek(0)

    response = send_file(buffer, mimetype='image/png')
    return response

if __name__ == "__main__":
    app.run()