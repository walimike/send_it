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
    #if is_not_valid_order_json(order_request):
    #    return is_not_valid_order_json(order_request)

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
    role = get_jwt_identity()['role']
    if role.lower() != admin:
        return jsonify({"message":"you are not authorized to access this endpoint"}),401
    return jsonify({"Parcels":parcel_db.fetch_all_orders()}),200


@appblueprint.route('/parcels/<int:parcel_id>', methods=['GET'])
@jwt_required
def fetch_specific_order(parcel_id):
    return jsonify({"Parcel":parcel_db.fetch_parcel(parcel_id)})

@appblueprint.route('/users/parcels', methods=['GET'])
# has an error for user_id
@jwt_required
def fetch_parcel_by_specific_user():
    user_id = get_jwt_identity()['user_id']
    return jsonify({"Parcel":parcel_db.fetch_parcel_by_specific_user(user_id)})

@appblueprint.route('/parcels/<int:parcel_id>/status', methods=['PUT'])
@jwt_required
def change_order_status(parcel_id):
    user_role = get_jwt_identity()['role']
    if user_role.lower() != 'admin':
        return jsonify({"message":"Unauthorized access"}),401
    new_status = request.json.get('Status')
    if not parcel_db.fetch_parcel(parcel_id):
        return jsonify({"message":"order does not exist"})
    parcel_db.update_parcel(new_status,parcel_id)
    return jsonify({"message":"successfully updated"}),200

@appblueprint.route('/parcels/<int:parcel_id>/destination', methods=['PUT'])
@jwt_required
def change_order_destination(parcel_id):
    destination = request.json['Destination']
    user_id = get_jwt_identity()['user_id']
    parcel = parcel_db.fetch_specific_order(parcel_id)
    if parcel['usrid'] != user_id:
        return jsonify({"message":"you are not the owner of this parcel"}),400
    parcel_db.update_parcel_destination(destination,parcel_id)
    return jsonify({"message":"destination successfully changed"}),200

@appblueprint.route(' /parcels/<int:parcel_id>/presentLocation', methods=['PUT'])
@jwt_required
def change_order_present_location(parcel_id):
    location = request.json['Present Location']
    role = get_jwt_identity()['role']
    if user_role.lower() != 'admin':
        return jsonify({"message":"Unauthorized access"}),401
    parcel_db.change_location(location,parcel_id)
    return jsonify({"message":"present location successfully changed"}),200
