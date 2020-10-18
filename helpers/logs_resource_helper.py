from flask_restful import fields, reqparse, inputs
from models.log import Log

paginate_fields = {
    'total': fields.Integer,
    'pageSize': fields.Integer,
    'current': fields.Integer
}

log_fields = {
    'id': fields.Integer,
    'date': fields.String,
    'user_id': fields.Integer,

    'created_at': fields.String
}


log_list_fields = {
    'pagination': fields.Nested(paginate_fields),
    'list': fields.List(fields.Nested(log_fields))
}

sortable_fields = ['id', 'date', 'user_id' ]

log_post_parser = reqparse.RequestParser()
log_post_parser.add_argument('date', type=str)
log_post_parser.add_argument('user_id', type=int)


log_update_parser = reqparse.RequestParser()
log_update_parser.add_argument('date', type=str)
log_update_parser.add_argument('user_id', type=int)



log_query_parser = reqparse.RequestParser()
log_query_parser.add_argument('date', type=str)
log_query_parser.add_argument('user_id', type=int)



log_query_parser.add_argument('orderby', type=str, default='id')
log_query_parser.add_argument('desc', type=int, default=0)
log_query_parser.add_argument('page', type=int)
log_query_parser.add_argument('pagesize', type=int)

def make_conditions(conditions, args):
    if args['date'] is not None:
        conditions.append(Log.date.like('%'+args['date']+'%'))
    if args['user_id'] is not None:
        conditions.append(Log.user_id.like('%'+args['user_id']+'%'))

    return conditions

def update_all_fields(args, o):
    if args['date']:
        o.date = args['date']
    if args['user_id']:
        o.user_id = args['user_id']

    return o