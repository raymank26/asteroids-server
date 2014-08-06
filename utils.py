import json
from flask import Response
def jsonable(func):
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        if type(value) == dict:
            return json.dumps(value)
        return Response(json.dumps(value[0]),
            mimetype="application/json",
            status=value[1])
    return wrapper
