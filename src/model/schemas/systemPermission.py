from flask_restful import fields

system_permission_fields = {
    'id': fields.Integer,
    'system_id': fields.Integer,
    'name': fields.String,
    'description': fields.String,
}

