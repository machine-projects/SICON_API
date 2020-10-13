from flask import Blueprint, jsonify, request
from flask_jwt_extended import  jwt_required
from flask import current_app, request
from src.infra.decorator.auth.authDecorator import AuthDecorator
from src.handler.profileSystem.profileSystemHandler import ProfileSystemHandler as ProfileSystem
from src.infra.decorator.request.errorsRequestDecorator import ErrorsRequestDecorator


controller_profile_permission = Blueprint('controller_profile_permission', __name__)
jwt = AuthDecorator()
validity_req = ErrorsRequestDecorator()


@controller_profile_permission.route('/profilepermission', methods=['GET'])
@jwt_required
def get_all():
    return  ProfileSystem().get_all() 

@controller_profile_permission.route('/profilepermission/params', methods=['GET'])
@jwt_required
def get_by_params():
    return  ProfileSystem().get_by_params() 

@controller_profile_permission.route('/profilepermission', methods=['PUT'])
@validity_req.body_is_json
@jwt_required
def update():
    return  ProfileSystem().update()

@controller_profile_permission.route('/profilepermission', methods=['POST'])
@jwt_required
@validity_req.body_is_json
def create():
    return  ProfileSystem().create()

@controller_profile_permission.route('/profilepermission', methods=['DELETE'])
@jwt_required
@validity_req.body_is_json
def delete_by_id():
    return  ProfileSystem().delete() 


