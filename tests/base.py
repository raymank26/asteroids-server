import unittest

from app import app as flask_app, db
class MongoTestCase(unittest.TestCase):

    def setUp(self):
        self.app = flask_app
        self.app.config['DB'] = "asteroids_test"
        self.client = self.app.test_client()

    def tearDown(self):
        db.connection.drop_database(self.app.config['DB'])


if __name__ == "__main__":
    unittest.main()
