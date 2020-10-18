from flask_restful import Resource, reqparse, request
from flask_restful import fields, marshal_with, marshal
from sqlalchemy.exc import IntegrityError
from sqlalchemy import or_, and_, text
from flask_jwt_extended import jwt_required
from models.log import Log
from app import db
from utils.util import max_res


from helpers.logs_resource_helper import *  

class LogsResource(Resource):

    @jwt_required
    def get(self, log_id=None):
        if log_id:
            log = Log.find_by_id(log_id)
            return max_res(marshal(log, log_fields))
        else:
            conditions = []

            args = log_query_parser.parse_args()
            page = args['page']
            per_page = args['pagesize']

            if args['orderby'] not in sortable_fields:
                return max_res('', code=500, errmsg='排序非法字段')
            sort = args['orderby']
            if args['desc']>0:
                sort = args['orderby'] + ' desc'

            conditions = make_conditions(conditions,args)
            # 在这里添加更多的 条件查询 例如 
            # if args['name'] is not None:
            #       conditions.append(Log.name.like('%'+args['name']+'%'))
       
            if conditions is []:
                pagination = Log.query.order_by(text(sort)).paginate(page, per_page, error_out=False)
            else:
                pagination = Log.query.filter(*conditions).order_by(text(sort)).paginate(page, per_page, error_out=False)
            paginate = {
                'total':pagination.total,
                'pageSize': pagination.per_page,
                'current': pagination.page
            }
            print(pagination.items)


            return max_res(marshal({
                'pagination': paginate,
                'list': [marshal(u, log_fields) for u in pagination.items]
            }, log_list_fields))


    @jwt_required
    def post(self):
        args = log_post_parser.parse_args()

        log = Log(**args)
        try:
            log.add()
        except IntegrityError:
            return max_res('', code=401, errmsg='名称重复')

        return max_res(marshal(log, log_fields))


   
    def put(self, log_id=None):
        log = Log.find_by_id(log_id)

        args = log_update_parser.parse_args()

        log = update_all_fields(args, log)
        #可以在这里继续添加 需要更新的字段 如
        #    if args['name']:
        #       o.name = args['name']
        #
        
        db.session.commit()
        try:
            log.update()
        except Exception as e:
            return max_res('',500, 'Failed to modify.')

        return max_res(marshal(log, log_fields))

   
    def delete(self, log_id=None):
        log = Log.find_by_id(log_id)

        try:
            log.delete()
        except Exception as e:
            return max_res('',500, 'The record has already deleted.')

        return max_res('The record has been deleted.')