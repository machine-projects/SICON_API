from flask import Blueprint, jsonify, request
from flask_jwt_extended import  jwt_required
from flask import current_app, request
from src.infra.decorator.auth.authDecorator import AuthDecorator
from src.handler.person.personHandler import PersonHandler
from src.infra.decorator.request.errorsRequestDecorator import ErrorsRequestDecorator
from src.model.enum.permission import PermissionEnum

controller_person = Blueprint('controller_person', __name__)
jwt = AuthDecorator()
validity_req = ErrorsRequestDecorator()


@controller_person.route('/person', methods=['GET'])
@jwt.required_permission(PermissionEnum.VIEW.value)
def get_all():
    return  PersonHandler().get_all_persons() 

@controller_person.route('/person/params', methods=['GET'])
@jwt.required_permission(PermissionEnum.VIEW.value)
def get_by_params():
    return  PersonHandler().get_by_params() 


@controller_person.route('/person', methods=['PUT'])
@jwt.required_permission(PermissionEnum.EDIT.value)
@validity_req.body_is_json
def update():
    return  PersonHandler().update_person()

@controller_person.route('/person', methods=['POST'])
@jwt.required_permission(PermissionEnum.CRAFT.value)
@validity_req.body_is_json
def create():
    return  PersonHandler().create_person()

@controller_person.route('/person', methods=['DELETE'])
@jwt.required_permission(PermissionEnum.DEL.value)
@validity_req.body_is_json
def delete_by_id():
    return  PersonHandler().delete_person() 


