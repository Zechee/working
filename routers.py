from app import api

from resourses.users_resource import UsersResource
api.add_resource(UsersResource, '/users', '/uers/<int:user_id>')

from resourses.logs_resource import LogsResource
api.add_resource(LogsResource, '/logs', '/logs/<int:workinglog_id>')

from resourses.Logitems_resource import LogitemsResource
api.add_resource(LogitemsResource, '/logitems', '/logitems/<int:logitem_id>')