from flask import Blueprint, jsonify, request
from flask_jwt_extended import  jwt_required
from flask import current_app, request
from src.infra.decorator.auth.authDecorator import AuthDecorator
from src.handler.systemPermission.systemPermissionHandler import SystemPermission
from src.infra.decorator.request.errorsRequestDecorator import ErrorsRequestDecorator


controller_system_permission = Blueprint('controller_system_permission', __name__)
jwt = AuthDecorator()
validity_req = ErrorsRequestDecorator()


@controller_system_permission.route('/systempermission', methods=['GET'])
@jwt_required
def get_all():
    return  SystemPermission().get_all() 

@controller_system_permission.route('/systempermission/params', methods=['GET'])
@jwt_required
def get_by_params():
    return  SystemPermission().get_by_params() 

@controller_system_permission.route('/systempermission', methods=['PUT'])
@validity_req.body_is_json
@jwt_required
def update():
    return  SystemPermission().update()

@controller_system_permission.route('/systempermission', methods=['POST'])
@jwt_required
@validity_req.body_is_json
def create():
    return  SystemPermission().create()

@controller_system_permission.route('/systempermission', methods=['DELETE'])
@jwt_required
@validity_req.body_is_json
def delete_by_id():
    return  SystemPermission().delete() 


