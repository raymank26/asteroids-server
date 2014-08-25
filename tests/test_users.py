from __future__ import absolute_import
from tests.base import MongoTestCase
import json
# import appbase


class UserCreation(MongoTestCase):

    def test_create_ok(self):
        response = self.client.post("/users/", data={
            "username": "raymank26",
            "password1": "123",
            "password2": "123"
            })
        self.assertEqual(response.status, "200 OK")

    def test_password_match_failed(self):
        response = self.client.post("/users/", data={
            "username": "raymank26",
            "password1": "123",
            "password2": "some another password"
            })

        self.assertEqual(json.loads(response.data)['path'],
            ["password1", "password2"])
        self.assertEqual(response.status, "400 BAD REQUEST")

    def test_fields_not_provided(self):
        response = self.client.post("/users/", data={})
        self.assertEqual(response.status, "400 BAD REQUEST")
        self.assertEqual(json.loads(response.data)['path'],
            ["username"])

    def test_empty_fields(self):
        response = self.client.post("/users/", data={"username": "",
            "password1": "", "password2": ""})
        self.assertEqual(response.status, "400 BAD REQUEST")

    def test_dups(self):
        response = self.client.post("/users/", data={"username": "foobar",
            "password1": "123", "password2": "123"})
        self.assertEqual(response.status, "200 OK")

        dups_response = self.client.post("/users/", data={"username": "foobar",
            "password1": "123", "password2": "123"})
        self.assertEqual(dups_response.status, "400 BAD REQUEST")


class UserAuth(MongoTestCase):
    def setUp(self):
        super(UserAuth, self).setUp()
        self.client.post("/users/", data={"username": "foobar",
            "password1": "123", "password2": "123"})

    # TODO: add more auth tests
    def test_auth_ok(self):
        response = self.client.put("/users/authenticate",
            data={"username": "foobar", "password": "123"})
        self.assertEqual(response.status, "200 OK")

    def test_auth_fail(self):
        response = self.client.put("/users/authenticate",
            data={"username": "foobar", "password": "another password"})
        self.assertEqual(response.status, "400 BAD REQUEST")
