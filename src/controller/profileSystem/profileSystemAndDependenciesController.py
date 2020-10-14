from flask import Blueprint, jsonify, request
from flask_jwt_extended import  jwt_required
from flask import current_app, request
from src.infra.decorator.auth.authDecorator import AuthDecorator
from src.handler.profileSystemAndDependencies.profileSystemAndDependenciesHandler import ProfileSystemAndDependenciesHandler as ProfileSystemAndDependencies
from src.infra.decorator.request.errorsRequestDecorator import ErrorsRequestDecorator


controller_profile_system_and_dependencies = Blueprint('controller_profile_system_and_dependencies', __name__)
jwt = AuthDecorator()
validity_req = ErrorsRequestDecorator()


@controller_profile_system_and_dependencies.route('/profilesystemanddependencies/id/<_id>', methods=['GET'])
@jwt_required
def get_by_id(_id):
    return  ProfileSystemAndDependencies().get_by_id(_id) 

@controller_profile_system_and_dependencies.route('/profilesystemanddependencies', methods=['POST'])
@jwt_required
@validity_req.body_is_json
def create():
    return  ProfileSystemAndDependencies().create()