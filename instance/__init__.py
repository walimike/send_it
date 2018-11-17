from instance.config import app_config
from flask import Flask
from api.models.parcels import ParcelDb
from api.models.users import UserDb


class AppSettings:

    def __init__(self,config_name):
        self.config = config_name

    def create_app(self):
        app = Flask(__name__, instance_relative_config=True)
        app.config.from_object(app_config[self.config])
        app.config.from_pyfile('config.py')
        return app

    def create_databases(self):
        parcel_db = ParcelDb(app_config[self.config].DATABASE_URL)
        user_db = UserDb(app_config[self.config].DATABASE_URL)
        parcel_db.drop_tables()
        user_db.drop_tables()
        parcel_db.create_tables()
        user_db.create_tables()
        return parcel_db, user_db
