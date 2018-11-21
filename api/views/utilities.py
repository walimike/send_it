from api.models.parcels import ParcelDb
from api.models.models import User
from api.models.users import UserDb
from flask import Blueprint,jsonify
from api.models.validators import Validator

appblueprint = Blueprint('api',__name__)

parcel_db = ParcelDb()
user_db = UserDb()
is_valid = Validator()

"""These functions below validate the json input data and return user friendly responses"""

def is_not_valid_signup_key_word(json_input):
    if is_not_valid_login_key_word(json_input):
        return is_not_valid_login_key_word(json_input)
    if not json_input.get('Email'):
        return jsonify({"message":"Email key word is not in the right format"})
    if not json_input.get('Role'):
        return jsonify({"message":"Role key word is not in the right format"})

def is_not_valid_login_key_word(json_input):
    if not json_input:
        return jsonify({"message":"request must be in json format"})
    if not json_input.get('Name'):
        return jsonify({"message":"Name key word is not in the right format"})
    if not json_input.get('Password'):
        return jsonify({"message":"Password key word is not in the right format"})

def is_not_valid_order_key(json_input):
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

def is_not_valid_order(order_dict):
    if not is_valid.pure_text(order_dict.get('Parcel Name')):
        return jsonify({"message":"an error occured in Parcel Name input"})
    if not is_valid.normal_string(order_dict.get('Source')):
        return jsonify({"message":"an error occured in Source input"})
    if not is_valid.normal_string(order_dict.get('Destination')):
        return jsonify({"message":"an error occured in Destination input"})
    if not is_valid.normal_string(order_dict.get('Present Location')):
        return jsonify({"message":"an error occured in Precent Location input"})
    if not is_valid.integer(order_dict.get('Price')):
        return jsonify({"message":"an error occured in Price input"})

def is_not_valid_user_details(user_dict):
    if not is_valid.pure_text(user_dict.get('Name')):
        return jsonify({"message":"an error occured in Name input"})
    if not is_valid.email(user_dict.get('Email')):
        return jsonify({"message":"email not in the right format"})
    if not is_valid.password(user_dict.get('Password')):
        return jsonify({"message":"an error occured in Password input"})
    #if user_dict.get('Role').lower() != 'admin' or user_dict.get('Role').lower() != 'user':
        #return jsonify({"message":"role can either be user or admin only"})

def is_not_valid_user_login_details(user_dict):
    if not is_valid.password(user_dict.get('Password')):
        return jsonify({"message":"an error occured in Password input"})
    if not is_valid.pure_text(user_dict.get('Name')):
        return jsonify({"message":"an error occured in Name input"})
