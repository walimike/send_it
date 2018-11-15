from flask import Blueprint, jsonify, abort, request, json
from api.models.parcels import ParcelList
from api.models.models import Parcel
from api.models.validators import Validator


appblueprint = Blueprint('api',__name__)
my_parcels = ParcelList()
is_valid = Validator()


@appblueprint.route('/')
def welcomeMessage():
    return "<h1>Welcome to Send It.</h1>"

@appblueprint.route('/parcels')
def fetch_all_orders():
    return jsonify({"Parcel list": my_parcels.fetch_all_orders()})

@appblueprint.route('/parcels', methods=['POST'])
def make_order():
    """{"Owner":"","Source":"","Destination":"","Parcel name":""}"""
    if not request.json or not request.get_json()['Owner'] or not \
    request.get_json()['Source'] or not request.get_json()['Destination']\
    or not request.get_json()['Parcel name']:
        abort (400)

    owner,source,destination,parcel_name = request.get_json()['Owner'],\
    request.get_json()['Source'], request.get_json()['Destination'],\
    request.get_json()['Parcel name']

    if not is_valid.input_fields(owner,parcel_name,source,destination):
        return jsonify({"Error":"Ooops, one of the input fields is not in order"}), 400

    parcel_id = my_parcels.parcel_id_generator()
    new_parcel = Parcel(parcel_name,source,destination,parcel_id)
    my_parcels.add_parcel(owner,new_parcel)
    return jsonify({"ParcelList":my_parcels.parcel_list}), 201

@appblueprint.route('/users')
def fetch_all_users():
    return jsonify({"Userlist":my_parcels.fetch_all_users()})

@appblueprint.route('/parcels/<int:parcel_id>')
def fetch_specific_order(parcel_id):
    if not my_parcels.fetch_specific_order(parcel_id):
        abort(404)
    return jsonify({"Userlist":my_parcels.fetch_specific_order(parcel_id)})

@appblueprint.route('/users/<int:user_id>/parcels')
def fetch_all_orders_by_specific_user(user_id):
    orders = my_parcels.fetch_all_orders_by_specific_user(user_id)
    if not orders:
        abort(404)
    return jsonify({"Orders":orders})

@appblueprint.route('/parcels/<int:parcel_id>/cancel', methods=['PUT'])
def cancel_specific_order(parcel_id):
    if not my_parcels.fetch_specific_order(parcel_id):
        abort(404)    
    new_status = request.get_json()['status']
    if not is_valid.status_update(new_status):
        return jsonify({"Error":"Status can only be canceled ie. 'status':'cancel'"}),400
    return jsonify({'Parcel List':my_parcels.cancel_order(parcel_id)})
