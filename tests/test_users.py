from __future__ import absolute_import
import unittest
from tests.base import MongoTestCase
# import appbase

class UserCreation(MongoTestCase):
    def test_create_ok(self):
        response = self.client.post("/users/", data={
            "username": "raymank26",
            "password1": "123",
            "password2": "123"
            })
        self.assertEqual(response.status, "200 OK")
        # print(type(response.status)
        # print(dir(response))
        # print(response.data)



