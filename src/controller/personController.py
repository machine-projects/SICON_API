from flask import Blueprint, jsonify, request
from flask_jwt_extended import  jwt_required
from flask import current_app, request
from src.infra.decorator.auth.authDecorator import AuthDecorator
from src.handler.person.personHandler import PersonHandler
from src.infra.decorator.request.errorsRequestDecorator import ErrorsRequestDecorator


controller_person = Blueprint('controller_person', __name__)
jwt = AuthDecorator()
validity_req = ErrorsRequestDecorator()



@controller_person.route('/person', methods=['GET'])
# @jwt_required
def get_all():
    return  PersonHandler().get_all_persons() 

@controller_person.route('/person/cpf/<cpf>', methods=['GET'])
# @jwt_required
def get_by_cpf(cpf):
    return  PersonHandler().get_by_cpf(cpf) 

@controller_person.route('/person/cnpj/<cnpj>', methods=['GET'])
# @jwt_required
def get_by_cnpj(cnpj):
    return  PersonHandler().get_by_cnpj(cnpj) 

@controller_person.route('/person', methods=['PUT'])
@validity_req.body_is_json
# @jwt_required
def update():
    return  PersonHandler().update_person()

@controller_person.route('/person', methods=['POST'])
# @jwt_required
@validity_req.body_is_json
def create():
    return  PersonHandler().create_person()

@controller_person.route('/person', methods=['DELETE'])
# @jwt_required
@validity_req.body_is_json
def delete_by_id():
    return  PersonHandler().delete_person() 


