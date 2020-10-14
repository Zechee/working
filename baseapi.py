from werkzeug.exceptions import HTTPException
from flask_restful import Api

class BaseApi(Api):
    def handle_error(self, e):
        code = 500
        msg = str(e)
        if isinstance(e, HTTPException):
            code = e.code
            msg = e.data
        
        res = { "code": code, "msg": msg }
        return res
    # pass