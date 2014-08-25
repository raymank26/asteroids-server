from __future__ import absolute_import
from flask import Blueprint, request
from utils import jsonable, login_required, show_errors
from .schemes import user_creation, user_auth
from models import User
from voluptuous import MultipleInvalid, Invalid
from mongoengine import NotUniqueError

users = Blueprint("users", __name__, url_prefix="/users")


@users.route('/', methods=['POST'])
@jsonable
def create():
    data = request.form.to_dict()
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
    User.ensure_indexes()
    user = User(username=_user['username'])
    user.set_password(_user['password1'])
    try:
        user.save()
    except NotUniqueError as e:
        return {
            "path": ["username"],
            "errors": "user with same name exist"
            }, 400

    return {"success": True}


@users.route('/authenticate', methods=['PUT'])
@jsonable
def authenticate():
    common_error = {
        "non_field_errors": ["Pair user-password doesn't exist"]
    }
    data = request.form.to_dict()
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

@users.route('/check_auth/', methods=['GET'])
@jsonable
@login_required
def check(user):
    print user
    return "ok"


