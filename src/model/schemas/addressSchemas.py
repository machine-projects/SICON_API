from flask_restful import fields



__id = 'id'
__person_id = 'person_id'
__neighborhood = 'neighborhood'
__street = 'street'
__number = 'number'
__complement = 'complement'
__city = 'city'


address_fields = {
        __id: fields.Integer,
        __person_id: fields.Integer,
        __neighborhood: fields.String,
        __street: fields.String,
        __number: fields.String,
        __complement: fields.String,
        __city: fields.String
    }


