from src.repository.systemPermission.systemPermissionRepository import SystemPermissionRepository
from src import request
from src.infra.model.resultModel import ResultModel
from src.infra.handler.pagination import Paginate
from src.contract.systemPermission.getByParamsSystemPermissionContract import GetByParamsSystemPermissionContract
from src.contract.systemPermission.updateSystemPermissionContract import UpdateSystemPermissionContract
from src.contract.systemPermission.createSystemPermissionContract import CreateSystemPermissionContract
from src.contract.systemPermission.deleteSystemPermissionContract import DeleteSystemPermissionContract
from src.infra.handler.validationsAndSetStatusResultInfraHandler import ValidationsAndSetStatusResultInfraHandler


class SystemPermission:

    def __init__(self):
        pass

    def get_all(self):
        repository = SystemPermissionRepository()
        playload = Paginate().include_paginate_args_playload(request)
        system_permission = repository.get_all(playload)
        
        status_result = ValidationsAndSetStatusResultInfraHandler()
        return status_result.default(system_permission)

    def get_by_params(self):
        contract = GetByParamsSystemPermissionContract()
        playload = request.args
        if not(contract.validate(playload)):
            return ResultModel('Parametro incorreto.', False, contract.errors).to_dict(), 406
        params_filter = {}
        _id = playload.get('id')
        name = playload.get('name')
        system_id = playload.get('system_id')

        if _id:
            params_filter['id'] = int(_id)
        if name:
            params_filter['name'] = name
        if system_id:
            params_filter['system_id'] = int(system_id)
        
        repository = SystemPermissionRepository()
        system_permission = repository.get_search_by_params(params_filter)
        
        status_result = ValidationsAndSetStatusResultInfraHandler()
        return status_result.default(system_permission)
    
    def update(self):
        contract = UpdateSystemPermissionContract()
        playload = request.json
        if not(contract.validate(playload)):
            return ResultModel('Problema nos parametros enviados.', False, contract.errors).to_dict(), 406
        repository = SystemPermissionRepository()

        system_permission = repository.update(playload)
        
        status_result = ValidationsAndSetStatusResultInfraHandler()
        return status_result.default(system_permission)

    def create(self):
        contract = CreateSystemPermissionContract()
        playload = request.json
        if not(contract.validate(playload)):
            return ResultModel('Problema nos parametros enviados.', False, contract.errors).to_dict(), 406
        repository = SystemPermissionRepository()
        system_permission = repository.create(playload)
        
        status_result = ValidationsAndSetStatusResultInfraHandler()
        return status_result.default(system_permission)
        
    
    def delete(self):
        contract = DeleteSystemPermissionContract()
        playload = request.json
        if not(contract.validate(playload)):
            return ResultModel('Problema nos parametros enviados.', False, contract.errors).to_dict(), 406
        repository = SystemPermissionRepository()

        system = repository.delete(playload.get('id'))
        
        status_result = ValidationsAndSetStatusResultInfraHandler()
        return status_result.default(system)
