from api.models.models import User
from api.models.db_controller import Dbcontroller
from flask import Blueprint,jsonify
from api.models.validators import Validator

appblueprint = Blueprint('api',__name__)


db_conn = Dbcontroller()
is_valid = Validator()


"""These functions below validate the json input data and return user friendly responses"""

def is_not_valid_signup_key_word(json_input):
    if is_not_valid_login_key_word(json_input):
        return is_not_valid_login_key_word(json_input)
    if not json_input.get('email'):
        return jsonify({"message":"email key word is not in the right format"})

def is_not_valid_login_key_word(json_input):
    if not json_input:
        return jsonify({"message":"request must be in json format"})
    if not json_input.get('name'):
        return jsonify({"message":"name key word is not in the right format"})
    if not json_input.get('password'):
        return jsonify({"message":"password key word is not in the right format"})

def is_not_valid_order_key(json_input):
    if not json_input:
        return jsonify({"message":"request must be in json format"})
    if not json_input.get('parcel_name'):
        return jsonify({"message":"parcel_name key word is not in the right format"})
    if not json_input.get('source'):
        return jsonify({"message":"source key word is not in the right format"})
    if not json_input.get('destination'):
        return jsonify({"message":"destination key word is not in the right format"})
    if not json_input.get('price'):
        return jsonify({"message":"price key word is not in the right format"})

def is_not_valid_order(order_dict):
    if not is_valid.pure_text(order_dict.get('parcel_name')):
        return jsonify({"message":"an error occured in Parcel_name input"})
    if not is_valid.normal_string(order_dict.get('source')):
        return jsonify({"message":"an error occured in source input"})
    if not is_valid.normal_string(order_dict.get('destination')):
        return jsonify({"message":"an error occured in destination input"})
    if not is_valid.integer(order_dict.get('price')):
        return jsonify({"message":"an error occured in price input"})

def is_not_valid_user_details(user_dict):
    if is_not_valid_user_login_details(user_dict):
        return is_not_valid_user_login_details(user_dict)
    if not is_valid.email(user_dict.get('email')):
        return jsonify({"message":"email not in the right format"})

def is_not_valid_user_login_details(user_dict):
    if not is_valid.password(user_dict.get('password')):
        return jsonify({"message":"an error occured in password input"})
    if not is_valid.pure_text(user_dict.get('name')):
        return jsonify({"message":"an error occured in name input"})
