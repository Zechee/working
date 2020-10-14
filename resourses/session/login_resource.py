from flask_restful import Resource, reqparse, request
from flask_jwt_extended.utils import create_access_token
from app import db, app
from utils.util import max_res
from models.user import User
import datetime

login_parser = reqparse.RequestParser()
login_parser.add_argument('username',type=str,required=True,help='username is required.')
login_parser.add_argument('password',type=str,required=True,help='Password is required.')

class LoginResource(Resource):
    def post(self):
        args = login_parser.parse_args()
        username = args['username']
        password = args['password']

        user = User.find_by_username(username=username)
        if not user or not user.check_password(password):
            return max_res('',401,'Invalid username or password')

        # Identity can be any data that is json serializable
        expires = datetime.timedelta(days=10)
        access_token = create_access_token(user.id, expires_delta=expires)
        return max_res({'token':access_token}), 200

