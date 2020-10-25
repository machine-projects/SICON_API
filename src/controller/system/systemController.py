from flask import Blueprint, jsonify, request, current_app
from flask_jwt_extended import  jwt_required
from src.infra.decorator.auth.authDecorator import AuthDecorator
from src.infra.decorator.request.errorsRequestDecorator import ErrorsRequestDecorator
from src.handler.system.systemHandler import SystemHandler as System
from src.model.enum.permission import PermissionEnum

controller_system = Blueprint('controller_system', __name__)
jwt = AuthDecorator()
validity_req = ErrorsRequestDecorator()



@controller_system.route('/system', methods=['GET'])
@jwt.required_permission(PermissionEnum.VIEW.value)
def get_all():
    return  System().get_all() 

@controller_system.route('/system/params', methods=['GET'])
@jwt.required_permission(PermissionEnum.VIEW.value)
def get_by_params():
    return  System().get_by_params() 

@controller_system.route('/system', methods=['PUT'])
@jwt.required_permission(PermissionEnum.EDIT.value)
@validity_req.body_is_json
def update():
    return  System().update()

@controller_system.route('/system', methods=['POST'])
@jwt.required_permission(PermissionEnum.CRAFT.value)
@validity_req.body_is_json
def create():
    return  System().create()

@controller_system.route('/system', methods=['DELETE'])
@jwt.required_permission(PermissionEnum.DEL.value)
@validity_req.body_is_json
def delete_by_id():
    return  System().delete() 

