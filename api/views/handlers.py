from api.views.views import appblueprint
from flask import jsonify

@appblueprint.errorhandler(400)
def bad_request(error):
    return jsonify({"msg": "Bad request"}), 400
