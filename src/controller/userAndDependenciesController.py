from flask import Blueprint, jsonify, request
from src.handler.userAndDependencies.userAndDependenciesHandler import UserAndDependenciesHandler
from flask_jwt_extended import  jwt_required
from flask import current_app, request
from src.infra.decorator.auth.authDecorator import AuthDecorator
from src.infra.decorator.request.errorsRequestDecorator import ErrorsRequestDecorator


controller_user_and_dependencies = Blueprint('controller_user_and_dependencies', __name__)
jwt = AuthDecorator()
validity_req = ErrorsRequestDecorator()



# @controller_user_and_dependencies.route('/users', methods=['GET'])
# # @jwt_required
# def get_all():
#     user = UserHandler()
#     return user.get_all_users()

# @controller_user_and_dependencies.route('/user/username/<username>', methods=['GET'])
# # @jwt_required
# def get_by_username(username):
#     user = UserHandler()
#     return user.get_by_username(username)

# @controller_user_and_dependencies.route('/user/id/<_id>', methods=['GET'])
# # @jwt_required
# def get_by_id(_id):
#     user = UserHandler()
#     return user.get_by_id(_id)

@controller_user_and_dependencies.route('/completeuser', methods=['POST'])
@jwt.admin_required
@validity_req.body_is_json
def post():
    user_and_dependencies = UserAndDependenciesHandler()
    return user_and_dependencies.create_user_person_address()

# @controller_user_and_dependencies.route('/user', methods=['PUT'])
# @jwt.admin_required
# @validity_req.body_is_json
# def put():
#     user = UserHandler()
#     return user.update_user()

# @controller_user_and_dependencies.route('/user', methods=['DELETE'])
# @jwt.admin_required
# @validity_req.body_is_json
# def delete():
#     user = UserHandler()
#     return user.delete_user()
