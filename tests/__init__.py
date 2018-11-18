from instance import create_app

app = create_app(config_name='development')

from api.views import appblueprint

app.register_blueprint(appblueprint, url_prefix = '/v2/api/')
