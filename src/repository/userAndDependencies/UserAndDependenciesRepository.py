from src import db
from src.model.users import User
from src.model.address import Address
from src.model.person import Person
from src.model.users import User
from src.model.schemas.users import users_fields, users_fields_with_pass
from src.model.schemas.personSchemas import person_fields
from src.model.schemas.addressSchemas import address_fields
from flask_restful import marshal
from src.infra.model.resultModel import ResultModel


class UserAndDependenciesRepository:

    def __init__(self):
        pass

    def get(self, playload):
        user_id = playload.get('user_id')
        person_id = playload.get('person_id')
        address_id = playload.get('address_id')
        try:
            if user_id:
                user_id = int(user_id)
                user_result, person_result = db.session.query(User, Person).filter(Person.id == User.person_id).filter(User.id == user_id).first()
                
                if not user_result:
                    return  ResultModel('Sem resultados na pesquisa.', False, True).to_dict()
                user_data = marshal(user_result, users_fields)
                person_data = marshal(person_result, person_fields)

                query_address = Address.query.filter_by(person_id=person_data['id']).all()
                address_data = marshal(query_address, address_fields)
                return self.__formart_result(user_data, person_data, address_data)

            elif person_id:
                person_id = int(person_id)
                person_result, user_result = db.session.query(Person, User).filter(User.person_id == Person.id).filter(Person.id == person_id).first()
                if not person_result:
                    return  ResultModel('Pessoa não encontrada.', False, True).to_dict()
                

                person_data = marshal(person_result, person_fields)
                user_data = marshal(user_result, users_fields)

                address_result = Address.query.filter_by(person_id=person_data.get('id')).all()
                address_data = marshal(address_result, address_fields)
                return self.__formart_result(user_data, person_data, address_data)

            elif address_id:
                address_id_result = db.session.query(Address).filter(Address.id == address_id).first()
                if not address_id_result: 
                    return  ResultModel('Endereço não encontrado.', False, True).to_dict()
                person_id = address_id_result.person_id
                person_result, user_result = db.session.query(Person, User).filter(User.person_id == Person.id).filter(Person.id == person_id).first()
                if not person_result:
                    return  ResultModel('Pessoa não encontrada.', False, True).to_dict()
                
                person_data = marshal(person_result, person_fields)
                user_data = marshal(user_result, users_fields)
                address_result = Address.query.filter_by(person_id=person_data.get('id')).all()
                address_data = marshal(address_result, address_fields)
                return self.__formart_result(user_data, person_data, address_data)
        except Exception as e:
            return ResultModel('Ouve algum problema ao tentar acessar o banco de dados.', False, True, str(e)).to_dict()



        
   
    def __formart_result(self, user_data, person_data, address_data):
        data = dict(
            user=user_data,
            person=person_data,
            address=address_data
        )
        return ResultModel('Pesquisa realizada com sucesso.', data, False).to_dict()