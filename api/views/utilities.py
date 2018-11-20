from api.models.parcels import ParcelDb
from api.models.models import User
from api.models.users import UserDb
from flask import Blueprint,jsonify


appblueprint = Blueprint('api',__name__)

parcel_db = ParcelDb()
user_db = UserDb()

"""These functions below validate the json input data and return user friendly responses"""

def is_not_valid_signup_json(json_input):
    if is_not_valid_login_json(json_input):
        return is_not_valid_login_json(json_input)
    if not json_input.get('Email'):
        return jsonify({"message":"Email key word is not in the right format"})
    if not json_input.get('Role'):
        return jsonify({"message":"Role key word is not in the right format"})

def is_not_valid_login_json(json_input):
    if not json_input:
        return jsonify({"message":"request must be in json format"})
    if not json_input.get('Name'):
        return jsonify({"message":"Name key word is not in the right format"})
    if not json_input.get('Password'):
        return jsonify({"message":"Password key word is not in the right format"})

def is_not_valid_order_json(json_input):
    if not json_input:
        return jsonify({"message":"request must be in json format"})
    if not json_input.get('Parcel Name'):
        return jsonify({"message":"Parcel Name key word is not in the right format"})
    if not json_input.get('Source'):
        return jsonify({"message":"Source key word is not in the right format"})
    if not json_input.get('Destination'):
        return jsonify({"message":"Destination key word is not in the right format"})
    if not json_input.get('Present Location'):
        return jsonify({"message":"Present Location key word is not in the right format"})
    if not json_input.get('Price'):
        return jsonify({"message":"Price key word is not in the right format"})
