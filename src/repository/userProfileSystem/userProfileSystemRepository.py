from src.model.userProfileSystem import UserProfileSystem
from src import db
from flask import current_app
from flask_restful import marshal
from src.model.schemas import PAGINATE
from src.model.schemas.userProfileSystem import user_profile_system_fields
from src.infra.model.resultModel import ResultModel


class UserProfileSystemRepository:
    

    def get_all(self, playload):
        try:
            page = playload.get('page')
            per_page = playload.get('per_page')

            user_profile_system = UserProfileSystem.query.filter().paginate(page, per_page)
            data_paginate = marshal(user_profile_system, PAGINATE)
            data = marshal(user_profile_system.items, user_profile_system_fields)
            return ResultModel('Pesquisa realizada com sucesso.', data, False).to_dict(data_paginate)
        except Exception as e:
            return ResultModel('Não foi possivel realizar a pesquisa.', False, True, str(e)).to_dict()

    def get_search_by_params(self, playload, witch_dates=False):
        try:
            page = playload.get('page')
            per_page = playload.get('per_page')
           
            user_profile_system = UserProfileSystem.query.filter_by(**playload).all()
            data_paginate = marshal(user_profile_system, PAGINATE)
            data = marshal(user_profile_system.items, user_profile_system_fields)
            return ResultModel('Pesquisa realizada com sucesso.', data, False).to_dict(data_paginate)
        except Exception as e:
            return ResultModel('Não foi possivel realizar a pesquisa.', False, True, str(e)).to_dict()

    def create(self, playload):
        try:
            user_id = playload.get('user_id')
            profile_system_id = playload.get('profile_system_id')

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
