from flask_restful import  marshal
from src.model.schemas.users import users_fields
from src import db, request
from flask_jwt_extended import create_access_token
from flask import current_app
from flask_bcrypt import Bcrypt
import datetime
from src.infra.model.resultModel import ResultModel
from src.repository.user.userRepository import UserRepository
from src.contract.auth.loginCotract import LoginContract
from src.infra.handler.pagination import Paginate


class AuthHandler:
    
    def post(self):
        contract = LoginContract()
        playload = request.json
        if not(contract.validate(playload)):
            return ResultModel('Envie todos parametros obrigatorios.', False, contract.errors).to_dict(), 406
        password = playload.get('password')
        bcrypt = Bcrypt(current_app)
        crypt_password =  bcrypt.generate_password_hash(password).decode('utf-8')
        repository = UserRepository()
        user_result = repository.get_by_username(playload.get('username'), True)
        if user_result['error']:
            return user_result
        user = repository.get_by_username(playload.get('username'), True)['data']['result']
        if not user:
            ResultModel('Usuario não existe.', False, True)
        if not user or not bcrypt.check_password_hash(user['password'], password):
            return ResultModel('Credenciais incorretas.', False, True).to_dict(), 406
        data = {
            'userId': user['id'],
            'is_admin': user['is_admin']
        }
        expires = datetime.timedelta(days=current_app.config.get('TOKEN_DAYS_EXPIRES'))
        token = create_access_token(identity=user['id'], expires_delta=expires, user_claims=data)
        return ResultModel('Sucesso na geração do token.', token, False).to_dict(), 201
