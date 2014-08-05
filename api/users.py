from __future__ import absolute_import
from flask import Blueprint
from utils import jsonable

users = Blueprint("users", __name__, url_prefix="/users")


@users.route('/', methods=['POST'])
def create():
    pass

@users.route('/', methods=['GET'])
@jsonable
def show():
    return {"sdflkjsdf": "sdkj"}
