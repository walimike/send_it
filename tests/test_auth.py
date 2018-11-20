import unittest
from instance import create_app
from api.views.auth import  user_db
from tests import app
import json

class TestApi(unittest.TestCase):
    """
    Class inherits from unittest class. Used for testing app.
    """

    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.test_user1 = {"Name":"wali","Email":"walimike@ymail.com",\
        "Password":"1234","Role":"Admin"}

    def tearDown(self):
        pass

    def test_can_sign_up(self):
        response = self.client.post('/v2/api/auth/signup', json = self.test_user1)
        self.assertIn('wali', str(response.data))
        self.assertEqual(response.status_code, 201)

    def test_invalid_sign_up_name_key(self):
        invalid_user = {"Naame":"wali","Email":"walimike@ymail.com",\
        "Password":"1234","Role":"Admin"}
        response = self.client.post('/v2/api/auth/signup', json = invalid_user)
        self.assertEqual(response.status_code, 400)
        self.assertIn('Name key word is not in the right format', str(response.data))

    def test_invalid_sign_up_email_key(self):
        invalid_user = {"Name":"wali","Evmail":"walimike@ymail.com",\
        "Password":"1234","Role":"Admin"}
        response = self.client.post('/v2/api/auth/signup', json = invalid_user)
        self.assertEqual(response.status_code, 400)
        self.assertIn('Email key word is not in the right format', str(response.data))

    def test_invalid_sign_up_name_key(self):
        invalid_user = {"Name":"wali","Email":"walimike@ymail.com",\
        "Password":"1234","Roole":"Admin"}
        response = self.client.post('/v2/api/auth/signup', json = invalid_user)
        self.assertEqual(response.status_code, 400)
        self.assertIn('Role key word is not in the right format', str(response.data))

    def test_invalid_sign_up_password_key(self):
        invalid_user = {"Name":"wali","Email":"walimike@ymail.com",\
        "Passwdaord":"1234","Role":"Admin"}
        response = self.client.post('/v2/api/auth/signup', json = invalid_user)
        self.assertEqual(response.status_code, 400)
        self.assertIn('Password key word is not in the right format', str(response.data))

    def test_can_login(self):
        self.client.post('/v2/api/auth/signup', json = self.test_user1)
        login_credentials = {"Name":"wali","Password":"1dr234"}
        response = self.client.post('/v2/api/auth/login', json = login_credentials)
        self.assertEqual(response.status_code, 200)

    def test_invalid_json(self):
        self.client.post('/v2/api/auth/signup', json = self.test_user1)
        response = self.client.post('/v2/api/auth/login', json = {})
        self.assertEqual(response.status_code, 400)
        response = self.client.post('/v2/api/auth/login', json = {"Name":"wali","Password":""})
        self.assertEqual(response.status_code, 400)
