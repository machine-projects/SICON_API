from src.model.sytemPermission import SystemPermission
from src.repository.system.systemRepository import  SystemRepository
from src import db
from flask import current_app
from flask_restful import marshal
from src.model.schemas import PAGINATE
from src.model.schemas.systemPermission import system_permission_fields
from src.infra.model.resultModel import ResultModel


class SystemPermissionRepository:
    

    def get_all(self, playload):
        try:
            page = playload.get('page')
            per_page = playload.get('per_page')

            system_permission = SystemPermission.query.filter().paginate(page, per_page)
            data_paginate = marshal(system_permission, PAGINATE)
            data = marshal(system_permission.items, system_permission_fields)
            return ResultModel('Pesquisa realizada com sucesso.', data, False).to_dict(data_paginate)
        except Exception as e:
            return ResultModel('Não foi possivel realizar a pesquisa.', False, True, str(e)).to_dict()

    def get_search_by_params(self, playload, witch_dates=False):
        try:
            page = playload.get('page')
            per_page = playload.get('per_page')
           
            system_permission = SystemPermission.query.filter_by(**playload).all()
            data_paginate = marshal(system_permission, PAGINATE)
            data = marshal(system_permission, system_permission_fields)
            return ResultModel('Pesquisa realizada com sucesso.', data, False).to_dict(data_paginate)
        except Exception as e:
            return ResultModel('Não foi possivel realizar a pesquisa.', False, True, str(e)).to_dict()
    
    def search_multiples_ids(self, playload):
        try:
            page = playload.get('page')
            per_page = playload.get('per_page')
            ids = playload.get('ids')
            system_permission = SystemPermission.query.filter(SystemPermission.id.in_(ids)).all()
            data_paginate = marshal(system_permission, PAGINATE)
            data = marshal(system_permission, system_permission_fields)
            return ResultModel('Pesquisa realizada com sucesso.', data, False).to_dict(data_paginate)
        except Exception as e:
            return ResultModel('Não foi possivel realizar a pesquisa.', False, True, str(e)).to_dict()

    def create(self, playload):
        try:
            name = playload.get('name')
            system_id = playload.get('system_id')

            system_repository = SystemRepository()
            system_exist = system_repository.get_search_by_params({'id': system_id})
            if not system_exist['data']['result']:
                return ResultModel(f'Não existe sistema com id "{system_id}".', False, True).to_dict()

            system_permission_exist = SystemPermission.query.filter_by(name=name, system_id=system_id).first()
            if system_permission_exist:
                return ResultModel(f'A permissão "{name}" já existe.', False, True).to_dict()
           
            system_permission = SystemPermission(playload)
            db.session.add(system_permission)
            db.session.commit()
            data = marshal(system_permission, system_permission_fields)
            return ResultModel('Permissão criado com sucesso.', data, False).to_dict()
        except Exception as e:
            return ResultModel('Não foi possivel criar a permissão.', False, True, str(e)).to_dict()
    

    def update(self, playload):
        try:
            _id = playload.get('id')
            name = playload.get('name')
            description = playload.get('description')
            url = playload.get('url')
            system_permission = SystemPermission.query.get(_id)
            if not system_permission:
                return ResultModel('Id não encontrado.', False, True).to_dict()
            system_permission.name = name
            system_permission.description = description
            system_permission.url = url
            db.session.add(system_permission)
            db.session.commit()
            data = marshal(system_permission, system_permission_fields)
            return ResultModel('Permissão atualizado com sucesso.', data, False).to_dict()
        except Exception as e:
            return ResultModel('Não foi possivel atualizar a permissão.', False, True, str(e)).to_dict()

    def delete(self, _id):
        try:
            system_permission = SystemPermission.query.get(_id)
            if not system_permission:
                return ResultModel('Permissão não encontrado.', False, True).to_dict()
            db.session.delete(system_permission)
            db.session.commit()
            data = marshal(system_permission, system_permission_fields)
            return ResultModel('Permissão deletado com sucesso.', data, False).to_dict()
        except Exception as e:
            return ResultModel('Não foi possivel deletar a permissão.', False, True, str(e)).to_dict()
