
from models import User
def authenticate(token):
    try:
        user = User.objects.findOne(token=token)
        return user
    except User.DoesNotExist:
        return None






