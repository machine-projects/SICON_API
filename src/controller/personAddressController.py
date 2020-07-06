from flask import Blueprint, jsonify, request
from flask_jwt_extended import  jwt_required
from flask import current_app, request
from src.infra.decorator.auth.authDecorator import AuthDecorator
from src.infra.decorator.request.errorsRequestDecorator import ErrorsRequestDecorator
from src.handler.personAddress.personAddressHandler import *

controller_person_address = Blueprint('controller_person_address', __name__)
jwt = AuthDecorator()
validity_req = ErrorsRequestDecorator()



@controller_person_address.route('/personaddress/all', methods=['POST'])
# @jwt_required
def get_all():
    return  PersonAddressHandler().get_all_persons_address()

@controller_person_address.route('/personaddress/id', methods=['POST'])
# @jwt_required
def get_by_id():
    return  PersonAddressHandler().get_by_person_id()

@controller_person_address.route('/personaddress/person/address', methods=['POST'])
# @jwt_required
def get_by_person_id_address_id():
    return  PersonAddressHandler().get_by_person_id_address_id()

@controller_person_address.route('/personaddress', methods=['PUT'])
@validity_req.body_is_json
# @jwt_required
def update():
    return  PersonAddressHandler().update_person_address()

@controller_person_address.route('/personaddress', methods=['POST'])
# @jwt_required
@validity_req.body_is_json
def create():
    return  PersonAddressHandler().create_person_address()

@controller_person_address.route('/personaddress', methods=['DELETE'])
# @jwt_required
@validity_req.body_is_json
def delete_by_id():
    return  PersonAddressHandler().delete_person_address()


