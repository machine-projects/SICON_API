from flask import jsonify
from src.infra.model.resultModel import ResultModel


def config_decorators_jwt(jwt):
        
    @jwt.expired_token_loader
    def expired_token_callback():
        return ResultModel('Token invalido', False, [
            dict(name='token', message='O token já está expirado.')
            ]).to_dict(), 401
        
    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return ResultModel("Token invalido",False, [
                dict(name='token', message='Falha na verificação do token.')
                ]).to_dict(), 401

        
    @jwt.unauthorized_loader
    def unauthorized_loader_callback(error):
        return ResultModel('Token invalido', False, [
            dict(name='token', message='O token de acesso não foi encontrado.')
            ]).to_dict(), 401

    @jwt.needs_fresh_token_loader
    def fresh_token_loader_callback():
        return ResultModel('Token invalido', False, [
            dict(name='token', message='O token não é novo. É necessário um token novo!')
            ]).to_dict(), 401

    return jwt



