
from flask_jwt_extended import get_jwt_identity

class PermissionAccessException(Exception):
    pass


def check_object_permission(user_id):
    current_user_id = get_jwt_identity()
    if current_user_id != user_id:
        raise PermissionAccessException