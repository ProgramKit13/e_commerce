from flask_restful import Resource
from api import api
from ..schemas import userPayments_schema
from flask import request, make_response, jsonify
from ..services import userPayments_service, user_service
from ..schemas.validators import validator
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import date
import secrets

class FormPayment(Resource):
    @jwt_required
    def get(self, hash):
        cs = userPayments_schema.UserPayments_Schema()
        current_user = get_jwt_identity()
        get_user = user_service.get_user_token(current_user)
        verify = True
        errorTypes = {}
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            typePayment = request.json['typePayment']
            token = secrets.token_hex(64)
            value = request.json['value']
            status = 'panding'
            userToken = get_user
            datePayment = date.today()
            dateStatus = date.today()
            cartToken = secrets.token_hex(64)

            userPayments_service.create_payment(typePayment, token, value, status, userToken, datePayment, dateStatus)
            return make_response(jsonify('Payment created.'), 201)