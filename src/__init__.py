from flask_restful import Api
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_jwt_extended import  JWTManager
from src.infra.decorator.request.defaultReturnJwt import config_decorators_jwt

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    api = Api(app)
    db.init_app(app)
    jwt = JWTManager(app)
    config_decorators_jwt(jwt)
   
    

    # imports
    from src.controller.indexController import controller_index
    app.register_blueprint(controller_index)
    from src.controller.userController import controller_user
    app.register_blueprint(controller_user)
    from src.controller.authController import controller_auth
    app.register_blueprint(controller_auth)
    from src.controller.personController import controller_person
    app.register_blueprint(controller_person)
    from src.controller.addressController import controller_address
    app.register_blueprint(controller_address)
    from src.controller.userAndDependenciesController import controller_user_and_dependencies
    app.register_blueprint(controller_user_and_dependencies)

    return app
