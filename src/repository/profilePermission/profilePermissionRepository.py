from src.model.profilePermission import ProfilePermission
from src import db
from flask import current_app
from flask_restful import marshal
from src.model.schemas import PAGINATE
from src.model.schemas.profilePermission import profile_permission_fields
from src.infra.model.resultModel import ResultModel, ResultErrorModel
from src.repository.systemPermission.systemPermissionRepository import  SystemPermissionRepository


class ProfilePermissionRepository:
    

    def get_all(self, playload):
        try:
            page = playload.get('page')
            per_page = playload.get('per_page')

            profile_permission = ProfilePermission.query.filter(**playload).paginate(page, per_page)
            data_paginate = marshal(profile_permission, PAGINATE)
            data = marshal(profile_permission.items, profile_permission_fields)
            return ResultModel('Pesquisa realizada com sucesso.', data, False).to_dict(data_paginate)
        except Exception as e:
            return ResultModel('Não foi possivel realizar a pesquisa.', False, True, str(e)).to_dict()

    def get_search_by_params(self, playload, witch_dates=False):
        try:
            page = playload.get('page')
            per_page = playload.get('per_page')
           
            profile_permission = ProfilePermission.query.filter_by(**playload).all()
            data_paginate = marshal(profile_permission, PAGINATE)
            data = marshal(profile_permission, profile_permission_fields)
            return ResultModel('Pesquisa realizada com sucesso.', data, False).to_dict(data_paginate)
        except Exception as e:
            return ResultModel('Não foi possivel realizar a pesquisa.', False, True, str(e)).to_dict()

    def create(self, playload):
        try:
            profile_system_id = playload.get('profile_system_id')
            system_permisions_ids = playload.get('system_permisions_ids')
            search_system_permision_ids = SystemPermissionRepository().search_multiples_ids({'ids':system_permisions_ids})
            if len(search_system_permision_ids['data']['result']) != len(system_permisions_ids):
                result_error = ResultErrorModel()
                system_permisions_invalid_ids = system_permisions_ids.copy()
                for search_system_permision_id in search_system_permision_ids['data']['result']:
                    if search_system_permision_id.get('id') in system_permisions_invalid_ids:
                        system_permisions_invalid_ids.remove(search_system_permision_id.get('id'))
                for invalid_id in  system_permisions_invalid_ids:
                    result_error.add_error('system_permision_id', f'O ID {invalid_id} não existe')
                return ResultModel(f'Dados invalidos.', False, result_error.errors).to_dict()

            profile_system_id = playload.get('profile_system_id')
            data = []
            for system_permission_id in system_permisions_ids:
                
                new_profile_permission = ProfilePermission(dict(
                profile_system_id= profile_system_id,
                system_permission_id = system_permission_id,
                    )
                    )
                db.session.add(new_profile_permission)
                data.append(new_profile_permission)
            db.session.flush()
            db.session.commit()
            data = marshal(data, profile_permission_fields)
            return ResultModel('Permissão criado com sucesso.', data, False).to_dict()
        except Exception as e:
            return ResultModel('Não foi possivel criar o usuario.', False, True, str(e)).to_dict()
    
    def update(self, playload):
        try:
            _id = playload.get('id')
            profile_permission = playload.get('profile_permission')
            system_permision_id = playload.get('system_permision_id')
            profile_permission = ProfilePermission.query.get(_id)
            if not profile_permission:
                return ResultModel('Id não encontrado.', False, True).to_dict()
            profile_permission.profile_permission = profile_permission
            profile_permission.system_permision_id = system_permision_id
            db.session.add(profile_permission)
            db.session.commit()
            data = marshal(profile_permission, profile_permission_fields)
            return ResultModel('Permissão atualizado com sucesso.', data, False).to_dict()
        except Exception as e:
            return ResultModel('Não foi possivel atualizar a permissão.', False, True, str(e)).to_dict()

    def delete(self, _id):
        try:
            profile_permission = ProfilePermission.query.get(_id)
            if not profile_permission:
                return ResultModel('Não encontrado.', False, True).to_dict()
            db.session.delete(profile_permission)
            db.session.commit()
            data = marshal(profile_permission, profile_permission_fields)
            return ResultModel('Deletado com sucesso.', data, False).to_dict()
        except Exception as e:
            return ResultModel('Não foi possivel deletar.', False, True, str(e)).to_dict()
