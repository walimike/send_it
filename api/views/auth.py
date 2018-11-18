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
    if not request.json or not request.get_json()['Name'] or not \
    request.get_json()['Email'] or not request.get_json()['Password']\
    or not request.get_json()['Role']:
        return jsonify({"msg": "Bad request"}), 400

    name,email,password,role = request.get_json()['Name'],\
    request.get_json()['Email'], request.get_json()['Password'],\
    request.get_json()['Role']

    new_user = User(name,email,password,role)
    user_db.add_user(new_user)
    return jsonify({"User credentials":user_db.fetch_user(new_user)}),200
