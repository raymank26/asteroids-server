import json
def jsonable(func):
    def wrapper(*args, **kwargs):
        value = json.dumps(func(*args, **kwargs))
        return value
        # if type(value) == tuple:

    return wrapper
