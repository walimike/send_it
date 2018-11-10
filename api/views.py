from flask import Blueprint, jsonify, abort, request, make_response, json
from api.models.parcels import ParcelList

my_parcels = ParcelList()
appblueprint = Blueprint('api',__name__)

@appblueprint.route('/')
def welcomeMessage():
    return "<h1>Welcome to Send It.</h1>"

@appblueprint.route('/parcels')
def fetch_all_orders():
    return jsonify({"Parcel list": my_parcels.parcel_list})
