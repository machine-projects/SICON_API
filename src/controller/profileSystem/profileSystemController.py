from flask import Blueprint, jsonify, request
from flask_jwt_extended import  jwt_required
from flask import current_app, request
from src.infra.decorator.auth.authDecorator import AuthDecorator
from src.handler.profileSystem.profileSystemHandler import ProfileSystemHandler as ProfileSystem
from src.infra.decorator.request.errorsRequestDecorator import ErrorsRequestDecorator
from src.model.enum.permission import PermissionEnum

controller_profile_system = Blueprint('controller_profile_system', __name__)
jwt = AuthDecorator()
validity_req = ErrorsRequestDecorator()


@controller_profile_system.route('/profilesystem', methods=['GET'])
@jwt.required_permission(PermissionEnum.VIEW.value)
def get_all():
    return  ProfileSystem().get_all() 

@controller_profile_system.route('/profilesystem/params', methods=['GET'])
@jwt.required_permission(PermissionEnum.VIEW.value)
def get_by_params():
    return  ProfileSystem().get_by_params() 

@controller_profile_system.route('/profilesystem', methods=['PUT'])
@jwt.required_permission(PermissionEnum.EDIT.value)
@validity_req.body_is_json
def update():
    return  ProfileSystem().update()

@controller_profile_system.route('/profilesystem', methods=['POST'])
@jwt.required_permission(PermissionEnum.CRAFT.value)
@validity_req.body_is_json
def create():
    return  ProfileSystem().create()

@controller_profile_system.route('/profilesystem', methods=['DELETE'])
@jwt.required_permission(PermissionEnum.DEL.value)
@validity_req.body_is_json
def delete_by_id():
    return  ProfileSystem().delete() 

