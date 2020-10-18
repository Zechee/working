from flask_restful import fields, reqparse, inputs
from models.logitem import Logitem

paginate_fields = {
    'total': fields.Integer,
    'pageSize': fields.Integer,
    'current': fields.Integer
}

logitem_fields = {
    'id': fields.Integer,
    'work_hour': fields.Integer,
    'user_id': fields.Integer,
    'content': fields.String,

    'created_at': fields.String
}

logitem_list_fields = {
    'pagination': fields.Nested(paginate_fields),
    'list': fields.List(fields.Nested(logitem_fields))
}

sortable_fields = ['id', 'work_hour', 'user_id', 'content', ]

logitem_post_parser = reqparse.RequestParser()
logitem_post_parser.add_argument('work_hour', type=int)
logitem_post_parser.add_argument('user_id', type=int)
logitem_post_parser.add_argument('content', type=str)


logitem_update_parser = reqparse.RequestParser()
logitem_update_parser.add_argument('work_hour', type=int)
logitem_update_parser.add_argument('user_id', type=int)
logitem_update_parser.add_argument('content', type=str)



logitem_query_parser = reqparse.RequestParser()
logitem_query_parser.add_argument('work_hour', type=int)
logitem_query_parser.add_argument('user_id', type=int)
logitem_query_parser.add_argument('content', type=str)



logitem_query_parser.add_argument('orderby', type=str, default='id')
logitem_query_parser.add_argument('desc', type=int, default=0)
logitem_query_parser.add_argument('page', type=int)
logitem_query_parser.add_argument('pagesize', type=int)

def make_conditions(conditions, args):
    if args['work_hour'] is not None:
        conditions.append(Logitem.work_hour.like('%'+args['work_hour']+'%'))
    if args['user_id'] is not None:
        conditions.append(Logitem.user_id.like('%'+args['user_id']+'%'))
    if args['content'] is not None:
        conditions.append(Logitem.content==args['content'])

    return conditions

def update_all_fields(args, o):
    if args['work_hour']:
        o.work_hour = args['work_hour']
    if args['user_id']:
        o.user_id = args['user_id']
    if args['content']:
        o.content = args['content']

    return o