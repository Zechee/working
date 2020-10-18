from app import api

from resourses.logs_resource import LogsResource
api.add_resource(LogsResource, '/logs', '/logs/<int:log_id>')

from resourses.logitems_resource import LogitemsResource
api.add_resource(LogitemsResource, '/logitems', '/logitems/<int:logitem_id>')