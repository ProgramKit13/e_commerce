from flask_restful import Resource
from datetime import datetime
from api import api
from ..schemas import user_schema
from flask import request, make_response, jsonify
from ..entities import user
from ..services import user_service
from ..schemas.validators import validator
import secrets
from validate_docbr import CPF
import uuid
from ..decorators import admin_required, api_key_required

class userRegister(Resource):
     def post(self):
        verify = True
        errorTypes = {}
        cs = user_schema.UserSchema()
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            firstName = request.json['firstName']
            lastName = request.json['lastName']
            email = request.json["email"]
            password = request.json["password"]
            cpf = request.json["cpf"]
            genre = request.json['genre']
            adminAccess = False
            dateCreation = datetime.today()
            token = secrets.token_hex(6)
            apiKey = str(uuid.uuid4())
            validateEmail = validator.email_validate(email)
            if validateEmail is not True:
                verify = False
                errorTypes['email'] = 'E-mail inválido.'

            validatePass =validator.pass_validate(password)
            if validatePass == False:
                verify = False
                errorTypes['password'] = 'Senha fora dos critérios.'

            if firstName.isalpha() is not True:
                verify = False
                errorTypes['firstName'] = 'Nome com espaços ou caracteres especiais.'

            
            if lastName.isalpha() is not True:
                verify = False
                errorTypes['lastName'] = 'Nome com espaços ou caracteres especiais.'

            validateCPF = CPF()
            cpfValidate = validateCPF.validate(cpf)
            if cpfValidate == False:
                verify = False
                errorTypes['cpf'] = 'Cpf inválido.'
            
            if genre != '1' and genre != '2' and genre != '3':
                verify = False
                errorTypes['genre'] = 'Opção inválida.'

            if verify:
                new_user = user.User(firstName=firstName, lastName=lastName, email=email, password=password, cpf=cpf, genre=genre, token=token, dateCreation=dateCreation, adminAccess=adminAccess, apiKey=apiKey)
                result = user_service.user_register(new_user)
                ref = cs.jsonify(result)
                return make_response(ref, 201)
            else:
                return make_response(jsonify(errorTypes), 404)




api.add_resource(userRegister, '/user&register')
