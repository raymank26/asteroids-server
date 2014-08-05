from __future__ import absolute_import
from flask import Blueprint
from utils import jsonable

scores = Blueprint("scores", __name__, url_prefix="/scores")

@scores.route("/top10/", methods=["GET"])
@jsonable
def top_ten():
    return {
        "foo": 120123,
        "bar": 120123,
    }
