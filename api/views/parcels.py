from flask import jsonify, abort, request, json
from api.views.utilities import appblueprint, parcel_db, is_not_valid_order_key,\
is_not_valid_order, user_db
from api.models.models import Parcel
from flask_jwt_extended import jwt_required,get_jwt_identity
from flasgger import swag_from

@appblueprint.route('/parcels', methods=['POST'])
@jwt_required
#@swag_from('../docs/make_order.yml', methods = ['POST'])
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
    parcel_db.add_parcel(new_parcel)
    return jsonify({"message":"order added successfully"}),201

@appblueprint.route('/parcels', methods=['GET'])
@jwt_required
#@swag_from('../docs/fetch_all_orders.yml', methods = ['GET'])
def fetch_all_orders():
    role = get_jwt_identity()['role']
    if role != 'admin':
        return jsonify({"message":"you are not authorized to access this endpoint"}),401
    return jsonify({"Parcels":parcel_db.fetch_all_orders()}),200

@appblueprint.route('/parcels/<int:parcel_id>', methods=['GET'])
@jwt_required
#@swag_from('../docs/fetch_specific_order.yml', methods = ['GET'])
def fetch_specific_order(parcel_id):
    parcel = parcel_db.fetch_parcel(parcel_id)
    if not parcel:
        return jsonify({"message":"parcel not found"})
    return jsonify({"Parcel":parcel}),200

@appblueprint.route('/users/parcels', methods=['GET'])
@jwt_required
#@swag_from('../docs/fetch_parcel_by_specific_user.yml', methods = ['GET'])
def fetch_parcel_by_specific_user():
    user_id = get_jwt_identity()['user_id']
    return jsonify({"Parcel":parcel_db.fetch_parcel_by_specific(user_id)})

@appblueprint.route('/parcels/<int:parcel_id>/cancel', methods=['PUT'])
@jwt_required
#@swag_from('../docs/change_order_status.yml', methods = ['PUT'])
def change_order_status(parcel_id):
    user_role = get_jwt_identity()['role']
    if user_role == 'user':
        return jsonify({"message":"Unauthorized access"}),401
    new_status = request.json.get('status')

    if new_status != 'cancel':
        return jsonify({"message":"status can only be canceled"}),400
    if not parcel_db.fetch_parcel(parcel_id):
        return jsonify({"message":"order does not exist"}),404
    parcel_db.update_parcel(new_status,parcel_id)
    return jsonify({"message":"successfully updated"}),200

@appblueprint.route('/parcels/<int:parcel_id>/destination', methods=['PUT'])
@jwt_required
@swag_from('../docs/change_order_destination.yml', methods = ['PUT'])
def change_order_destination(parcel_id):
    destination = request.json['destination']
    user_id = get_jwt_identity()['user_id']
    parcel = parcel_db.fetch_parcel(parcel_id)

    if not parcel:
        return jsonify({"message":"parcel of this ID not found"}),404
    if parcel['usrid'] != user_id:
        return jsonify({"message":"you do not have authorization over this parcel"}),401
    parcel_db.update_parcel_destination(destination,parcel_id)
    return jsonify({"message":"destination successfully changed"}),200

@appblueprint.route('/parcels/<int:parcel_id>/presentlocation', methods=['PUT'])
@jwt_required
@swag_from('../docs/change_order_present_location.yml', methods = ['PUT'])
def change_order_present_location(parcel_id):
    location = request.json['present_location']
    role = get_jwt_identity()['role']
    if role != 'admin':
        return jsonify({"message":"Unauthorized access"}),401
    parcel_db.change_location(location,parcel_id)
    return jsonify({"message":"present location successfully changed"}),200

@appblueprint.route('/users', methods=['GET'])
def fetch_all_users():
    return jsonify({"users":user_db.fetch_all_users()})

@appblueprint.route('/test-endpoint', methods=['GET'])
def test_endpoint():
    return jsonify({"Parcels":parcel_db.fetch_all_orders()}),200
