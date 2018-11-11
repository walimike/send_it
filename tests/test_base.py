import unittest
import json
from tests import app
from api.views.utilities import user_db
import os
from api.models.models import User


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        with self.app.test_client():
            admin_user = User('admin','admin@gmail.com','@H@nN@H92','admin')
            user_db.create_tables()
            user_db.add_user(admin_user)
            self.test_user1 = {"name":"wali","email":"walimike@ymail.com",\
            "password":"wrej@jafcd"}
            self.test_order ={"source":"jinja","destination":"kampala",\
            "parcel_name":"car","price":1234}

    def tearDown(self):
        user_db.drop_tables()

    def register_user(self):
        response = self.client.post('/v2/api/auth/signup',\
        data=json.dumps(self.test_user1),content_type='application/json' )

    def admin_login(self):
        admin_user = {"name":"admin","password":"@H@nN@H92"}
        return self.client.post('/v2/api/auth/login',\
         data=json.dumps(self.test_user1),content_type='application/json')

    def login_user(self):
        return self.client.post('/v2/api/auth/login',\
         data=json.dumps(self.test_user1),content_type='application/json')

    def get_token(self):
        self.register_user()
        response = self.login_user()
        data = json.loads(response.data.decode())
        return 'Bearer ' + data['access_token']

    def get_admin_token(self):
        response = self.admin_login()
        data = json.loads(response.data.decode())
        return 'Bearer ' + data['access_token']

    def make_valid_order(self):
        response = self.client.post( '/v2/api/parcels',content_type='application/json',\
        headers={'Authorization': self.get_token()}, data=json.dumps(self.test_order))
        return response

    def fetch_all_orders(self):
        response = self.client.get( '/v2/api/parcels', content_type='application/json',\
        headers={'Authorization': self.get_token()}, data=json.dumps(self.test_order))
        return response

    def change_order_location(self):
        self.make_valid_order()
        new_destination = {"present_location":"mpererwe"}
        response = self.client.put( '/v2/api/parcels/1/presentlocation', content_type='application/json',\
        headers={'Authorization': self.get_token()}, data=json.dumps(new_destination))
        return response

    def change_order_destination(self):
        self.make_valid_order()
        new_destination = {"destination":"mpigi"}
        response = self.client.put( '/v2/api/parcels/1/destination', content_type='application/json',\
        headers={'Authorization': self.get_token()}, data=json.dumps(new_destination))
        return response

    def change_order_status(self):
        self.make_valid_order()
        new_destination = {"status":"cancel"}
        response = self.client.put( '/v2/api/parcels/1/cancel', content_type='application/json',\
        headers={'Authorization': self.get_token()}, data=json.dumps(new_destination))
        return response
