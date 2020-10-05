from flask import Blueprint
from src.handler.auth.login import AuthHandler
from src.handler.auth.tokenHandler import TokenHandler
from src.infra.decorator.request.errorsRequestDecorator import ErrorsRequestDecorator
from flask_jwt_extended import  jwt_required

controller_auth = Blueprint('controller_auth', __name__)
validity_req = ErrorsRequestDecorator()

@controller_auth.route('/login', methods=['POST'])
@validity_req.body_is_json
def login():
    auth = AuthHandler()
    return auth.post()

@controller_auth.route('/isvalidtoken', methods=['POST'])
@jwt_required
def isvalidtoken():
    return TokenHandler().validation_token()

