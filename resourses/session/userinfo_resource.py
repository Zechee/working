from flask_restful import Resource, reqparse, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db, app
from utils.util import max_res
from models.user import User
import datetime


class UserinfoResource(Resource):
    @jwt_required
    def get(self):
        current_userid = get_jwt_identity()
        print(current_userid)
        user = User.find_by_id(current_userid)
        if not user:
            return max_res('', 500, 'Invalid User'), 500
        res = {
            "id": user.id,
            "account": user.username,
            "name": user.name,
            "avatar": ""
        }
        return max_res(res)