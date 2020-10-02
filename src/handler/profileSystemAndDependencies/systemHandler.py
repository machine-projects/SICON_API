from src.repository.system.systemRepository import SystemRepository
from src import request
from src.infra.model.resultModel import ResultModel
from src.infra.handler.pagination import Paginate
from src.contract.system.createSystemContract import CreateSystemContract
from src.contract.system.getByParamsSystemContract import GetByParamsSystemContract
from src.contract.system.updateSystemContract import UpdateSystemContract
from src.contract.system.deleteSystemContract import DeleteSystemContract
from src.infra.handler.validationsAndSetStatusResultInfraHandler import ValidationsAndSetStatusResultInfraHandler


class SystemHandler:

    def __init__(self):
        pass

    def get_all(self):
        repository = SystemRepository()
        playload = Paginate().include_paginate_args_playload(request)
        systems = repository.get_all_systems(playload)
        
        status_result = ValidationsAndSetStatusResultInfraHandler()
        return status_result.default(systems)

    def get_by_params(self):
        contract = GetByParamsSystemContract()
        playload = request.args
        if not(contract.validate(playload)):
            return ResultModel('Parametro incorreto.', False, contract.errors).to_dict(), 406
        params_filter = {}
        _id = playload.get('id')
        name = playload.get('name')
        url = playload.get('url')

        if _id:
            params_filter['id'] = _id
        if name:
            params_filter['name'] = name
        if url:
            params_filter['url'] = url
        
        repository = SystemRepository()
        systems = repository.get_search_by_params(params_filter)
        
        status_result = ValidationsAndSetStatusResultInfraHandler()
        return status_result.default(systems)
    
    def update(self):
        contract = UpdateSystemContract()
        playload = request.json
        if not(contract.validate(playload)):
            return ResultModel('Problema nos parametros enviados.', False, contract.errors).to_dict(), 406
        repository = SystemRepository()

        system = repository.update(playload)
        
        status_result = ValidationsAndSetStatusResultInfraHandler()
        return status_result.default(system)

    def create(self):
        contract = CreateSystemContract()
        playload = request.json
        if not(contract.validate(playload)):
            return ResultModel('Problema nos parametros enviados.', False, contract.errors).to_dict(), 406
        repository = SystemRepository()
        system = repository.create(playload)
        
        status_result = ValidationsAndSetStatusResultInfraHandler()
        return status_result.default(system)
        
    
    def delete(self):
        contract = DeleteSystemContract()
        playload = request.json
        if not(contract.validate(playload)):
            return ResultModel('Problema nos parametros enviados.', False, contract.errors).to_dict(), 406
        repository = SystemRepository()

        system = repository.delete(playload.get('id'))
        
        status_result = ValidationsAndSetStatusResultInfraHandler()
        return status_result.default(system)
