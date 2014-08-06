from __future__ import absolute_import
from flask import Blueprint, request
from utils import jsonable
from .schemes import user_creation
from models import User
from voluptuous import MultipleInvalid, Invalid

users = Blueprint("users", __name__, url_prefix="/users")


# class UserCreate(restful.Resourse):
#     def post(self):
#         parser = reqparse.RequestParser()
#         parser.add_argument()

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
        return {"errors": e.error_message, "path": e.path}, 400
    user = User(username=_user['username'], password=_user['password1'])
    user.save()
    return {"success": True}


# @users.route('/', methods=['GET'])
# @jsonable
# def show():
#     return {"sdflkjsdf": "sdkj"}
