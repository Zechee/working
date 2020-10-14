from app import jwt, app
from werkzeug.exceptions import HTTPException

# 处理全局未授权错误
@jwt.unauthorized_loader
def handle_unauthorized_error(e):
    res = { "code": 401, "msg": str(e) }
    return res

@app.errorhandler(Exception)
def handle_error(e):
    code = 500
    msg = str(e)
    if isinstance(e, HTTPException):
        code = e.code
        msg = e.data
    
    res = { "code": code, "msg": msg }
    return res

