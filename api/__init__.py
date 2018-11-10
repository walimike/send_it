from flask import Flask

app = Flask(__name__)

from api.views import appblueprint

app.register_blueprint(views.appblueprint, url_prefix = '/v1/api/')
