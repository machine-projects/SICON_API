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
from src.infra.handler.pagination import Paginate

class AddressHandler:

    def __init__(self):
        pass

    def get_all_address(self):
        repository = AddressRepository()
        paginate = Paginate().url_intercept_args(request)
        address = repository.get_all_address(paginate)
        status_result = ValidationsAndSetStatusResultInfraHandler()
        return status_result.default(address)

    def get_by_id(self, playload):
        _id = playload.get('id')
        if _id: playload['id'] = int(_id)
        contract = GetByIdAddressContract()
        if not(contract.validate(playload)):
            return ResultModel('Problema nos parametros enviados.', False, contract.errors).to_dict(), 406
        repository = AddressRepository()
        person = repository.get_by_id(playload)
        status_result = ValidationsAndSetStatusResultInfraHandler()
        return status_result.default(person)
    
    def get_by_person_id(self, playload):
        contract = GetByIdAddressContract()
        _id = playload.get('id')
        if _id: playload['id'] = int(_id)
        if not(contract.validate(playload)):
            return ResultModel('Problema nos parametros enviados.', False, contract.errors).to_dict(), 406
        repository = AddressRepository()
        address = repository.get_by_person_id(playload)
        
        status_result = ValidationsAndSetStatusResultInfraHandler()
        return status_result.default(address)

    def update_address(self):
        contract = UpdateAdressContract()
        playload = request.json
        if not(contract.validate(playload)):
            return ResultModel('Problema nos parametros enviados.', False, contract.errors).to_dict(), 406
        repository = AddressRepository()
        address = repository.update_address(playload)
        
        status_result = ValidationsAndSetStatusResultInfraHandler()
        return status_result.default(address)

    def create_address(self):
        contract = CreateAdressContract()
        playload = request.json
        if not(contract.validate(playload)):
            return ResultModel('Problema nos parametros enviados.', False, contract.errors).to_dict(), 406
        repository = AddressRepository()
        address = repository.create_address(playload)
        
        status_result = ValidationsAndSetStatusResultInfraHandler()
        return status_result.default(address)
    
    def delete_address(self):
        contract = DeleteAddressContract()
        playload = request.json
        if not(contract.validate(playload)):
            return ResultModel('Problema nos parametros enviados.', False, contract.errors).to_dict(), 406
        repository = AddressRepository()

        address = repository.delete_address(playload)
        status_result = ValidationsAndSetStatusResultInfraHandler()
        return status_result.default(address)
