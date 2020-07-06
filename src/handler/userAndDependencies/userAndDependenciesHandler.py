from flask_restful import Resource, marshal
from src.model.users import User
from src import db, request
from src.model.schemas.users import users_fields
from flask_bcrypt import Bcrypt
from flask import current_app
from src.repository.user.userRepository import UserRepository
from src.repository.person.personRepository import PersonRepository
from src.repository.address.addressRepository import AddressRepository
from src.repository.personAdress.personAdressRepository import PersonAddressRepository
from src.infra.model.resultModel import ResultModel
from src.contract.userAndDependencies.createUserAndpersonAndAddressContract import CreateUserAndpersonAndAddressContract



class UserAndDependenciesHandler:
 
    def create_user_person_address(self):
        contract = CreateUserAndpersonAndAddressContract()
        playload = request.json
        if not(contract.validate(playload)):
            return ResultModel('Envie todos parametros obrigatorios.', False, contract.errors).to_dict(), 406
        user_dto = playload.get('user')
        person_dto = playload.get('person')
        address_dto = playload.get('address')
        
        user_repository = UserRepository()
        person_repository = PersonRepository()
        address_repository = AddressRepository()
        person_address_repository = PersonAddressRepository()

        user_exist = user_repository.get_by_username(user_dto.get('username'))
        if user_exist['message'] != 'Nome de usuario não encontrado.':
            if user_exist.get('exeption'):
                return user_exist, 500
            elif user_exist['message'] == 'Pesquisa realizada com sucesso.':
                username = user_dto.get('username')
                return ResultModel(f'Usuario "{username}" já existe.', False, True).to_dict(), 406
            return user_exist, 406

        person = person_repository.create_person(person_dto)
        if not person['data']:
            return person, 500
        person = person['data']
        address_dto['person_id'] = person.get('id')
        address = address_repository.create_address(address_dto)
        if not address['data']:
            return address, 500
        address = address['data']
        person_address_dto = dict(
            person_id=person['id'],
            address_id=address['id']
        )
        person_address = person_address_repository.create_person_address(person_address_dto)
        if not person_address['data']:
            return person_address, 500
        person_address = person_address['data']
        
        user_repository.create(user_dto)
        user_dto['person_id'] = person['id']
        user = user_repository.create(user_dto)
        if user['error']:
            if user['exeption']:
                return user, 500
            return user, 406
        user = user['data']

        result = dict(
        user=user,
        person=person,
        address=address,
        person_address=person_address
        )   
        return result, 200
