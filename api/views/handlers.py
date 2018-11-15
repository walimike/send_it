from api.views.views import appblueprint
from flask import jsonify

@appblueprint.errorhandler(400)
def bad_request(error):
    return jsonify({"msg": "Bad request"}), 400

@appblueprint.errorhandler(404)
def not_found(error):
    return jsonify({"Error": "Oooopss ID out of range"}), 404
