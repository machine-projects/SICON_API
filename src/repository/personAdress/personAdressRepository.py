from src import db
from src.model.personAddress import PersonAddress
from src.model.schemas.personAddressSchemas import person_address_fields
from flask_restful import marshal
from src.infra.model.resultModel import ResultModel
import datetime


class PersonAddressRepository:
    
    def __init__(self):
        pass

    @staticmethod
    def get_all_persons_address():
        try:
            persons = PersonAddress.query.all()
            data = marshal(persons, person_address_fields)
            return ResultModel('Pesquisa realizada com sucesso.', data, False).to_dict()
        except Exception as e:
            return ResultModel('Não foi possivel realizar a pesquisa.', False, True, str(e)).to_dict()

    def get_by_person_id_address_id(self, person_address_dict):
        try:
            person_id = person_address_dict.get('person_id')
            address_id = person_address_dict.get('address_id')

            person_address = PersonAddress.query.filter_by(person_id=person_id, address_id=address_id).first()
            if not person_address: return ResultModel('Não encontrado.', False, True).to_dict()

            person_address_fields = person_address_fields
            data = marshal(person_address, person_address_fields)
            return ResultModel('Pesquisa realizada com sucesso.', data, False).to_dict()
        except Exception as e:
            return ResultModel('Não foi possivel realizar a pesquisa.', False, True, str(e)).to_dict()
    
    def get_by_person_id(self, person_address_dict):
        try:
            person_id = person_address_dict.get('person_id')

            person_address = PersonAddress.query.filter_by(person_id=person_id).all()
            if not person_address: return ResultModel('Não encontrado.', False, True).to_dict()

            person_address_fields = person_address_fields
            data = marshal(person_address, person_address_fields)
            return ResultModel('Pesquisa realizada com sucesso.', data, False).to_dict()
        except Exception as e:
            return ResultModel('Não foi possivel realizar a pesquisa.', False, True, str(e)).to_dict()
    
    @staticmethod
    def create_person_address(person_address_dict):
        try:
            person_id = person_address_dict.get('person_id')
            address_id = person_address_dict.get('address_id')

            person_address = PersonAddress(address_id, person_id)
            db.session.add(person_address)
            db.session.commit()
            person_address_result = marshal(person_address, person_address_fields)
            return ResultModel('Pessoa Endereço criado com sucesso.', person_address_result, False).to_dict()
        except Exception as e:
            return ResultModel('Não foi possivel criar pessoa endereço.', False, True, str(e)).to_dict()

    @staticmethod
    def update_person_address(person_address_dict):
        try:
            _id = person_address_dict.get('id')
            person_id = person_address_dict.get('person_id')
            address_id = person_address_dict.get('address_id')

            person_address = PersonAddress.query.get(_id)
            if person_address:
                person_address.person_id = person_id
                person_address.address_id = address_id
                person_address.modification_date = datetime.datetime.utcnow()
                db.session.add(person_address)
                db.session.commit()
            data = marshal(person_address, person_address_fields)
            return ResultModel('Pessoa Endereço alterado com sucesso.', data, False).to_dict()
        except Exception as e:
            return ResultModel('Não foi possivel alterar a pessoa endereço.', False, True, str(e)).to_dict()
    
    @staticmethod
    def delete_person_address(person_address_dict):
        try:
            _id = person_address_dict.get('id')
            persons_addresses = PersonAddress.query.get(_id)
            if persons_addresses:
                db.session.delete(persons_addresses)
                db.session.commit()

            data = marshal(persons_addresses, person_address_fields)
            return ResultModel('Pessoa Endereço deletado com sucesso.', data, False).to_dict()
        except Exception as e:
            return ResultModel('Não foi possivel deletar a pessoa endereço.', False, True, str(e)).to_dict()
    
    