from src.repository.profilePermission.profilePermissionRepository import ProfilePermissionRepository
from src import request
from src.infra.model.resultModel import ResultModel
from src.infra.handler.pagination import Paginate
from src.contract.profilePermission.getByParamsProfilePermissionContract import GetByParamsProfilePermissionContract
from src.contract.profilePermission.createProfilePermissionContract import CreateProfilePermissionContract
from src.contract.profilePermission.updateProfilePermissionContract import UpdateProfilePermissionContract
from src.contract.profilePermission.deleteProfilePermissionContract import DeleteProfilePermissionContract
from src.infra.handler.validationsAndSetStatusResultInfraHandler import ValidationsAndSetStatusResultInfraHandler


class ProfilePermissionHandler:

    def __init__(self):
        pass

    def get_all(self):
        repository = ProfilePermissionRepository()
        playload = Paginate().include_paginate_args_playload(request)
        profile_permission = repository.get_all(playload)
        
        status_result = ValidationsAndSetStatusResultInfraHandler()
        return status_result.default(profile_permission)

    def get_by_params(self):
        contract = GetByParamsProfilePermissionContract()
        playload = request.args
        if not(contract.validate(playload)):
            return ResultModel('Parametro incorreto.', False, contract.errors).to_dict(), 406
        params_filter = {}
        profile_system_id = playload.get('profile_system_id')
        system_permission_id = playload.get('system_permission_id')
        _id = playload.get('id')

        if _id:
            params_filter['id'] = int(_id)
        if profile_system_id:
            params_filter['profile_system_id'] = int(profile_system_id)
        if system_permission_id:
            params_filter['system_permission_id'] = int(system_permission_id)
        repository = ProfilePermissionRepository()
        profile_permission = repository.get_search_by_params(params_filter)
        
        status_result = ValidationsAndSetStatusResultInfraHandler()
        return status_result.default(profile_permission)
    
    def update(self):
        contract = UpdateProfilePermissionContract()
        playload = request.json
        if not(contract.validate(playload)):
            return ResultModel('Problema nos parametros enviados.', False, contract.errors).to_dict(), 406
        repository = ProfilePermissionRepository()

        profile_permission = repository.update(playload)
        
        status_result = ValidationsAndSetStatusResultInfraHandler()
        return status_result.default(profile_permission)

    def create(self):
        contract = CreateProfilePermissionContract()
        playload = request.json
        if not(contract.validate(playload)):
            return ResultModel('Problema nos parametros enviados.', False, contract.errors).to_dict(), 406
        repository = ProfilePermissionRepository()
        # data = []
        # for system_permision_id in playload['system_permisions_ids']:
        #     data.append(dict(
        #         system_permision_id=system_permision_id,
        #         profile_system_id=playload.get('profile_system_id')
        #     ))

        profile_permission = repository.create(playload)
        
        status_result = ValidationsAndSetStatusResultInfraHandler()
        return status_result.default(profile_permission)
        
    
    def delete(self):
        contract = DeleteProfilePermissionContract()
        playload = request.json
        if not(contract.validate(playload)):
            return ResultModel('Problema nos parametros enviados.', False, contract.errors).to_dict(), 406
        repository = ProfilePermissionRepository()

        profile_permission = repository.delete(playload.get('id'))
        
        status_result = ValidationsAndSetStatusResultInfraHandler()
        return status_result.default(profile_permission)
