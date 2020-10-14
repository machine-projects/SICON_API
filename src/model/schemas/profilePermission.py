from flask_restful import fields


profile_permission_fields = {
        'id': fields.Integer,
        'profile_system_id': fields.Integer,
        'system_permission_id': fields.Integer,
    }
