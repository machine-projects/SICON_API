from flask import Blueprint, jsonify, request
from flask_jwt_extended import  jwt_required
from flask import current_app, request
from src.infra.decorator.auth.authDecorator import AuthDecorator
from src.handler.address.addressHandler import AddressHandler
from src.infra.decorator.request.errorsRequestDecorator import ErrorsRequestDecorator
from src.model.enum.permission import PermissionEnum

controller_address = Blueprint('controller_address', __name__)
jwt = AuthDecorator()
validity_req = ErrorsRequestDecorator()


@controller_address.route('/address', methods=['GET'])
@jwt.required_permission(PermissionEnum.VIEW.value)
def get_all():
    return  AddressHandler().get_all_address() 

@controller_address.route('/address/id/<_id>', methods=['GET'])
@jwt.required_permission(PermissionEnum.VIEW.value)
def get_by_id(_id):
    playload = dict(id=_id)
    return  AddressHandler().get_by_id(playload) 

@controller_address.route('/address/personid/<_id>', methods=['GET'])
@jwt.required_permission(PermissionEnum.VIEW.value)
def get_by_person_id(_id):
    playload = dict(id=_id)
    return  AddressHandler().get_by_person_id(playload) 

@controller_address.route('/address', methods=['PUT'])
@jwt.required_permission(PermissionEnum.EDIT.value)
@validity_req.body_is_json
def update():
    return  AddressHandler().update_address()

@controller_address.route('/address', methods=['POST'])
@jwt.required_permission(PermissionEnum.CRAFT.value)
@validity_req.body_is_json
def create():
    return  AddressHandler().create_address()

@controller_address.route('/address', methods=['DELETE'])
@jwt.required_permission(PermissionEnum.DEL.value)
@validity_req.body_is_json
def delete_by_id():
    return  AddressHandler().delete_address() 


