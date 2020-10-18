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
from src.helper.genericHelper import GenericHelper as Helper
from src.infra.handler.setStatusResponseHandler import SetStatusResponseHandler


class PersonHandler:

    def __init__(self):
        pass

    def get_all_persons(self):
        repository = PersonRepository()
        playload = Paginate().include_paginate_args_playload(request)
        persons = repository.get_all_persons(playload)
        
        status_result = SetStatusResponseHandler()
        return status_result.default(persons)

    def get_by_cpf(self, cpf):
        contract = GetByCpfPersonContract()
        if not(contract.validate(cpf)):
            return ResultModel('Parametro incorreto.', False, contract.errors).to_dict(), 406
        repository = PersonRepository()
        person = repository.get_by_cpf_or_cnpj('Pessoa Fisica', cpf)
        
        status_result = SetStatusResponseHandler()
        return status_result.default(person)
    
    def get_by_cnpj(self, cnpj):
        contract = GetByCnpjPersonContract()
        if not(contract.validate(cnpj)):
            return ResultModel('Parametro incorreto.', False, contract.errors).to_dict(), 406
        repository = PersonRepository()
        person = repository.get_by_cnpj_or_cnpj('Pessoa Juridica', cnpj)
        
        status_result = SetStatusResponseHandler()
        return status_result.default(person)

    def update_person(self):
        contract = UpdatePersonContract()
        playload = request.json
        if not(contract.validate(playload)):
            return ResultModel('Problema nos parametros enviados.', False, contract.errors).to_dict(), 406
        playload = Helper().captalize_full_dict(playload)
        repository = PersonRepository()

        person = repository.update_person(playload)
        
        status_result = SetStatusResponseHandler()
        return status_result.default(person)

    def create_person(self):
        contract = CreatePersonContract()
        playload = request.json
        if not(contract.validate(playload)):
            return ResultModel('Problema nos parametros enviados.', False, contract.errors).to_dict(), 406
        playload = Helper().captalize_full_dict(playload)
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
