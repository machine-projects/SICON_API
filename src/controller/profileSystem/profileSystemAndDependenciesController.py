from flask import Blueprint, jsonify, request
from flask_jwt_extended import  jwt_required
from flask import current_app, request
from src.infra.decorator.auth.authDecorator import AuthDecorator
from src.handler.profileSystemAndDependencies.profileSystemAndDependenciesHandler import ProfileSystemAndDependenciesHandler as ProfileSystemAndDependencies
from src.infra.decorator.request.errorsRequestDecorator import ErrorsRequestDecorator
from src.model.enum.permission import PermissionEnum

controller_profile_system_and_dependencies = Blueprint('controller_profile_system_and_dependencies', __name__)
jwt = AuthDecorator()
validity_req = ErrorsRequestDecorator()


@controller_profile_system_and_dependencies.route('/profilesystemanddependencies/<_id>', methods=['GET'])
@jwt.required_permission(PermissionEnum.VIEW.value)
def get_by_params(_id):
    return  ProfileSystemAndDependencies().get_by_id(_id) 

@controller_profile_system_and_dependencies.route('/profilesystemanddependencies', methods=['POST'])
@jwt.required_permission(PermissionEnum.CRAFT.value)
@validity_req.body_is_json
def create():
    return  ProfileSystemAndDependencies().create()
