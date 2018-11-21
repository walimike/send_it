from .testbase import BaseTestCase
import unittest
import json
from tests import app
from api.views.utilities import user_db
import os

class EndPointTests(BaseTestCase):

    def test_can_make_order(self):
        res = self.make_valid_order()
        self.assertEqual(res.status_code, 200)

    def test_can_fetch_all_orders(self):
        res = self.fetch_all_orders()
        self.assertEqual(res.status_code, 200)

    def test_can_change_present_location(self):
        res = self.change_order_location()
        self.assertEqual(res.status_code, 200)

    def test_can_not_change_order_destinstion_not_found(self):
        res = self.change_order_destination()
        self.assertEqual(res.status_code, 404)

    def test_can_change_order_status(self):
        res = self.change_order_status()
        self.assertEqual(res.status_code, 200)

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

    def test_can_fetch_all_orders(self):
        self.make_valid_order()
        res = self.client.get( '/v2/api/parcels', content_type='application/json',\
        headers={'Authorization': self.get_token()})
        self.assertEqual(res.status_code, 200)
