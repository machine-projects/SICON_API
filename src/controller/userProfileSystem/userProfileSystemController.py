from flask import Blueprint, jsonify, request
from flask_jwt_extended import  jwt_required
from flask import current_app, request
from src.infra.decorator.auth.authDecorator import AuthDecorator
from src.handler.userProfileSystem.userProfileSystemHandler import UserProfileSystemHandler as UserProfileSystem
from src.infra.decorator.request.errorsRequestDecorator import ErrorsRequestDecorator
from src.model.enum.permission import PermissionEnum


controller_user_profile_system = Blueprint('controller_user_profile_system', __name__)
jwt = AuthDecorator()
validity_req = ErrorsRequestDecorator()


@controller_user_profile_system.route('/userprofilesystem', methods=['GET'])
@jwt.required_permission(PermissionEnum.VIEW.value)
def get_all():
    return  UserProfileSystem().get_all() 

@controller_user_profile_system.route('/userprofilesystem/params', methods=['GET'])
@jwt.required_permission(PermissionEnum.VIEW.value)
def get_by_params():
    return  UserProfileSystem().get_by_params() 

@controller_user_profile_system.route('/userprofilesystem', methods=['PUT'])
@jwt.required_permission(PermissionEnum.EDIT.value)
@validity_req.body_is_json
def update():
    return  UserProfileSystem().update()

@controller_user_profile_system.route('/userprofilesystem', methods=['POST'])
@jwt.required_permission(PermissionEnum.CRAFT.value)
@validity_req.body_is_json
def create():
    return  UserProfileSystem().create_witch_multiples_users()

@controller_user_profile_system.route('/userprofilesystem', methods=['DELETE'])
@jwt.required_permission(PermissionEnum.DEL.value)
@validity_req.body_is_json
def delete_by_id():
    return  UserProfileSystem().delete() 

