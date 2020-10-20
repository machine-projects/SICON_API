from flask_restful import Resource, marshal
from src.repository.userProfileSystem.userProfileSystemRepository import UserProfileSystemRepository
from src.repository.user.userRepository import UserRepository
from src import db, request
from src.infra.model.resultModel import ResultModel
from src.infra.handler.pagination import Paginate
from src.contract.userProfileSystem.createContract import CreateUserProfileSystemContract
from src.contract.userProfileSystem.createMultiplesUsersContract import CreateMultiplesUserProfileSystemContract
from src.contract.userProfileSystem.getByParamsUserProfileSystemContract import GetByParamsUserProfileSystemContract
from src.contract.userProfileSystem.updateUserProfileSystemContract import UpdateUserProfileSystemContract
from src.contract.userProfileSystem.deleteUserProfileSystemContract import DeleteUserProfileSystemContract
from src.infra.handler.setStatusResponseHandler import SetStatusResponseHandler


class UserProfileSystemHandler:

    def __init__(self):
        pass

    def get_all(self):
        repository = UserProfileSystemRepository()
        playload = Paginate().include_paginate_args_playload(request)
        profiles_systems = repository.get_all(playload)
        
        status_result = SetStatusResponseHandler()
        return status_result.default(profiles_systems)

    def get_by_params(self):
        contract = GetByParamsUserProfileSystemContract()
        playload = request.args
        if not(contract.validate(playload)):
            return ResultModel('Parametro incorreto.', False, contract.errors).to_dict(), 406
        params_filter = {}
        _id = playload.get('id')
        user_id = playload.get('user_id')
        profile_system_id = playload.get('profile_system_id')
        system_id = playload.get('system_id')

        if _id:
            params_filter['id'] = int(_id)
        if user_id:
            params_filter['user_id'] = int(user_id)
        if profile_system_id:
            params_filter['profile_system_id'] = int(profile_system_id)
        if system_id:
            params_filter['system_id'] = int(system_id)
        
        repository = UserProfileSystemRepository()
        _filter = Paginate().include_paginate_args_playload(request)
        _filter['data'] = params_filter
        user_profile_system = repository.get_search_by_params(_filter)
        
        status_result = SetStatusResponseHandler()
        return status_result.default(user_profile_system)

    def update(self):
        contract = UpdateUserProfileSystemContract()
        playload = request.json
        if not(contract.validate(playload)):
            return ResultModel('Problema nos parametros enviados.', False, contract.errors).to_dict(), 406
        repository = UserProfileSystemRepository()

        user_profile_system = repository.update(playload)
        
        status_result = SetStatusResponseHandler()
        return status_result.default(user_profile_system)

    def create(self):
        contract = CreateUserProfileSystemContract()
        playload = request.json
        if not(contract.validate(playload)):
            return ResultModel('Problema nos parametros enviados.', False, contract.errors).to_dict(), 406
        repository = UserProfileSystemRepository()
        user_profile_system = repository.create(playload)
        status_result = SetStatusResponseHandler()
        return status_result.default(user_profile_system)
    
    def create_witch_multiples_users(self):
        contract = CreateUserProfileSystemContract()
        playload = request.json
        if not(contract.validate(playload)):
            return ResultModel('Problema nos parametros enviados.', False, contract.errors).to_dict(), 406
        
        repository = UserProfileSystemRepository()
        user_profile_system = repository.create(playload)
        status_result = SetStatusResponseHandler()
        return status_result.default(user_profile_system)
        
    
    def delete(self):
        contract = DeleteUserProfileSystemContract()
        playload = request.json
        if not(contract.validate(playload)):
            return ResultModel('Problema nos parametros enviados.', False, contract.errors).to_dict(), 406
        repository = UserProfileSystemRepository()

        user_profile_system = repository.delete(playload.get('id'))
        
        status_result = SetStatusResponseHandler()
        return status_result.default(user_profile_system)
