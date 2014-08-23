from __future__ import absolute_import

import unittest
from time import sleep
import config
from config.local import MONGODB_SETTINGS

from app import create_app
class MongoTestCase(unittest.TestCase):

    def setUp(self):
        self.db_name = "asteroids_test"
        db_settings = MONGODB_SETTINGS.copy()
        db_settings['DB'] = self.db_name
        self.app, self.db = create_app({"MONGODB_SETTINGS": db_settings})
        self.client = self.app.test_client()

    def tearDown(self):
        self.db.connection.drop_database(self.db_name)
