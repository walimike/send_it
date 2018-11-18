from flask import Blueprint, jsonify, abort, request, json
from api.models.parcels import ParcelDb
from api.models.models import User
from api.models.users import UserDb
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity)


appblueprint = Blueprint('api',__name__)
parcel_db = ParcelDb()
user_db = UserDb()
user_db.create_tables()


@appblueprint.route('/auth/signup', methods=['POST'])
def add_user():
    """{"Name":"","Email":"","Password":"","Role":""}"""
    if not request.json or not request.json.get('Name') or not \
    request.json.get('Email') or not request.json.get('Password')\
    or not request.json.get('Role'):
        abort(400)

    name,email,password,role = request.json.get('Name', None),\
    request.json.get('Email', None), request.json.get('Password', None),\
    request.json.get('Role', None)

    new_user = User(name,email,password,role)
    user_db.add_user(new_user)
    return jsonify({"User credentials":user_db.fetch_user(new_user)}),201


@appblueprint.route('/auth/login', methods=['POST'])
def login():
    """{"Name":"","Password":""}"""
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400
    password = request.json.get('Password', None)
    username = request.json.get('Name', None)
    if not username:
        return jsonify({"msg": "Missing username parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400

    new_user = User(username,' ',password, ' ')
    current_user = user_db.fetch_user(new_user)
    
    access_token = create_access_token(identity=current_user["usrid"])
    return jsonify({"Message":"Successfully loged in"}), 200
