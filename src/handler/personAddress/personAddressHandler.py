from flask_restful import Resource, marshal
from src.repository.personAdress.personAdressRepository import PersonAddressRepository
from src import db, request
from src.contract.personAddress.getAllPersonAddressContract import GetAllPersonAddressContract
from src.contract.personAddress.getByPersonIdAddressIdContract import GetByPersonIdAddressIdContract
from src.contract.personAddress.getByPersonId import GetByPersonIdContract
from src.contract.personAddress.createPersonAddressContract import CreatePersonAddressContract
from src.contract.personAddress.updatePersonAddressContract import UpdatePersonAddressContract
from src.contract.personAddress.deletePersonAddressContract import DeletePersonAddressContract
from src.infra.model.resultModel import ResultModel
from src.infra.handler.validationsAndSetStatusResultInfraHandler import ValidationsAndSetStatusResultInfraHandler
from src.helper.personHelper import PersonHelper

class PersonAddressHandler:

    def __init__(self):
        pass

    @staticmethod
    def get_all_persons_address():
        contract = GetAllPersonAddressContract()
        playload = request.json
        if not(contract.validate(playload)):
            return ResultModel('Parametro incorreto.', False, contract.errors).to_dict(), 406
        repository = PersonAddressRepository()
        person_address = repository.get_all_persons_address()
        valid_result = ValidationsAndSetStatusResultInfraHandler() 
        return valid_result.default(person_address)

    @staticmethod
    def get_by_person_id_address_id():
        contract = GetAllPersonAddressContract()
        playload = request.json
        if not(contract.validate(playload)):
            return ResultModel('Parametro incorreto.', False, contract.errors).to_dict(), 406
        repository = PersonAddressRepository()
        person_address = repository.get_by_person_id_address_id(playload)
        valid_result = ValidationsAndSetStatusResultInfraHandler() 
        return valid_result.default(person_address)
    
    @staticmethod
    def get_by_person_id():
        contract = GetByPersonIdContract()
        playload = request.json
        if not(contract.validate(playload)):
            return ResultModel('Parametro incorreto.', False, contract.errors).to_dict(), 406
        repository = PersonAddressRepository()
        person_address = repository.get_by_person_id(playload)
        valid_result = ValidationsAndSetStatusResultInfraHandler() 
        return valid_result.default(person_address)

    @staticmethod
    def create_person_address():
        contract = CreatePersonAddressContract()
        playload = request.json
        if not(contract.validate(playload)):
            return ResultModel('Problema nos parametros enviados.', False, contract.errors).to_dict(), 406
        repository = PersonAddressRepository()
        person_address = repository.update_person(playload)
        valid_result = ValidationsAndSetStatusResultInfraHandler() 
        return valid_result.default(person_address)

    @staticmethod
    def update_person_address():
        contract = UpdatePersonAddressContract()
        playload = request.json
        if not(contract.validate(playload)):
            return ResultModel('Problema nos parametros enviados.', False, contract.errors).to_dict(), 406
        repository = PersonAddressRepository()
        person_address = repository.create_person(playload)
        valid_result = ValidationsAndSetStatusResultInfraHandler() 
        return valid_result.default(person_address)
    
    @staticmethod
    def delete_person_address():
        contract = DeletePersonAddressContract()
        playload = request.json
        if not(contract.validate(playload)):
            return ResultModel('Problema nos parametros enviados.', False, contract.errors).to_dict(), 406
        repository = PersonAddressRepository()
        person_address = repository.delete_person_address(playload)
        valid_result = ValidationsAndSetStatusResultInfraHandler() 
        return valid_result.default(person_address)