# from functools import wraps
# def max_res(a_func):
#     @wraps(a_func)
#     def return_res():
#         max_res_d(a_func())
#     return return_res()


# def max_res_d(result,code='200',errmsg=None):
def max_res(result, code=200, errmsg=None):
    res = {}
    if errmsg == None:
        res = {'code': code, 'data': result}
    # TODO: 需要优化代码
    else:
        res = {'code': code, 'msg': errmsg, 'data': result}
    return res