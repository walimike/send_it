from flask import Blueprint, jsonify, abort, request, make_response, json

appblueprint = Blueprint('api',__name__)

@appblueprint.route('/')
def welcomeMessage():
    return "<h1>Welcome to Send It.</h1>"
