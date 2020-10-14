from src.model.userProfileSystem import UserProfileSystem
from src import db
from flask import current_app
from flask_restful import marshal
from src.model.schemas import PAGINATE
from src.model.schemas.userProfileSystem import user_profile_system_fields
from src.infra.model.resultModel import ResultModel
from src.repository.user.userRepository import  UserRepository
from src.repository.profileSystem.profileSystemRepository import ProfileSystemRepository


class UserProfileSystemRepository:
    

    def get_all(self, playload):
        try:
            paginate_filter = playload.get('paginate')
            page = paginate_filter.get('page')
            per_page = paginate_filter.get('per_page')

            user_profile_system = UserProfileSystem.query.filter().paginate(page, per_page)
            data_paginate = marshal(user_profile_system, PAGINATE)
            data = marshal(user_profile_system.items, user_profile_system_fields)
            return ResultModel('Pesquisa realizada com sucesso.', data, False).to_dict(data_paginate)
        except Exception as e:
            return ResultModel('Não foi possivel realizar a pesquisa.', False, True, str(e)).to_dict()

    def get_search_by_params(self, playload, witch_dates=False):
        try:
            paginate_filter = playload.get('paginate')
            data_filter = playload.get('data')
            page = paginate_filter.get('page')
            per_page = paginate_filter.get('per_page')
           
            user_profile_system = UserProfileSystem.query.filter_by(**data_filter).all()
            data_paginate = marshal(user_profile_system, PAGINATE)
            data = marshal(user_profile_system, user_profile_system_fields)
            return ResultModel('Pesquisa realizada com sucesso.', data, False).to_dict(data_paginate)
        except Exception as e:
            return ResultModel('Não foi possivel realizar a pesquisa.', False, True, str(e)).to_dict()

    def create(self, playload):
        try:
            user_id = playload.get('user_id')
            profile_system_id = playload.get('profile_system_id')
            user_id_exist= UserRepository().get_by_id(user_id)
            if not user_id_exist['data']['result']['id']:
                return ResultModel(f'O ID {user_id} de usuário não existe.', False, True).to_dict()
            
            profile_system_id_exist= ProfileSystemRepository().get_by_id(profile_system_id)
            if not profile_system_id_exist['data']['result']['id']:
                return ResultModel(f'O ID {profile_system_id} de perfil de sistema não existe.', False, True).to_dict()
            
            user_profile_system_exist = UserProfileSystem.query.filter_by(user_id=user_id, profile_system_id=profile_system_id).first()
            if user_profile_system_exist:
                return ResultModel(f'Esses dados já foram cadastrados.', False, True).to_dict()
           
            user_profile_system = UserProfileSystem(playload)
            db.session.add(user_profile_system)
            db.session.commit()
            data = marshal(user_profile_system, user_profile_system_fields)
            return ResultModel('Criado com sucesso.', data, False).to_dict()
        except Exception as e:
            return ResultModel('Não foi possivel criar.', False, True, str(e)).to_dict()
    
    # def create_multiples(self, playload):
    #     try:
    #         profile_system_id = playload.get('profile_system_id')
    #         system_permisions_ids = playload.get('system_permisions_ids')
    #         search_system_permision_ids = SystemPermissionRepository().search_multiples_ids({'ids':system_permisions_ids})
    #         if len(search_system_permision_ids['data']['result']) != len(system_permisions_ids):
    #             result_error = ResultErrorModel()
    #             system_permisions_invalid_ids = system_permisions_ids.copy()
    #             for search_system_permision_id in search_system_permision_ids['data']['result']:
    #                 if search_system_permision_id.get('id') in system_permisions_invalid_ids:
    #                     system_permisions_invalid_ids.remove(search_system_permision_id.get('id'))
    #             for invalid_id in  system_permisions_invalid_ids:
    #                 result_error.add_error('system_permision_id', f'O ID {invalid_id} não existe')
    #             return ResultModel(f'Dados invalidos.', False, result_error.errors).to_dict()

    #         profile_system_id = playload.get('profile_system_id')
    #         data = []
    #         for system_permission_id in system_permisions_ids:
                
    #             new_profile_permission = ProfilePermission(dict(
    #             profile_system_id= profile_system_id,
    #             system_permission_id = system_permission_id,
    #                 )
    #                 )
    #             db.session.add(new_profile_permission)
    #             data.append(new_profile_permission)
    #         db.session.flush()
    #         db.session.commit()
    #         data = marshal(data, profile_permission_fields)
    #         return ResultModel('Permissão criado com sucesso.', data, False).to_dict()
    #     except Exception as e:
    #         return ResultModel('Não foi possivel criar o usuario.', False, True, str(e)).to_dict()
    

    def update(self, playload):
        try:
            _id = playload.get('id')
            user_id = playload.get('user_id')
            profile_system_id = playload.get('profile_system_id')
            user_profile_system = UserProfileSystem.query.get(_id)
            if not user_profile_system:
                return ResultModel('Id não encontrado.', False, True).to_dict()
            
            user_profile_system.user_id = user_id
            user_profile_system.profile_system_id = profile_system_id
            db.session.add(user_profile_system)
            db.session.commit()
            data = marshal(user_profile_system, user_profile_system_fields)
            return ResultModel('Atualizado com sucesso.', data, False).to_dict()
        except Exception as e:
            return ResultModel('Não foi possivel atualizar.', False, True, str(e)).to_dict()

    def delete(self, _id):
        try:
            user_profile_system = UserProfileSystem.query.get(_id)
            if not user_profile_system:
                return ResultModel('Não encontrado.', False, True).to_dict()
            db.session.delete(user_profile_system)
            db.session.commit()
            data = marshal(user_profile_system, user_profile_system_fields)
            return ResultModel('Deletado com sucesso.', data, False).to_dict()
        except Exception as e:
            return ResultModel('Não foi possivel deletar.', False, True, str(e)).to_dict()
