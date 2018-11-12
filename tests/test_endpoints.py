from tests.test_base import BaseTestCase
import unittest
import json
from tests import app
from api.views.utilities import user_db,parcel_db
import os

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
        response = self.client.put( '/v2/api/parcels/10/destination', content_type='application/json',\
        headers={'Authorization': self.get_token()}, data=json.dumps(new_destination))
        self.assertEqual(response.status_code, 404)

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

    def test_cannot_fetch_all_orders_with_unauthorized_access(self):
        self.make_valid_order()
        res = self.client.get( '/v2/api/parcels', content_type='application/json',\
        headers={'Authorization': self.get_token()})
        self.assertEqual(res.status_code, 401)

    def test_cannot_make_invalid_order(self):
        response = self.client.post( '/v2/api/parcels',content_type='application/json',\
        headers={'Authorization': self.get_token()}, data=json.dumps({}))
        self.assertEqual(response.status_code, 400)

    def test_can_change_location(self):
        self.make_valid_order()
        new_location = {"present_location":"mpigi"}
