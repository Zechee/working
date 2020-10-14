from flask import Flask, jsonify, request, json
from flask_bcrypt import Bcrypt
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from flask_migrate import Migrate

from werkzeug.exceptions import HTTPException, InternalServerError
from werkzeug.exceptions import default_exceptions

from config import app_config
from baseapi import BaseApi

config_name = 'development'
bcrypt = Bcrypt()

app = Flask(__name__)
api = BaseApi(app, catch_all_404s=True)
app.config.from_object(app_config[config_name])
db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)
bcrypt.init_app(app)

from utils.error_handle import *
for ex in default_exceptions:
    app.register_error_handler(ex, handle_error)

from resourses.users_resource import UsersResource
from resourses.session.login_resource import LoginResource
 

api.prefix = '/api'
api.add_resource(LoginResource, '/auth/login')
api.add_resource(UsersResource, '/users', '/users/<int:user_id>')

if __name__ == '__main__':
    app.run()