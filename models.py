from mongoengine import (
    Document,
    StringField,
    IntField,
    ReferenceField,
    DateTimeField
)
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
import random


class User(Document):
    username = StringField(required=True, unique=True)
    password = StringField(required=True)
    auth_token = StringField()

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def bind_token(self):
        self.auth_token = ''.join(
            random.choice('0123456789ABCDEF') for i in range(16))
        self.save()


class Score(Document):
    value = IntField(required=True)
    datetime = DateTimeField(default = lambda: datetime.datetime.now())
    user = ReferenceField(User)




