from src import db
from src.model.address import Address
from src.model.personAddress import PersonAddress
from src.model.address import Address
from src.model.schemas.addressSchemas import address_fields
from flask_restful import marshal
from src.infra.model.resultModel import ResultModel
import datetime


class AddressRepository:
    
    def __init__(self):
        pass

    @staticmethod
    def get_all_address():
        try:
            address = Address.query.all()
            data = marshal(address, address_fields)
            return ResultModel('Pesquisa realizada com sucesso.', data, False).to_dict()
        except Exception as e:
            return ResultModel('Não foi possivel realizar a pesquisa.', False, True, str(e)).to_dict()

    def get_by_person_id(self, playload):
        try:
            person_id = playload.get('id')
            schema_address = address_fields

            person = Address.query.filter_by(person_id=person_id).all()
            data = marshal(person, schema_address)
            return ResultModel('Pesquisa realizada com sucesso.', data, False).to_dict()
        except Exception as e:
            return ResultModel('Não foi possivel realizar a pesquisa.', False, True, str(e)).to_dict()
    
    def get_by_id(self, data_dict):
        try:
            _id = data_dict.get('id')
            schema_address = address_fields
            address = Address.query.get(_id)
            if not address:
                return ResultModel('Endereço não encontrado.', False, True).to_dict()
            data = marshal(address, schema_address)
            return ResultModel('Pesquisa realizada com sucesso.', data, False).to_dict()
        except Exception as e:
            return ResultModel('Não foi possivel realizar a pesquisa.', False, True, str(e)).to_dict()
    
    @staticmethod
    def create_address(data_address):
        try:
            address = Address(data_address)
            db.session.add(address)
            db.session.commit()
            address_result = marshal(address, address_fields)
            return ResultModel('Endereço criado com sucesso.', address_result, False).to_dict()
        except Exception as e:
            return ResultModel('Não foi possivel criar endereço.', False, True, str(e)).to_dict()

    @staticmethod
    def update_address(address_dict):
        try:
            _id = address_dict.get('id')
            person_id = address_dict.get('person_id')
            neighborhood = address_dict.get('neighborhood')
            street = address_dict.get('street')
            number = address_dict.get('number')
            complement = address_dict.get('complement')
            city = address_dict.get('city')

            address = Address.query.get(_id)
            if  not address:
                return ResultModel('Não foi possivel alterar o endereço.', False, True).to_dict()
            
            address.id = _id
            address.person_id = person_id
            address.neighborhood = neighborhood
            address.street = street
            address.number = number
            address.complement = complement
            address.city = city
            address.modification_date = datetime.datetime.utcnow()
            db.session.add(address)
            db.session.commit()
            data = marshal(address, address_fields)
            return ResultModel('Endereço alterada com sucesso.', data, False).to_dict()
        except Exception as e:
            return ResultModel('Não foi possivel alterar o endereço.', False, True, str(e)).to_dict()
    
    @staticmethod
    def delete_address(address_dict):
        try:
            address_id = address_dict.get('id')
            person_address = PersonAddress.query.filter_by(address_id=address_id).first()
            if person_address:
                db.session.delete(person_address)
                db.session.commit()

            address = Address.query.get(address_id)
            if not address:
                return ResultModel('Endereço não encontrado.', False, True).to_dict()
            
            db.session.delete(address)
            db.session.commit()
            data = marshal(address, address_fields)
            return ResultModel('Endereço deletado com sucesso.', data, False).to_dict()
        except Exception as e:
            return ResultModel('Não foi possivel deletar o endereço.', False, True, str(e)).to_dict()
    
    