from src.model.system import System
from src import db
from flask import current_app
from flask_restful import marshal
from src.model.schemas import PAGINATE
from src.model.schemas.system import system_fields, system_fields_with_dates
from src.infra.model.resultModel import ResultModel


class SystemRepository:
    

    def get_all(self, playload):
        try:
            paginate_filter = playload.get('paginate')
            page = paginate_filter.get('page')
            per_page = paginate_filter.get('per_page')

            system = System.query.filter().paginate(page, per_page)
            data_paginate = marshal(system, PAGINATE)
            data = marshal(system.items, system_fields)
            return ResultModel('Pesquisa realizada com sucesso.', data, False).to_dict(data_paginate)
        except Exception as e:
            return ResultModel('Não foi possivel realizar a pesquisa.', False, True, str(e)).to_dict()

    def get_search_by_params(self, playload, witch_dates=False):
        try:
            paginate_filter = playload.get('paginate')
            data_filter = playload.get('data')
            page = paginate_filter.get('page')
            per_page = paginate_filter.get('per_page')
           
            system = System.query.filter_by(**data_filter).all()
            data_paginate = marshal(system, PAGINATE)
       
            data = marshal(system, system_fields)
            return ResultModel('Pesquisa realizada com sucesso.', data, False).to_dict(data_paginate)
        except Exception as e:
            return ResultModel('Não foi possivel realizar a pesquisa.', False, True, str(e)).to_dict()

    def get_by_id(self, _id, witch_dates=False):
        try:      
            system = System.query.get(_id)
            data = marshal(system, system_fields)
            return ResultModel('Pesquisa realizada com sucesso.', data, False).to_dict()
        except Exception as e:
            return ResultModel('Não foi possivel realizar a pesquisa.', False, True, str(e)).to_dict()

    def create(self, playload):
        try:
            name = playload.get('name')

            system_by_name = System.query.filter_by(name=name).first()
            if system_by_name:
                return ResultModel(f'O Sistema "{name}" já existe.', False, True).to_dict()
           
            system = System(playload)
            db.session.add(system)
            db.session.commit()
            data = marshal(system, system_fields)
            return ResultModel('Sistema criado com sucesso.', data, False).to_dict()
        except Exception as e:
            return ResultModel('Não foi possivel criar o usuario.', False, True, str(e)).to_dict()
    

    def update(self, playload):
        try:
            _id = playload.get('id')
            name = playload.get('name')
            description = playload.get('description')
            url = playload.get('url')
            system = System.query.get(_id)
            if not system:
                return ResultModel('Sistema não existe.', False, True).to_dict()
            system.name = name
            system.description = description
            system.url = url
            db.session.add(system)
            db.session.commit()
            data = marshal(system, system_fields)
            return ResultModel('Atualizado com sucesso.', data, False).to_dict()
        except Exception as e:
            return ResultModel('Não foi possivel atualizar.', False, True, str(e)).to_dict()

    def delete(self, _id):
        try:
            system = System.query.get(_id)
            if not system:
                return ResultModel('Sistema não encontrado.', False, True).to_dict()
            db.session.delete(system)
            db.session.commit()
            data = marshal(system, system_fields)
            return ResultModel('Sistema deletado com sucesso.', data, False).to_dict()
        except Exception as e:
            return ResultModel('Não foi possivel deletar o sistema.', False, True, str(e)).to_dict()
