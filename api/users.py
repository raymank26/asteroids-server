from __future__ import absolute_import
from flask import Blueprint, request
from utils import jsonable
from .schemes import user_creation, user_auth
from models import User
from voluptuous import MultipleInvalid, Invalid

users = Blueprint("users", __name__, url_prefix="/users")


def show_errors(e):
    return {"errors": e.error_message, "path": e.path}, 400


@users.route('/', methods=['POST'])
@jsonable
def create():
    data = request.form.to_dict()
    print request.form
    try:
        _user = user_creation(data)
        if _user['password1'] != _user['password2']:
            raise MultipleInvalid(errors=[
                Invalid(
                    message="Passwords doesn't match",
                    path=["password1", "password2"])
            ])
    except MultipleInvalid as e:
        return show_errors(e)
    user = User(username=_user['username'])
    user.set_password(_user['password1'])
    user.save()
    return {"success": True}


@users.route('/authenticate', methods=['PUT'])
@jsonable
def authenticate():
    common_error = {
        "non_field_errors": ["Pair user-password doesn't exist"]
    }
    data = request.form.to_dict()
    print data
    try:
        _user = user_auth(data)
    except MultipleInvalid as e:
        return show_errors(e)
    try:
        user = User.objects.get(username=_user['username'])
    except User.DoesNotExist:
        return common_error, 400
    if not user.check_password(_user['password']):
        return common_error, 400
    if user.auth_token is None:
        user.bind_token()

    return {
        "token": user.auth_token
    }
