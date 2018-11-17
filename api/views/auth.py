from flask import Blueprint, jsonify, abort, request, json
from instance import AppSettings


appblueprint = Blueprint('api',__name__)
app_settings = AppSettings('development')
user_db = app_settings.create_user_database()
