from flask_restful import fields




profile_system_fields = {
        'id': fields.Integer,
        'system_id': fields.Integer,
        'name': fields.String,
        'description': fields.String,
    }
