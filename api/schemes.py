from voluptuous import Schema


def is_unicode(x):
    # print x
    return x[0].decode('utf-8')

user_creation = Schema({
    "username": unicode,
    "password1": unicode,
    "password2": unicode,
}, required=True)


user_auth = Schema({
    "username": unicode,
    "password": unicode
}, required=True)
