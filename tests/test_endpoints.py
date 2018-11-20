import unittest
import os
import json
from tests import app
from api.views.utilities import user_db

class BaseTestCase(unittest.TestCase):
    """This class represents the bucketlist test case"""

    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        with self.app.test_client() as client:
           user_db.create_tables()
           self.test_user1 = {"Name":"wali","Email":"walimike@ymail.com",\
           "Password":"1234","Role":"Admin"}
           self.test_order ={"Source":"jinja","Destination":"kampala",\
           "Parcel name":"car","Present Location":"masindi","Price":1234}

    def register_user(self, ):
        return self.client.post('/v2/api/auth/signup', data=self.test_user1)

    def login_user(self):
        return self.client.post('/v2/api/auth/login', data=self.test_user1)

    def get_token(self):
        response = self.client.post('/v2/api/auth/login', data=self.test_user1)
        data = json.loads(response.data.decode())
        return 'Bearer ' + data['access_token']

    def test_can_make_order(self):
        self.register_user()
        self.login_user()
        res = self.client.post(
            '/v2/api/parcels', content_type='application/json',
            headers={'Authorization': self.get_token()},
            data=self.test_order)
        self.assertEqual(res.status_code, 201)
