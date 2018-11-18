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
