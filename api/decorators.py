from functools import wraps
from flask_jwt_extended import get_jwt, verify_jwt_in_request
from flask import make_response, jsonify, request
from .services.user_service import api_key

def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt()
        if claims['rules'] != 'admin':
           return make_response(jsonify(msgm = 'Feature only allowed for admins.'), 403)
        else:
            return fn(*args, **kwargs)
    return wrapper


def api_key_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        apiKey = request.args.get('apiKey')
        if apiKey and api_key(apiKey):
            return fn(*args, **kwargs)
        else:
            return make_response(jsonify(msm='Invalid token api.'), 401)
    return wrapper