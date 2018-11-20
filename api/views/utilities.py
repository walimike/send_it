from api.models.parcels import ParcelDb
from api.models.models import User
from api.models.users import UserDb
from flask import Blueprint,jsonify


appblueprint = Blueprint('api',__name__)

parcel_db = ParcelDb()
user_db = UserDb()
