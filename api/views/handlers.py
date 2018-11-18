from flask import jsonify
from api.views.auth import appblueprint


@appblueprint.errorhandler(400)
def bad_request(error):
    return jsonify({"msg": "Bad request"}), 400
