from flask_restful import fields

system_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'description': fields.String,
    'url': fields.String,
}

system_fields_with_dates = {
    'id': fields.Integer,
    'name': fields.String,
    'description': fields.String,
    'url': fields.String,
    'modification_date': fields.String,
    'creation_date': fields.String,
}

