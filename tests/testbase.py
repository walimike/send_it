import unittest
import json
from tests import app
from api.views.utilities import user_db
import os

class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        with self.app.test_client():
           user_db.create_tables()
           self.test_user1 = {"Name":"wali","Email":"walimike@ymail.com",\
           "Password":"1234","Role":"Admin"}
           self.test_order ={"Source":"jinja","Destination":"kampala",\
           "Parcel name":"car","Present Location":"masindi","Price":1234}

    def register_user(self, ):
        response = self.client.post('/v2/api/auth/signup',\
        data=json.dumps(self.test_user1),content_type='application/json' )


    def login_user(self):
        return self.client.post('/v2/api/auth/login',\
         data=json.dumps(self.test_user1),content_type='application/json')

    def get_token(self):
        self.register_user()
        response = self.login_user()
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
        new_destination = {"Present Location":"Mpererwe"}
        response = self.client.put( '/v2/api/parcels/1/presentlocation', content_type='application/json',\
        headers={'Authorization': self.get_token()}, data=json.dumps(new_destination))
        return response

    def change_order_destination(self):
        self.make_valid_order()
        new_destination = {"Destination":"Mpigi"}
        response = self.client.put( '/v2/api/parcels/2/destination', content_type='application/json',\
        headers={'Authorization': self.get_token()}, data=json.dumps(new_destination))
        return response

    def change_order_status(self):
        self.make_valid_order()
        new_destination = {"Status":"Cancel"}
        response = self.client.put( '/v2/api/parcels/1/status', content_type='application/json',\
        headers={'Authorization': self.get_token()}, data=json.dumps(new_destination))
        return response
