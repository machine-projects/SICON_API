from src import db, request
from src.model.users import User
from src.model.schemas.users import users_fields
from src.repository.user.userRepository import UserRepository
from src.repository.person.personRepository import PersonRepository
from src.repository.address.addressRepository import AddressRepository
from src.repository.userAndDependencies.UserAndDependenciesRepository import UserAndDependenciesRepository
from src.infra.model.resultModel import ResultModel
from src.helper.personHelper import PersonHelper
from src.infra.handler.setStatusResponseHandler import SetStatusResponseHandler
from src.contract.userAndDependencies.createUserAndpersonAndAddressContract import CreateUserAndpersonAndAddressContract
from src.contract.userAndDependencies.getUserAndpersonAndAddressContract import GetUserAndpersonAndAddressContract
from flask_restful import Resource, marshal
from flask_bcrypt import Bcrypt
from flask import current_app



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
        status_result = SetStatusResponseHandler()
        user_exist = user_repository.get_by_username(user_dto.get('username'))
        if user_exist['message'] != 'Nome de usuario não encontrado.':
            if user_exist.get('exeption'):
                return user_exist, 500
            elif user_exist['message'] == 'Pesquisa realizada com sucesso.':
                username = user_dto.get('username')
                return ResultModel(f'Usuario "{username}" já existe.', False, True).to_dict(), 406
            return user_exist, 406
        cpf = person_dto.get('cpf')
        cnpj = person_dto.get('cnpj')
        person_helper = PersonHelper()
        if cpf:
            person_dto['cpf'] = person_helper.remove_characters(cpf)
        elif cnpj:
            person_dto['cnpj'] = person_helper.remove_characters(cnpj)
        person = person_repository.create_person(person_dto)
        if not person['data']['result']:
            return status_result.default(person)
        person = person['data']['result']
        address_dto['person_id'] = person.get('id')
        address = address_repository.create_address(address_dto)
        if not address['data']['result']:
            return status_result.default(address)
            
        address = address['data']['result']
        user_repository.create(user_dto)
        user_dto['person_id'] = person['id']
        user = user_repository.create(user_dto)
        if user['error']:
            return status_result.default(user)
        user = user['data']['result']

        result = dict(
        user=user,
        person=person,
        address=address,
        )   
        return result, 200

    def get_user_person_address(self):
        contract = GetUserAndpersonAndAddressContract()
        playload = request.args
        if not(contract.validate(playload)):
            return ResultModel('Envie ao menos um parametro.', False, contract.errors).to_dict(), 406
        repository = UserAndDependenciesRepository()
        return repository.get(playload)
        

