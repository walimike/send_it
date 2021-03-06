from tests.test_base import BaseTestCase
import unittest
import json
from tests import app
from api.views import db_conn

class EndTests(BaseTestCase):

    def test_cannot_fetch_all_orders_with_unauthorized_access(self):
        res = self.fetch_all_orders()
        self.assertEqual(res.status_code, 200)

    def test_cannot_change_present_location_with_unauthorized_access(self):
        res = self.change_order_location()
        self.assertEqual(res.status_code, 401)

    def test_can_change_order_destination(self):
        res = self.change_order_destination()
        self.assertEqual(res.status_code, 200)

    def test_can_not_change_order_destination_not_found(self):
        self.make_valid_order()
        new_destination = {"destination":"mpigi"}
        response = self.client.put( '/v2/api/parcels/100/destination', content_type='application/json',\
        headers={'Authorization': self.get_token()}, data=json.dumps(new_destination))
        self.assertEqual(response.status_code, 404)

    def test_cannot_change_order_status_with_unauthorized_access(self):
        res = self.change_order_status()
        self.assertEqual(res.status_code, 401)

    def test_can_fetch_all_orders_by_specific_user(self):
        self.make_valid_order()
        res = self.client.get( '/v2/api/users/parcels', content_type='application/json',\
        headers={'Authorization': self.get_token()})
        self.assertEqual(res.status_code, 200)

    def test_can_fetch_specific_order(self):
        self.make_valid_order()
        res = self.client.get( '/v2/api/parcels/1', content_type='application/json',\
        headers={'Authorization': self.get_token()})
        self.assertEqual(res.status_code, 200)

    def test_cannot_fetch_specific_order_out_of_range(self):
        self.make_valid_order()
        res = self.client.get( '/v2/api/parcels/1', content_type='application/json',\
        headers={'Authorization': self.get_token()})
        self.assertEqual(res.status_code, 200)
        res = self.client.get( '/v2/api/parcels/2', content_type='application/json',\
        headers={'Authorization': self.get_token()})
        self.assertEqual(res.status_code, 404)

    def test_cannot_fetch_all_orders_with_unauthorized_access(self):
        self.make_valid_order()
        res = self.client.get( '/v2/api/parcels', content_type='application/json',\
        headers={'Authorization': self.get_token()})
        self.assertEqual(res.status_code, 401)

    def test_cannot_make_invalid_order(self):
        response = self.client.post( '/v2/api/parcels',content_type='application/json',\
        headers={'Authorization': self.get_token()}, data=json.dumps({}))
        self.assertEqual(response.status_code, 400)

    def test_invalid_parcel_name_order(self):
        order ={"source":"jinja","destination":"kampala","parcelname":"car","price":1234}
        response = self.make_invalid_order(order)
        self.assertEqual(response.status_code, 400)
        self.assertIn("parcel_name key word is not in the right format",str(response.data))

    def test_invalid_source_name_order(self):
        order ={"sourcce":"jinja","destination":"kampala","parcel_name":"car","price":1234}
        response = self.make_invalid_order(order)
        self.assertEqual(response.status_code, 400)
        self.assertIn("source key word is not in the right format",str(response.data))

    def test_invalid_destination_name_order(self):
        order ={"source":"jinja","ddestination":"kampala","parcel_name":"car","price":1234}
        response = self.make_invalid_order(order)
        self.assertEqual(response.status_code, 400)
        self.assertIn("destination key word is not in the right format",str(response.data))

    def test_invalid_price_name_order(self):
        order ={"source":"jinja","destination":"kampala","parcel_name":"car","prrrice":1234}
        response = self.make_invalid_order(order)
        self.assertEqual(response.status_code, 400)
        self.assertIn("price key word is not in the right format",str(response.data))

    def test_invalid_parcel_order(self):
        order ={"source":"jinja","destination":"kampala","parcel_name":"car345","price":1234}
        response = self.make_invalid_order(order)
        self.assertEqual(response.status_code, 400)
        self.assertIn("an error occured in Parcel_name input",str(response.data))

    def test_invalid_source_order(self):
        order ={"source":2345,"destination":"kampala","parcel_name":"car","price":1234}
        response = self.make_invalid_order(order)
        self.assertEqual(response.status_code, 400)
        self.assertIn("an error occured in source input",str(response.data))

    def test_invalid_destination_order(self):
        order ={"source":"jinja","destination":4328563,"parcel_name":"car","price":1234}
        response = self.make_invalid_order(order)
        self.assertEqual(response.status_code, 400)
        self.assertIn("an error occured in destination input",str(response.data))

    def test_invalid_price_order(self):
        order ={"source":"jinja","destination":"kampala","parcel_name":"car","price":"rwf42"}
        response = self.make_invalid_order(order)
        self.assertEqual(response.status_code, 400)
        self.assertIn("an error occured in price input",str(response.data))

    def test_can_update_location(self):
        self.make_valid_order()
        res = self.client.put( '/v2/api/parcels/1/presentlocation', json={'present_location':'lira'}, content_type='application/json',\
        headers={'Authorization': self.get_admin_token()})
        self.assertEqual(res.status_code,200)
        self.assertIn("present location successfully changed",str(res.data))

    def test_can_fetch_all_orders(self):
        self.make_valid_order()
        res = self.client.get( '/v2/api/parcels', content_type='application/json',\
        headers={'Authorization': self.get_admin_token()})
        self.assertEqual(res.status_code,200)

    def test_can_change_order_status(self):
        self.make_valid_order()
        res = self.client.put( '/v2/api/parcels/1/cancel', json={'status':'cancel'},content_type='application/json',\
        headers={'Authorization': self.get_admin_token()})
        self.assertEqual(res.status_code,200)
        self.assertIn("successfully updated",str(res.data))

    def test_change_wrong_order_status(self):
        self.make_valid_order()
        res = self.client.put( '/v2/api/parcels/1/cancel', json={'status':'wrong'},content_type='application/json',\
        headers={'Authorization': self.get_admin_token()})
        self.assertEqual(res.status_code,400)
        self.assertIn("status can only be canceled",str(res.data))

    def test_change_order_status_doesnot_exist(self):
        self.make_valid_order()
        res = self.client.put( '/v2/api/parcels/5/cancel', json={'status':'cancel'},content_type='application/json',\
        headers={'Authorization': self.get_admin_token()})
        self.assertEqual(res.status_code,404)
        self.assertIn("order does not exist",str(res.data))

    def test_cannot_change_destination_by_wrong_user(self):
        self.make_valid_order()
        res = self.client.put( '/v2/api/parcels/1/destination', json={'destination':'kabarole'},content_type='application/json',\
        headers={'Authorization': self.get_token2()})
        self.assertEqual(res.status_code,401)
        self.assertIn("you do not have authorization over this parcel",str(res.data))
