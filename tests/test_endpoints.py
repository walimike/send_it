from .testbase import BaseTestCase
import unittest
import json
from tests import app
from api.views.utilities import user_db
import os

class EndPointTests(BaseTestCase):

    def test_can_make_order(self):
        res = self.make_valid_order()
        self.assertEqual(res.status_code, 201)
        self.assertIn(str(res),'well done')

    def test_can_fetch_all_orders(self):
        res = self.fetch_all_orders()
        self.assertEqual(res.status_code, 200)

    def test_can_change_present_location(self):
        res = self.change_order_location()
        self.assertEqual(res.status_code, 200)
