from instance import AppSettings
from api.views import appblueprint

app_settings = AppSettings('development')
app = app_settings.create_app()

app.register_blueprint(appblueprint, url_prefix = '/v2/api/')
