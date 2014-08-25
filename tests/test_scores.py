from __future__ import absolute_import
from tests.base import MongoTestCase
import json

class UserCreation(MongoTestCase):

    def test_empty_top_ten(self):
        self.assertEqual(self.get_top(), [])
        # self.assertEqual(response.status, "200 OK")
        # self.assertEqual(json.loads(response.data), [])

    def submit_score(self, score, token):
        data = {"score": score}
        return self.client.post("/scores/submit/",
            headers=[
            ('Authentication', token),
            ],
            data=data
            )

    def get_top(self):
        response = self.client.get("/scores/top10/")
        self.assertEqual(response.status, "200 OK")
        return json.loads(response.data)

    def test_submit(self):
        self.client.get("/")
        self.client.post("/users/", data={"username": "foobar",
            "password1": "123", "password2": "123"})
        response = self.client.put("/users/authenticate",
            data={"username": "foobar", "password": "123"})
        token = json.loads(response.data)['token']

        self.assertEqual(self.submit_score("100", token).status, "200 OK")
        self.assertEqual(self.submit_score("101", token).status, "200 OK")

        self.assertEqual(self.get_top(), [{u'username': u'foobar', u'value': 101}])
        # print(top)
