from flask import request, jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt
from functools import wraps

# Middleware to protect routes
def jwt_required_role(roles):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims["role"] not in roles:
                return jsonify({"error": "Unauthorized"}), 403
            return fn(*args, **kwargs)
        return wrapper
    return decorator
