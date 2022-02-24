from urllib import response
from flask import Flask, send_file, request
from flask_restful import Api, Resource, reqparse
from io import BytesIO
from numpy import require
import qrcode
# import uuid


app = Flask(__name__)
api = Api(app)

user_detail_post_args = reqparse.RequestParser()
user_detail_post_args.add_argument("information", type=str, help="Please send the user detail", required=True)



class GetQrCode(Resource):
    def post(self, user_id):
        args = user_detail_post_args.parse_args()
        # id = uuid.uuid1()
        buffer = BytesIO()

        qr = qrcode.make(args)
        qr.save(buffer)
        buffer.seek(0)

        response = send_file(buffer, mimetype='image/png')
        # return {int(id):args}
        return response

api.add_resource(GetQrCode, "/getqrcode/<int:user_id>")

if __name__ == "__main__":
    #set to true only at development phase 
    #set to false when in a production deployment
    app.run(debug=True)