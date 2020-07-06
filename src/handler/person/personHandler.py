from flask_restful import Resource, marshal
from src.repository.person.personRepository import PersonRepository
from src import db, request
from src.infra.model.resultModel import ResultModel
from src.contract.peson.getByCpfPersonContract import GetByCpfPersonContract
from src.contract.peson.getByCnpjPersonContract import GetByCnpjPersonContract
from src.contract.peson.createPersonContract import CreatePersonContract
from src.contract.peson.updatePersonContract import UpdatePersonContract
from src.contract.peson.deletePersonContract import DeletePersonContract
from src.helper.personHelper import PersonHelper

class PersonHandler:

    def __init__(self):
        pass

    def get_all_persons(self):
        repository = PersonRepository()
        persons = repository.get_all_persons()
        if persons['error']:
            return persons, 500
        return persons, 200

    def get_by_cpf(self, cpf):
        contract = GetByCpfPersonContract()
        if not(contract.validate(cpf)):
            return ResultModel('Parametro incorreto.', False, contract.errors).to_dict(), 406
        repository = PersonRepository()
        persons = repository.get_by_cpf_or_cnpj('Pessoa Fisica', cpf)
        if persons['error']:
            return persons, 500
        return persons, 200
    
    def get_by_cnpj(self, cnpj):
        contract = GetByCnpjPersonContract()
        if not(contract.validate(cnpj)):
            return ResultModel('Parametro incorreto.', False, contract.errors).to_dict(), 406
        repository = PersonRepository()
        persons = repository.get_by_cnpj_or_cnpj('Pessoa Juridica', cnpj)
        if persons['error']:
            return persons, 500
        return persons, 200

    def update_person(self):
        contract = UpdatePersonContract()
        playload = request.json
        if not(contract.validate(playload)):
            return ResultModel('Problema nos parametros enviados.', False, contract.errors).to_dict(), 406
        repository = PersonRepository()

        person = repository.update_person(playload)
        if person['error']:
            return person, 500
        return person, 200

    def create_person(self):
        contract = CreatePersonContract()
        playload = request.json
        if not(contract.validate(playload)):
            return ResultModel('Problema nos parametros enviados.', False, contract.errors).to_dict(), 406
        repository = PersonRepository()
        cpf = playload.get('cpf')
        cnpj = playload.get('cnpj')
        helper = PersonHelper()
        if cpf:
            playload['cpf'] = helper.remove_characters(cpf)
        if cnpj:
            playload['cnpj'] =  helper.remove_characters(cnpj)
        
        person = repository.create_person(playload)
        if person['error']:
            return person, 500
        return person, 200
    
    def delete_person(self):
        contract = DeletePersonContract()
        playload = request.json
        if not(contract.validate(playload)):
            return ResultModel('Problema nos parametros enviados.', False, contract.errors).to_dict(), 406
        repository = PersonRepository()

        person = repository.delete_person(playload.get('id'))
        if person['error']:
            return person, 500
        return person, 200