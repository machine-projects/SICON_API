from flask import Blueprint, jsonify, request
from src.handler.user.userHandler import UserHandler
from flask_jwt_extended import  jwt_required
from flask import current_app, request
from src.infra.decorator.auth.authDecorator import AuthDecorator
from src.infra.decorator.request.errorsRequestDecorator import ErrorsRequestDecorator
from src.model.enum.permission import PermissionEnum


controller_user = Blueprint('controller_user', __name__)
jwt = AuthDecorator()
validity_req = ErrorsRequestDecorator()



@controller_user.route('/users', methods=['GET'])
@jwt.required_permission(PermissionEnum.VIEW.value)
def get_all():
    user = UserHandler()
    return user.get_all_users()

@controller_user.route('/user/username/<username>', methods=['GET'])
@jwt.required_permission(PermissionEnum.VIEW.value)
def get_by_username(username):
    user = UserHandler()
    return user.get_by_username(username)

@controller_user.route('/user/id/<_id>', methods=['GET'])
@jwt.required_permission(PermissionEnum.VIEW.value)
def get_by_id(_id):
    user = UserHandler()
    return user.get_by_id(_id)

@controller_user.route('/user', methods=['POST'])
@jwt.required_permission(PermissionEnum.CRAFT.value)
@validity_req.body_is_json
def post():
    user = UserHandler()
    return user.create_user()

@controller_user.route('/user', methods=['PUT'])
@jwt.required_permission(PermissionEnum.EDIT.value)
@validity_req.body_is_json
def put():
    user = UserHandler()
    return user.update_user()

@controller_user.route('/user', methods=['DELETE'])
@jwt.required_permission(PermissionEnum.DEL.value)
@validity_req.body_is_json
def delete():
    user = UserHandler()
    return user.delete_user()
