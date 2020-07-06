from flask_restful import Resource, marshal
from src.repository.address.addressRepository import AddressRepository
from src import db, request
from src.contract.address.getByIdAddressContract import GetByIdAddressContract
from src.contract.address.getByPersonIdAddressContract import GetByPersonIdAddressContract
from src.contract.address.updateAddressContract import UpdateAdressContract
from src.contract.address.createAddressContract import CreateAdressContract
from src.contract.address.deleteAddressContract import DeleteAddressContract
from src.infra.model.resultModel import ResultModel
from src.infra.handler.validationsAndSetStatusResultInfraHandler import ValidationsAndSetStatusResultInfraHandler
from src.helper.personHelper import PersonHelper

class PersonHandler:

    def __init__(self):
        pass

    def get_all_address(self):
        repository = AddressRepository()
        persons = repository.get_all_address()
        valid_result = ValidationsAndSetStatusResultInfraHandler()
        return valid_result.default_result(persons)

    def get_by_id(self):
        contract = GetByIdAddressContract()
        playload = request.json
        if not(contract.validate(playload)):
            return ResultModel('Problema nos parametros enviados.', False, contract.errors).to_dict(), 406
        repository = AddressRepository()
        person = repository.get_by_id(playload)
        valid_result = ValidationsAndSetStatusResultInfraHandler()
        return valid_result.default_result(person)
    
    def get_by_person_id(self, cnpj):
        contract = GetByPersonIdAddressContract()
        if not(contract.validate(cnpj)):
            return ResultModel('Parametro incorreto.', False, contract.errors).to_dict(), 406
        repository = AddressRepository()
        person = repository.get_by_cnpj_or_cnpj('Pessoa Juridica', cnpj)
        valid_result = ValidationsAndSetStatusResultInfraHandler()
        return valid_result.default_result(person)

    def update_person(self):
        contract = UpdateAdressContract()
        playload = request.json
        if not(contract.validate(playload)):
            return ResultModel('Problema nos parametros enviados.', False, contract.errors).to_dict(), 406
        repository = AddressRepository()
        person = repository.update_address(playload)
        valid_result = ValidationsAndSetStatusResultInfraHandler()
        return valid_result.default_result(person)

    def create_person(self):
        contract = CreateAdressContract()
        playload = request.json
        if not(contract.validate(playload)):
            return ResultModel('Problema nos parametros enviados.', False, contract.errors).to_dict(), 406
        repository = AddressRepository()
        person = repository.create_person(playload)
        valid_result = ValidationsAndSetStatusResultInfraHandler()
        return valid_result.default_result(person)
    
    def delete_person(self):
        contract = DeleteAddressContract()
        playload = request.json
        if not(contract.validate(playload)):
            return ResultModel('Problema nos parametros enviados.', False, contract.errors).to_dict(), 406
        repository = AddressRepository()

        person = repository.delete_address(playload)
        valid_result = ValidationsAndSetStatusResultInfraHandler()
        return valid_result.default_result(person)
