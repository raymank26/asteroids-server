from __future__ import absolute_import

from flask import Blueprint, request, g
from voluptuous import MultipleInvalid

from .schemes import submit_score
from utils import jsonable, login_required, show_errors
from models import Score, User
# from app import db

scores = Blueprint("scores", __name__, url_prefix="/scores")


@scores.route("/top10/", methods=["GET"])
@jsonable
def top_ten():
    scores = Score._get_collection().aggregate([{
        "$group": {"_id": "$user", "value": {"$max": "$value"}}
    },
        {"$sort": {"value": -1}}
    ])
    res = []
    for score in scores['result']:
        # print score['_id']
        res.append({
            "username": User.objects.get(id=score['_id']).username,
            "value": score['value']
            })

    return res


@scores.route("/submit/", methods=['POST'])
@login_required
@jsonable
def submit(user):
    try:
        score_ = submit_score(request.form.to_dict())
    except MultipleInvalid as e:
        return show_errors(e)

    score = Score(value=score_['score'], user=user)
    score.save()
    return {"success": True}
