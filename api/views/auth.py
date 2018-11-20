from api.views.utilities import parcel_db, user_db, is_not_valid_login_json,is_not_valid_signup_json
from flask import Blueprint, jsonify, abort, request, json
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token,
    get_jwt_identity)
from api.views.utilities import appblueprint
from api.models.models import User


@appblueprint.route('/auth/signup', methods=['POST'])
def add_user():
    """{"Name":"","Email":"","Password":"","Role":""}"""
    user_input = request.json
    if is_not_valid_signup_json(user_input):
        return is_not_valid_signup_json(user_input),400

    name = request.json.get('Name', None)
    email = request.json.get('Email', None)
    password = request.json.get('Password', None)
    role = request.json.get('Role', None)

    new_user = User(name,email,password,role)
    user_db.add_user(new_user)
    return jsonify({"User credentials":user_db.fetch_user(new_user)}),201

@appblueprint.route('/auth/login', methods=['POST'])
def login():
    """{"Name":"","Password":""}"""
    user_input = request.json
    if is_not_valid_login_json(user_input):
        return is_not_valid_login_json(user_input),400

    password = request.json.get('Password', None)
    username = request.json.get('Name', None)

    if not username:
        return jsonify({"message": "Missing username parameter"}), 400
    if not password:
        return jsonify({"message": "Missing password parameter"}), 400

    new_user = User(username,' ',password, ' ')
    current_user = user_db.fetch_user(new_user)
    user = {"user_id":current_user["usrid"],"role":current_user["role"]}

    access_token = create_access_token(identity=user)
    return jsonify({"access token":access_token}), 200
