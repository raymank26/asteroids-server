import json
from flask import Response, request, abort
from functools import wraps
from models import User

def jsonable(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        if type(value) == dict:
            return json.dumps(value)
        if type(value) == tuple:
            return Response(json.dumps(value[0]),
                mimetype="application/json",
                status=value[1])
        return Response(json.dumps(value),
                mimetype="application/json")
    return wrapper

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.headers.get("Authentication")
        if not token:
            abort(403)
        try:
            user = User.objects.get(auth_token=token)
        except User.DoesNotExist:
            abort(403)
        return func(user, *args, **kwargs)
    return wrapper


def show_errors(e):
    return {"errors": e.error_message, "path": e.path}, 400


