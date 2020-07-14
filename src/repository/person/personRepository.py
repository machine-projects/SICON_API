from src import db
from src.model.person import Person
from src.model.address import Address
from src.model.schemas.personSchemas import person_fields
from flask_restful import marshal
from src.infra.model.resultModel import ResultModel
import datetime
from src.helper.genericHelper import GenericHelper

class PersonRepository:
    
    def __init__(self):
        pass

    @staticmethod
    def get_all_persons():
        try:
            persons = Person.query.all()
            data = marshal(persons, person_fields)
            return ResultModel('Pesquisa realizada com sucesso.', data, False).to_dict()
        except Exception as e:
            return ResultModel('Não foi possivel realizar a pesquisa.', False, True, str(e)).to_dict()

    def get_by_cpf_or_cnpj(self, _type, cpf_or_cnpj):
        try:
            schema_person = person_fields
            if _type == 'Pessoa Fisica':
                person = Person.query.filter_by(cpf=cpf_or_cnpj).first()
            elif _type == 'Pessoa Juridica':
                person = Person.query.filter_by(cnpj=cpf_or_cnpj).first()
                
            else: return ResultModel('Tipo de pessoa incorreto.', False, True).to_dict()
            data = marshal(person, schema_person)
            return ResultModel('Pesquisa realizada com sucesso.', data, False).to_dict()
        except Exception as e:
            return ResultModel('Não foi possivel realizar a pesquisa.', False, True, str(e)).to_dict()
    
    @staticmethod
    def create_person(data_person):
        try:
            helper = GenericHelper()
            birth_date = data_person.get('birth_date')
            cpf = data_person.get('cpf')
            cnpj = data_person.get('cnpj')
            if birth_date:
                data_person['birth_date'] = helper.str_date_to_datetime(birth_date)
            if cpf:
                find_cpf = Person.query.filter_by(cpf=cpf).first()
               
                if find_cpf: 
                    return ResultModel(
                    'Não foi possivel criar pessoa.',
                     False, [dict(name='cpf', error='O CPF já foi cadastrado.')]).to_dict()
            elif cnpj:
                find_cnpj = Person.query.filter_by(cnpj=cnpj).first()
                if find_cnpj: return ResultModel(
                    'Não foi possivel criar pessoa.',
                     False, [dict(name='cnpj', error='O CNPJ já foi cadastrado.')]).to_dict()

            person = Person(data_person)
            db.session.add(person)
            db.session.commit()
            person_result = marshal(person, person_fields)
            return ResultModel('Pessoa criada com sucesso.', person_result, False).to_dict()
        except Exception as e:
            return ResultModel('Não foi possivel criar pessoa.', False, True, str(e)).to_dict()

    @staticmethod
    def update_person(person_dict):
        try:
            helper = GenericHelper()
            
            birth_date = person_dict.get('birth_date')
            if birth_date:
                birth_date = helper.str_date_to_datetime(birth_date)
            _id = person_dict.get('id')
            _type = person_dict.get('type')
            name = person_dict.get('name')
            surname = person_dict.get('surname')
            gender = person_dict.get('gender')
            cpf = person_dict.get('cpf')
            company_name = person_dict.get('company_name')
            cnpj = person_dict.get('cnpj')

            person = Person.query.get(_id)
            if person:
                person.type = _type
                person.birth_date = birth_date
                person.name = name
                person.surname = surname
                person.gender = gender
                person.cpf = cpf
                person.company_name = company_name
                person.cnpj = cnpj
                person.modification_date = datetime.datetime.utcnow()
                db.session.add(person)
                db.session.commit()
            data = marshal(person, person_fields)
            return ResultModel('Pessoa alterada com sucesso.', data, False).to_dict()
        except Exception as e:
            return ResultModel('Não foi possivel alterar a pessoa.', False, True, str(e)).to_dict()
    
    @staticmethod
    def delete_person(person_id):
        try:
            person = Person.query.get(person_id)
            if person:
                db.session.delete(person)
                db.session.commit()
            data = marshal(person, person_fields)
            return ResultModel('Pessoa deletada com sucesso.', data, False).to_dict()
        except Exception as e:
            return ResultModel('Não foi possivel deletar a pessoa.', False, True, str(e)).to_dict()
    
    