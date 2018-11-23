import unittest
from tests import app
from api.views.utilities import db_conn

class TestApi(unittest.TestCase):
    """
    Class inherits from unittest class. Used for testing app.
    """

    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        with self.app.test_client() as client:
           db_conn.create_tables()
           self.test_user1 = {"name":"wali","email":"walimike@ymail.com",\
           "password":"12safgerg34"}

    def tearDown(self):
        db_conn.drop_tables()

    def test_can_sign_up(self):
        response = self.client.post('/v2/api/auth/signup', json = self.test_user1)
        self.assertIn('you have successfully signed up', str(response.data))
        self.assertEqual(response.status_code, 201)

    def test_cannot_sign_up_twice(self):
        response = self.client.post('/v2/api/auth/signup', json = self.test_user1)
        self.assertIn('you have successfully signed up', str(response.data))
        self.assertEqual(response.status_code, 201)
        response = self.client.post('/v2/api/auth/signup', json = self.test_user1)
        self.assertIn('user already exists with this credentials', str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_user_does_not_exist(self):
        response = self.client.post('/v2/api/auth/signup', json = self.test_user1)
        self.assertIn('you have successfully signed up', str(response.data))
        self.assertEqual(response.status_code, 201)
        unknown_user = {"name":"nantume","email":"nantume@ymail.com","password":"12safgerg34"}
        response = self.client.post('/v2/api/auth/login', json = unknown_user)
        self.assertIn('user does not exist, do you want to signup', str(response.data))
        self.assertEqual(response.status_code, 404)


    def test_invalid_sign_up_name_key(self):
        invalid_user = {"Naame":"wali","email":"walimike@ymail.com",\
        "password":"1234"}
        response = self.client.post('/v2/api/auth/signup', json = invalid_user)
        self.assertEqual(response.status_code, 400)
        self.assertIn('name key word is not in the right format', str(response.data))

    def test_invalid_sign_up_email_key(self):
        invalid_user = {"name":"wali","Evmail":"walimike@ymail.com",\
        "password":"1234"}
        response = self.client.post('/v2/api/auth/signup', json = invalid_user)
        self.assertEqual(response.status_code, 400)
        self.assertIn('email key word is not in the right format', str(response.data))

    def test_invalid_sign_up_password_key(self):
        invalid_user = {"name":"wali","email":"walimike@ymail.com",\
        "Passwdaord":"1234"}
        response = self.client.post('/v2/api/auth/signup', json = invalid_user)
        self.assertEqual(response.status_code, 400)
        self.assertIn('password key word is not in the right format', str(response.data))

    def test_short_password(self):
        invalid_user = {"name":"wali","email":"walimike@ymail.com",\
        "password":"1234"}
        response = self.client.post('/v2/api/auth/signup', json = invalid_user)
        self.assertEqual(response.status_code, 400)
        self.assertIn('an error occured in password input', str(response.data))

    def test_can_not_login_wrong_password(self):
        self.client.post('/v2/api/auth/signup', json = self.test_user1)
        login_credentials = {"name":"wali","password":"1dr23ifssdfs4"}
        response = self.client.post('/v2/api/auth/login', json = login_credentials)
        self.assertEqual(response.status_code, 400)

    def test_can_login(self):
        self.client.post('/v2/api/auth/signup', json = self.test_user1)
        login_credentials = {"name":"wali","password":"12safgerg34"}
        response = self.client.post('/v2/api/auth/login', json = login_credentials)
        self.assertEqual(response.status_code, 200)

    def test_invalid_json(self):
        self.client.post('/v2/api/auth/signup', json = self.test_user1)
        response = self.client.post('/v2/api/auth/login', json = {})
        self.assertEqual(response.status_code, 400)
        response = self.client.post('/v2/api/auth/login', json = {"name":"wali","password":""})
        self.assertEqual(response.status_code, 400)
        response = self.client.post('/v2/api/auth/login', json = {"Naaame":"wali","password":"ssafggrtrssv"})
        self.assertEqual(response.status_code, 400)
        response = self.client.post('/v2/api/auth/login', json = {"name":"wali","Pazvvssword":"serteseytsgsd"})
        self.assertEqual(response.status_code, 400)


    def test_can_fetch_all_users_not_prote(self):
        response = self.client.get('/v2/api/users')
        self.assertEqual(response.status_code, 200)
