from instance import create_app
from api.views import appblueprint

app = create_app(config_name='development')

app.register_blueprint(views.appblueprint, url_prefix = '/v1/api/')
