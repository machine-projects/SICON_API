from flask_restful import Resource, marshal
from src.repository.profileSystem.profileSystemRepository import ProfileSystemRepository
from src import db, request
from src.infra.model.resultModel import ResultModel
from src.infra.handler.pagination import Paginate
from src.contract.profileSystem.createProfileSystemContract import CreateProfileSystemContract
from src.contract.profileSystem.getByParamsProfileSystemContract import GetByParamsProfileSystemContract
from src.contract.profileSystem.updateProfileSystemContract import UpdateProfileSystemContract
from src.contract.profileSystem.deleteProfileSystemContract import DeleteProfileSystemContract
from src.infra.handler.validationsAndSetStatusResultInfraHandler import ValidationsAndSetStatusResultInfraHandler


class ProfileSystemHandler:

    def __init__(self):
        pass

    def get_all(self):
        repository = ProfileSystemRepository()
        playload = Paginate().include_paginate_args_playload(request)
        profiles_systems = repository.get_all_profiles_systems(playload)
        
        status_result = ValidationsAndSetStatusResultInfraHandler()
        return status_result.default(profiles_systems)

    def get_by_params(self):
        contract = GetByParamsProfileSystemContract()
        playload = request.args
        if not(contract.validate(playload)):
            return ResultModel('Parametro incorreto.', False, contract.errors).to_dict(), 406
        params_filter = {}
        _id = playload.get('id')
        name = playload.get('name')
        system_id = playload.get('system_id')

        if _id:
            params_filter['id'] = _id
        if name:
            params_filter['name'] = name
        if system_id:
            params_filter['system_id'] = system_id
        
        repository = ProfileSystemRepository()
        profile_system = repository.get_search_by_params(params_filter)
        
        status_result = ValidationsAndSetStatusResultInfraHandler()
        return status_result.default(profile_system)

    def update(self):
        contract = UpdateProfileSystemContract()
        playload = request.json
        if not(contract.validate(playload)):
            return ResultModel('Problema nos parametros enviados.', False, contract.errors).to_dict(), 406
        repository = ProfileSystemRepository()

        profile_system = repository.update(playload)
        
        status_result = ValidationsAndSetStatusResultInfraHandler()
        return status_result.default(profile_system)

    def create(self):
        contract = CreateProfileSystemContract()
        playload = request.json
        if not(contract.validate(playload)):
            return ResultModel('Problema nos parametros enviados.', False, contract.errors).to_dict(), 406
        repository = ProfileSystemRepository()
        person = repository.create(playload)
        status_result = ValidationsAndSetStatusResultInfraHandler()
        return status_result.default(person)
        
    
    def delete(self):
        contract = DeleteProfileSystemContract()
        playload = request.json
        if not(contract.validate(playload)):
            return ResultModel('Problema nos parametros enviados.', False, contract.errors).to_dict(), 406
        repository = ProfileSystemRepository()

        profile_system = repository.delete(playload.get('id'))
        
        status_result = ValidationsAndSetStatusResultInfraHandler()
        return status_result.default(profile_system)
