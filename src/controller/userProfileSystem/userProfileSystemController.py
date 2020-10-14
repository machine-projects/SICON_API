from flask import Blueprint, jsonify, request
from flask_jwt_extended import  jwt_required
from flask import current_app, request
from src.infra.decorator.auth.authDecorator import AuthDecorator
from src.handler.userProfileSystem.userProfileSystemHandler import UserProfileSystemHandler as UserProfileSystem
from src.infra.decorator.request.errorsRequestDecorator import ErrorsRequestDecorator


controller_user_profile_system = Blueprint('controller_user_profile_system', __name__)
jwt = AuthDecorator()
validity_req = ErrorsRequestDecorator()


@controller_user_profile_system.route('/userprofilesystem', methods=['GET'])
@jwt_required
def get_all():
    return  UserProfileSystem().get_all() 

@controller_user_profile_system.route('/userprofilesystem/params', methods=['GET'])
@jwt_required
def get_by_params():
    return  UserProfileSystem().get_by_params() 

@controller_user_profile_system.route('/userprofilesystem', methods=['PUT'])
@validity_req.body_is_json
@jwt_required
def update():
    return  UserProfileSystem().update()

@controller_user_profile_system.route('/userprofilesystem', methods=['POST'])
@jwt_required
@validity_req.body_is_json
def create():
    return  UserProfileSystem().create()

@controller_user_profile_system.route('/userprofilesystem', methods=['DELETE'])
@jwt_required
@validity_req.body_is_json
def delete_by_id():
    return  UserProfileSystem().delete() 


