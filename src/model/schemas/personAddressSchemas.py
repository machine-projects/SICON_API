from flask_restful import fields

__person_id = 'person_id'
__address_id = 'type'
__id = 'id'



person_address_fields = {
        __id: fields.Integer,
        __person_id: fields.Integer,
        __address_id: fields.Integer,
    }
