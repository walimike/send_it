from flask import jsonify, abort, request, json
from api.views.utilities import appblueprint, parcel_db, is_not_valid_order_json
from api.models.models import Parcel
from flask_jwt_extended import jwt_required,get_jwt_identity
from api.views.utilities import appblueprint


@appblueprint.route('/parcels', methods=['POST'])
@jwt_required
def make_order():
    """{"Source":"","Destination":"","Parcel name":"","Present Location":"","Price":""}"""
    """user_identity in form of a dict {""}"""
    user_identiy = get_jwt_identity()

    order_request = request.json
    if is_not_valid_order_json(order_request):
        return is_not_valid_order_json(order_request)

    parcel_name = request.json.get('Parcel Name')
    source = request.json.get('Source')
    destination = request.json.get('Destination')
    present_location = request.json.get('Present Location')
    price = request.json.get('Price')

    new_parcel = Parcel(parcel_name,price,user_identiy['user_id'],source,destination)
    parcel_db.add_parcel(new_parcel)
    return jsonify({"Parcels":parcel_db.fetch_all_orders()}), 201

@appblueprint.route('/parcels', methods=['GET'])
@jwt_required
def fetch_all_orders():
    return jsonify({"Parcels":parcel_db.fetch_all_orders()}),200


@appblueprint.route('/parcels/<int:parcel_id>', methods=['GET'])
@jwt_required
def fetch_specific_order(parcel_id):
    return jsonify({"Parcel":parcel_db.fetch_parcel(parcel_id)})

@appblueprint.route('/users/parcels', methods=['GET'])
@jwt_required
def fetch_parcel_by_specific_user():
    user_id = get_jwt_identity()['user_id']
    return jsonify({"Parcel":parcel_db.fetch_parcel_by_specific_user(user_id)})
