from voluptuous import Schema, All, Length, Required

user_creation = Schema({
    "username": All(unicode, Length(min=3)),
    "password1": All(unicode, Length(min=3)),
    "password2": All(unicode, Length(min=3)),
}, required=True)


user_auth = Schema({
    "username": unicode,
    "password": unicode
}, required=True)


submit_score = Schema({
    "score": unicode
    }, required=True)
