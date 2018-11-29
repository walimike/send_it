from flask import jsonify, abort, request, json
from api.views import appblueprint, is_not_valid_order_key,\
is_not_valid_order, db_conn
from api.models.models import Parcel
from flask_jwt_extended import jwt_required,get_jwt_identity


@appblueprint.route('/parcels', methods=['POST'])
@jwt_required
def make_order():

    user_identiy = get_jwt_identity()
    order_request = request.json
    if is_not_valid_order_key(order_request):
        return is_not_valid_order_key(order_request),400

    if is_not_valid_order(order_request):
        return is_not_valid_order(order_request),400

    parcel_name = request.json.get('parcel_name')
    source = request.json.get('source')
    destination = request.json.get('destination')
    price = request.json.get('price')

    new_parcel = Parcel(parcel_name,price,user_identiy['user_id'],source,destination)
    db_conn.add_parcel(new_parcel)
    return jsonify({"message":"order added successfully"}),201

@appblueprint.route('/parcels', methods=['GET'])
@jwt_required
def fetch_all_orders():
    role = get_jwt_identity()['role']
    if role != 'admin':
        return jsonify({"message":"you are not authorized to access this endpoint"}),401
    return jsonify({"Parcels":db_conn.fetch_all_orders()}),200

@appblueprint.route('/parcels/<int:parcel_id>', methods=['GET'])
@jwt_required
def fetch_specific_order(parcel_id):
    parcel = db_conn.fetch_parcel('parcelid',parcel_id)
    if not parcel:
        return jsonify({"message":"parcel not found"}),404
    return jsonify({"Parcel":parcel}),200

@appblueprint.route('/users/parcels', methods=['GET'])
@jwt_required
def fetch_parcel_by_specific_user():
    user_id = get_jwt_identity()['user_id']
    return jsonify({"Parcel":db_conn.fetch_parcel('usrid',user_id)})

@appblueprint.route('/parcels/<int:parcel_id>/cancel', methods=['PUT'])
@jwt_required
def change_order_status(parcel_id):
    user_role = get_jwt_identity()['role']
    if user_role == 'user':
        return jsonify({"message":"Unauthorized access"}),401
    new_status = request.json.get('status')

    if new_status != 'cancel':
        return jsonify({"message":"status can only be canceled"}),400
    if not db_conn.fetch_parcel('parcelid',parcel_id):
        return jsonify({"message":"order does not exist"}),404
    db_conn.update_parcel('parcel_status',new_status,parcel_id)
    return jsonify({"message":"successfully updated"}),200

@appblueprint.route('/parcels/<int:parcel_id>/destination', methods=['PUT'])
@jwt_required
def change_order_destination(parcel_id):
    destination = request.json['destination']
    user_id = get_jwt_identity()['user_id']
    parcel = db_conn.fetch_parcel('parcelid',parcel_id)

    if not parcel:
        return jsonify({"message":"parcel of this ID not found"}),404
    if parcel[0]['usrid'] != user_id:
        return jsonify({"message":"you do not have authorization over this parcel"}),401
    db_conn.update_parcel('parcel_destination',destination,parcel_id)
    return jsonify({"message":"destination successfully changed"}),200

@appblueprint.route('/parcels/<int:parcel_id>/presentlocation', methods=['PUT'])
@jwt_required
def change_order_present_location(parcel_id):
    location = request.json['present_location']
    role = get_jwt_identity()['role']
    if role != 'admin':
        return jsonify({"message":"Unauthorized access"}),401
    db_conn.update_parcel('present_location',location,parcel_id)
    return jsonify({"message":"present location successfully changed"}),200

@appblueprint.route('/users', methods=['GET'])
def fetch_all_users():
    return jsonify({"users":db_conn.fetch_all_users()})
