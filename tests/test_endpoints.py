import unittest
from api import app
from api.views import my_parcels

class ApiTest(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.test_parcel = {"Owner":"wali","Source":"jinja","Destination":"mbale"\
        ,"Parcel name":"success card"}
        self.test_parcel2 = {"Owner":"wali","Source":"mbarara","Destination":"gulu"\
        ,"Parcel name":"mobile phone"}

    def tearDown(self):
        my_parcels.parcel_list, my_parcels.user_list = [],[]

    def test_welcome_message(self):
        response = self.client.get('/v1/api/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Welcome to Send It.', str(response.data))

    def test_empty_parcel_list(self):
        response = self.client.get('/v1/api/parcels')
        self.assertEqual(response.status_code, 200)

    def test_can_make_parcel_order(self):
        self.assertEqual(len(my_parcels.fetch_all_orders()), 0)
        self.assertEqual(len(my_parcels.fetch_all_users()), 0)
        response = self.client.post('/v1/api/parcels', json = self.test_parcel)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(my_parcels.fetch_all_orders()), 1)
        self.assertEqual(len(my_parcels.fetch_all_users()), 1)

    def test_make_order_by_same_user(self):
        response = self.client.post('/v1/api/parcels', json = self.test_parcel)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(my_parcels.fetch_all_orders()), 1)
        self.assertEqual(len(my_parcels.fetch_all_users()), 1)
        response = self.client.post('/v1/api/parcels', json = self.test_parcel2)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(my_parcels.fetch_all_orders()), 2)
        self.assertEqual(len(my_parcels.fetch_all_users()), 1)

    def test_can_verify_invalid_input(self):
        invalid_input = {"Owner":"wa4li","Source":"jinja","Destination":"mbale",\
        "Parcel name":"success card"}
        response = self.client.post('/v1/api/parcels', json = invalid_input)
        self.assertEqual(response.status_code, 400)
        self.assertIn('Ooops, one of the input fields is not in order', str(response.data))

    def test_can_validate_empty_string(self):
        invalid_input = {"Owner":"","Source":"jinja","Destination":"mbale",\
        "Parcel name":"success card"}
        response = self.client.post('/v1/api/parcels', json = invalid_input)
        self.assertEqual(response.status_code, 400)
        self.assertIn('Bad request', str(response.data))

    def test_can_validate_empty_string(self):
        invalid_input = {"Owner":"","Source":"jinja","Destination":"mbale",\
        "Parcel name":"success card"}
        response = self.client.post('/v1/api/parcels', json = invalid_input)
        self.assertEqual(response.status_code, 400)

    def test_can_validate_integer(self):
        invalid_input = {"Owner":6,"Source":"jinja","Destination":"mbale",\
        "Parcel name":'wali'}
        response = self.client.post('/v1/api/parcels', json = invalid_input)
        self.assertEqual(response.status_code, 400)
        self.assertIn('Ooops, one of the input fields is not in order', str(response.data))

    def test_can_return_users(self):
        self.client.post('/v1/api/parcels', json = self.test_parcel)
        response = self.client.get('/v1/api/users')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(my_parcels.fetch_all_users()),1)

    def test_can_get_specific_order(self):
        self.client.post('/v1/api/parcels', json = self.test_parcel)
        self.client.post('/v1/api/parcels', json = self.test_parcel2)
        response = self.client.get('/v1/api/parcels/1')
        self.assertEqual(response.status_code, 200)
