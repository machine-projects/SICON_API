from flask_restful import fields


PAGINATE = dict(
   
        page = fields.Integer,
        pages = fields.Integer,
        per_page = fields.Integer,
        prev_num = fields.Integer,
        total = fields.Integer
)