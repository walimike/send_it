import unittest
from instance import create_app
from api.models.users import UserDb
from api.models.parcels import ParcelDb
from tests import app
import json

class TestApi(unittest.TestCase):
    """
    Class inherits from unittest class. Used for testing app.
    """

    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.test_userdb = UserDb()
        self.test_parceldb = ParcelDb()
        self.test_user1 = {"Name":"wali","Email":"walimike@ymail.com",\
        "Password":"1234","Role":"Admin"}

    def tearDown(self):
        pass

    def test_can_sign_up(self):
        response = self.client.post('/v2/api/auth/signup', json = self.test_user1)
        self.assertEqual(response.status_code, 200)
        self.assertIn('wali', str(response.data))
