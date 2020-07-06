from flask_restful import fields

__id = 'id'
__type = 'type'
__birth_date = 'birth_date'
__name = 'name'
__surname = 'surname'
__gender = 'gender'
__cpf = 'cpf'
__company_name = 'company_name'
__cnpj = 'cnpj'


person_fields = {
        __id: fields.Integer,
        __type: fields.String,
        __birth_date: fields.String,
        __name: fields.String,
        __surname: fields.String,
        __gender: fields.String,
        __cpf: fields.String,
        __company_name: fields.String,
        __cnpj: fields.String,
    }
