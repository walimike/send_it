import unittest
from api.views.views import my_parcels
from instance import create_app
from api.views import appblueprint


class ApiTest(unittest.TestCase):
    """
    Class inherits from unittest class. Used for testing app.
    """

    def setUp(self):
        self.app = create_app(config_name='testing')
        self.app.register_blueprint(appblueprint, url_prefix = '/test/api/')
        self.client = self.app.test_client()
        self.test_parcel = {"Owner":"wali","Source":"jinja","Destination":"mbale"\
        ,"Parcel name":"success card"}
        self.test_parcel2 = {"Owner":"wali","Source":"mbarara","Destination":"gulu"\
        ,"Parcel name":"mobile phone"}
        self.test_parcel3 = {"Owner":"munga","Source":"kampala","Destination":"soroti"\
        ,"Parcel name":"nissan"}

    def tearDown(self):
        my_parcels.parcel_list, my_parcels.user_list = [],[]

    def test_welcome_message(self):
        response = self.client.get('/test/api/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Welcome to Send It.', str(response.data))

    def test_empty_parcel_list(self):
        response = self.client.get('/test/api/parcels')
        self.assertEqual(response.status_code, 200)

    def test_can_make_parcel_order(self):
        self.assertEqual(len(my_parcels.fetch_all_orders()), 0)
        self.assertEqual(len(my_parcels.fetch_all_users()), 0)
        response = self.client.post('/test/api/parcels', json = self.test_parcel)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(my_parcels.fetch_all_orders()), 1)
        self.assertEqual(len(my_parcels.fetch_all_users()), 1)

    def test_make_order_by_same_user(self):
        response = self.client.post('/test/api/parcels', json = self.test_parcel)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(my_parcels.fetch_all_orders()), 1)
        self.assertEqual(len(my_parcels.fetch_all_users()), 1)
        response = self.client.post('/test/api/parcels', json = self.test_parcel2)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(my_parcels.fetch_all_orders()), 2)
        self.assertEqual(len(my_parcels.fetch_all_users()), 1)

    def test_can_verify_invalid_input(self):
        invalid_input = {"Owner":"wa4li","Source":"jinja","Destination":"mbale",\
        "Parcel name":"success card"}
        response = self.client.post('/test/api/parcels', json = invalid_input)
        self.assertEqual(response.status_code, 400)
        self.assertIn('Ooops, one of the input fields is not in order', str(response.data))

    def test_can_validate_empty_string(self):
        invalid_input = {"Owner":"","Source":"jinja","Destination":"mbale",\
        "Parcel name":"success card"}
        response = self.client.post('/test/api/parcels', json = invalid_input)
        self.assertEqual(response.status_code, 400)
        self.assertIn('Bad request', str(response.data))

    def test_can_validate_empty_string(self):
        invalid_input = {"Owner":"","Source":"jinja","Destination":"mbale",\
        "Parcel name":"success card"}
        response = self.client.post('/test/api/parcels', json = invalid_input)
        self.assertEqual(response.status_code, 400)

    def test_can_validate_integer(self):
        invalid_input = {"Owner":6,"Source":"jinja","Destination":"mbale",\
        "Parcel name":'wali'}
        response = self.client.post('/test/api/parcels', json = invalid_input)
        self.assertEqual(response.status_code, 400)
        self.assertIn('Ooops, one of the input fields is not in order', str(response.data))

    def test_can_return_users(self):
        self.client.post('/test/api/parcels', json = self.test_parcel)
        response = self.client.get('/test/api/users')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(my_parcels.fetch_all_users()),1)
        self.client.post('/test/api/parcels', json = self.test_parcel3)
        self.assertEqual(len(my_parcels.fetch_all_users()),2)

    def test_can_get_specific_order(self):
        response=self.client.post('/test/api/parcels', json = {})
        self.assertEqual(response.status_code, 400)
        self.assertIn('Bad request', str(response.data))
        self.client.post('/test/api/parcels', json = self.test_parcel2)
        response = self.client.get('/test/api/parcels/1')
        self.assertEqual(response.status_code, 200)

    def test_can_get_all_orders_by_specific_user(self):
        self.client.post('/test/api/parcels', json = self.test_parcel)
        self.client.post('/test/api/parcels', json = self.test_parcel2)
        response = self.client.get('/test/api/users/1/parcels')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/test/api/parcels/3')
        self.assertEqual(response.status_code, 400)
        self.client.post('/test/api/parcels', json = self.test_parcel2)
        response = self.client.get('/test/api/parcels/3')
        self.assertEqual(response.status_code, 200)

    def test_userid_out_of_range(self):
        self.client.post('/test/api/parcels', json = self.test_parcel)
        self.client.post('/test/api/parcels', json = self.test_parcel2)
        response = self.client.get('/test/api/users/1/parcels')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/test/api/users/5/parcels')
        self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    unittest.main
