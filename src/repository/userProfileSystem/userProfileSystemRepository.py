from src.model.userProfileSystem import UserProfileSystem
from src import db
from flask import current_app
from flask_restful import marshal
from src.model.schemas import PAGINATE
from src.model.schemas.userProfileSystem import user_profile_system_fields
from src.infra.model.resultModel import ResultModel
from src.repository.user.userRepository import  UserRepository
from src.repository.profileSystem.profileSystemRepository import ProfileSystemRepository
from src.infra.model.resultModel import ResultErrorModel

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
    
    def create_multiples(self, playload):
        try:
            profile_system_id = playload.get('profile_system_id')
            users_ids = playload.get('users_ids')

            exist_profile_system_id = ProfileSystemRepository().get_by_id(profile_system_id)
            if not exist_profile_system_id['data']['result']['id']:
                err_exist_ps_id = ResultErrorModel().add_error('profile_system_id', f'O ID {profile_system_id} não existe')
                return ResultModel(f'ID invalido.', False, err_exist_ps_id.errors).to_dict()

            exist_users = UserRepository().search_multiples_ids({'ids':users_ids})
            if len(exist_users['data']['result']) != len(users_ids):
                err_user = ResultErrorModel()
                users_invalid_ids = users_ids.copy()
                for user in exist_users['data']['result']:
                    if user.get('id') in users_invalid_ids:
                        users_invalid_ids.remove(user.get('id'))
                for invalid_id in  users_invalid_ids:
                    err_user.add_error('system_permision_id', f'O ID {invalid_id} não existe')
                return ResultModel(f'Dados invalidos.', False, err_user.errors).to_dict()
            data = []
            for user_id in users_ids:
                new_user_profile_system = UserProfileSystem(dict(
                profile_system_id= profile_system_id,
                user_id = user_id))
                db.session.add(new_user_profile_system)
                data.append(new_user_profile_system)
            db.session.flush()
            db.session.commit()
            data = marshal(data, user_profile_system_fields)
            return ResultModel('Permissão criado com sucesso.', data, False).to_dict()
        except Exception as e:
            return ResultModel('Não foi possivel criar o usuario.', False, True, str(e)).to_dict()
    

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
