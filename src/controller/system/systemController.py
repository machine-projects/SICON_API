from flask import Blueprint, jsonify, request, current_app
from flask_jwt_extended import  jwt_required
from src.infra.decorator.auth.authDecorator import AuthDecorator
from src.infra.decorator.request.errorsRequestDecorator import ErrorsRequestDecorator


controller_system = Blueprint('controller_system', __name__)
jwt = AuthDecorator()
validity_req = ErrorsRequestDecorator()



@controller_system.route('/system', methods=['GET'])
@jwt_required
def get_all():
    param1 = request.args.get('param1')
    param2 = request.args.get('param2')
    return jsonify([param1, param2])
