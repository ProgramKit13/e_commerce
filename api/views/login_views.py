from flask_restful import Resource
from datetime import datetime
from api import api, jwt
from ..schemas import login_schema
from flask import request, make_response, jsonify
from ..services import user_service
from ..schemas.validators import validator
from flask_jwt_extended import create_access_token, create_refresh_token
from datetime import timedelta

class Login(Resource):
            
    @jwt.additional_claims_loader
    def add_claimns_to_access_token(identify):
        user_token = user_service.get_user_id(identify)
        if user_token.adminAccess:
            rules = 'admin'
        else:
            rules = 'user'
        return {'rules':rules}
    

    def post(self):
        verify = True
        errorTypes = {}
        ls = login_schema.UserSchema()
        validate = ls.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            email = request.json["email"]
            password = request.json["password"]


            validateEmail = validator.email_validate(email)
            if validateEmail is not True:
                verify = False
                errorTypes['email'] = 'E-mail inválido.'

            validatePass =validator.pass_validate(password)
            if validatePass == False:
                verify = False
                errorTypes['password'] = 'Senha fora dos critérios.'



            user_bd = user_service.user_email(email)
            if user_bd and user_bd.verify_pass(password):
                access_token = create_access_token(
                    identity = user_bd.id,
                    expires_delta=timedelta(seconds=1000)
                )

                refresh_token = create_refresh_token(
                    identity=user_bd.id
                )
                return make_response(jsonify({
                    'access_token':access_token,
                    'refresh_token':refresh_token,
                    'msgm':'Login realizado com sucesso.' 
                }), 200)
            
            return make_response(jsonify({
                'msgm':'Credenciais inválidas.'
            }), 401)
            



api.add_resource(Login, '/login')
