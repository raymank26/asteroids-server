from mongoengine import Document, StringField
from werkzeug.security import generate_password_hash

class User(Document):
    username = StringField(required=True, unique=True)
    password = StringField(required=True)

    def save(self):
        self.password = generate_password_hash(self.password)
        super(User, self).save()


