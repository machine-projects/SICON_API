from flask import Blueprint, jsonify, request
from flask_jwt_extended import  jwt_required
from flask import current_app, request
from src.infra.decorator.auth.authDecorator import AuthDecorator
from src.handler.systemPermission.systemPermissionHandler import SystemPermission
from src.infra.decorator.request.errorsRequestDecorator import ErrorsRequestDecorator
from src.model.enum.permission import PermissionEnum


controller_system_permission = Blueprint('controller_system_permission', __name__)
jwt = AuthDecorator()
validity_req = ErrorsRequestDecorator()


@controller_system_permission.route('/systempermission', methods=['GET'])
@jwt.required_permission(PermissionEnum.VIEW.value)
def get_all():
    return  SystemPermission().get_all() 

@controller_system_permission.route('/systempermission/params', methods=['GET'])
@jwt.required_permission(PermissionEnum.VIEW.value)
def get_by_params():
    return  SystemPermission().get_by_params() 

@controller_system_permission.route('/systempermission', methods=['PUT'])
@jwt.required_permission(PermissionEnum.EDIT.value)
@validity_req.body_is_json
def update():
    return  SystemPermission().update()

@controller_system_permission.route('/systempermission', methods=['POST'])
@jwt.required_permission(PermissionEnum.CRAFT.value)
@validity_req.body_is_json
def create():
    return  SystemPermission().create()

@controller_system_permission.route('/systempermission', methods=['DELETE'])
@jwt.required_permission(PermissionEnum.DEL.value)
@validity_req.body_is_json
def delete_by_id():
    return  SystemPermission().delete() 

