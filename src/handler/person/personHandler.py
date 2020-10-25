from flask_restful import Resource, marshal
from src.repository.person.personRepository import PersonRepository
from src import db, request
from src.infra.model.resultModel import ResultModel
from src.infra.handler.pagination import Paginate
from src.contract.peson.getByCpfPersonContract import GetByCpfPersonContract
from src.contract.peson.getByCnpjPersonContract import GetByCnpjPersonContract
from src.contract.peson.createPersonContract import CreatePersonContract
from src.contract.peson.updatePersonContract import UpdatePersonContract
from src.contract.peson.deletePersonContract import DeletePersonContract
from src.helper.personHelper import PersonHelper
from src.helper.genericHelper import GenericHelper
from src.infra.handler.setStatusResponseHandler import SetStatusResponseHandler
from src.contract.peson.getByParamsPersonContract import GetByParamsPersonContract


class PersonHandler:

    def __init__(self):
        pass

    def get_all_persons(self):
        repository = PersonRepository()
        playload = Paginate().include_paginate_args_playload(request)
        persons = repository.get_all_persons(playload)
        
        status_result = SetStatusResponseHandler()
        return status_result.default(persons)

    def get_by_params(self):
        contract = GetByParamsPersonContract()
        playload = request.args
        if not(contract.validate(playload)):
            return ResultModel('Parametro incorreto.', False, contract.errors).to_dict(), 406
        generic_helper = GenericHelper()
        params_filter = {}
        _id = playload.get('id')
        cnpj = playload.get('cnpj')
        cpf = playload.get('cpf')
        birth_date = playload.get('birth_date')
        gender = playload.get('gender')
        name = playload.get('name')
        _type = playload.get('type')

        if _id:
            params_filter['id'] = int(_id)
        if cnpj:
            params_filter['cnpj'] = cnpj
        if cpf:
            params_filter['cpf'] = cpf
        if birth_date:
            params_filter['birth_date'] = generic_helper.str_date_to_datetime(birth_date)
        if gender:
            params_filter['gender'] = gender
        if name:
            params_filter['name'] = name
        if _type:
            params_filter['type'] = _type
        params_filter= Paginate().include_paginate_args_playload(request, params_filter)
        repository = PersonRepository()
        systems = repository.get_search_by_params(params_filter)
        status_result = SetStatusResponseHandler()
        return status_result.default(systems)

    def update_person(self):
        contract = UpdatePersonContract()
        playload = request.json
        if not(contract.validate(playload)):
            return ResultModel('Problema nos parametros enviados.', False, contract.errors).to_dict(), 406
        playload = GenericHelper().captalize_full_dict(playload)
        repository = PersonRepository()

        person = repository.update_person(playload)
        
        status_result = SetStatusResponseHandler()
        return status_result.default(person)

    def create_person(self):
        contract = CreatePersonContract()
        playload = request.json
        if not(contract.validate(playload)):
            return ResultModel('Problema nos parametros enviados.', False, contract.errors).to_dict(), 406
        playload = GenericHelper().captalize_full_dict(playload)
        repository = PersonRepository()
        cpf = playload.get('cpf')
        cnpj = playload.get('cnpj')
        helper = PersonHelper()
        if cpf:
            playload['cpf'] = helper.remove_characters(cpf)
        if cnpj:
            playload['cnpj'] =  helper.remove_characters(cnpj)
        
        person = repository.create_person(playload)
        
        status_result = SetStatusResponseHandler()
        return status_result.default(person)
        
    
    def delete_person(self):
        contract = DeletePersonContract()
        playload = request.json
        if not(contract.validate(playload)):
            return ResultModel('Problema nos parametros enviados.', False, contract.errors).to_dict(), 406
        repository = PersonRepository()

        person = repository.delete_person(playload.get('id'))
        
        status_result = SetStatusResponseHandler()
        return status_result.default(person)
