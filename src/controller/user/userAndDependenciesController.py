from flask import Blueprint, jsonify, request
from src.handler.userAndDependencies.userAndDependenciesHandler import UserAndDependenciesHandler
from flask_jwt_extended import  jwt_required
from flask import current_app, request
from src.infra.decorator.auth.authDecorator import AuthDecorator
from src.infra.decorator.request.errorsRequestDecorator import ErrorsRequestDecorator
from src.model.enum.permission import PermissionEnum


controller_user_and_dependencies = Blueprint('controller_user_and_dependencies', __name__)
jwt = AuthDecorator()
validity_req = ErrorsRequestDecorator()


@controller_user_and_dependencies.route('/completeuser', methods=['POST'])
# @jwt.admin_required
@jwt.required_permission(PermissionEnum.CRAFT.value)
@validity_req.body_is_json
def post():
    user_and_dependencies = UserAndDependenciesHandler()
    return user_and_dependencies.create_user_person_address()

@controller_user_and_dependencies.route('/completeuser', methods=['GET'])
@jwt.required_permission(PermissionEnum.VIEW.value)
def get():
    user_and_dependencies = UserAndDependenciesHandler()
    return user_and_dependencies.get_user_person_address()


## REMOVER ROTA DEPOIS QUE CRIAR ADMIN PARA CESSO DO SISTEMA
@controller_user_and_dependencies.route('/completeuser/firstadmin', methods=['POST'])
@validity_req.body_is_json
def post_first_user():
    user_and_dependencies = UserAndDependenciesHandler()
    return user_and_dependencies.create_user_person_address(True)
