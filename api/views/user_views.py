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
import bcrypt

class UserList(Resource):
    def get(self):
        users = user_service.user_list()
        cs = user_schema.UserSchema(many=True)
        return make_response(cs.jsonify(users), 200)


class UserSearchId(Resource):
    def get(self, id):
        user = user_service.user_list_id(id)
        if user is None:
            return make_response(jsonify("Usuário não encontrado"), 404)
        ps = user_schema.UserSchema()
        return make_response(ps.jsonify(user), 200)
    

class Register(Resource):
     def post(self):
        verify = True
        errorTypes = {}
        cs = user_schema.UserSchema()
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            name = request.json['name']
            email = request.json["email"]
            password = request.json["password"]
            cpf = request.json["cpf"]
            genre = request.json['genre']
            dateCreation = datetime.today()
            token = secrets.token_hex(32)

            print(dateCreation)

            validateEmail = validator.email_validate(email)
            if validateEmail is not True:
                verify = False
                errorTypes['email'] = 'E-mail inválido.'

            validatePass =validator.pass_validate(password)
            if validatePass == False:
                verify = False
                errorTypes['password'] = 'Senha fora dos critérios.'

            if name.isalpha() is not True:
                verify = False
                errorTypes['name'] = 'Nome com espaços ou caracteres especiais.'

            validateCPF = CPF()
            cpfValidate = validateCPF.validate(cpf)
            if cpfValidate == False:
                verify = False
                errorTypes['cpf'] = 'Cpf inválido.'
            
            if genre != '1' and genre != '2' and genre != '3':
                verify = False
                errorTypes['genre'] = 'Opção inválida.'

            if verify:
                salt = bcrypt.gensalt(8)
                hashPass = bcrypt.hashpw(password.encode('utf-8'), salt)
                new_user = user.User(name=name, email=email, password=hashPass, cpf=cpf, genre=genre, token=token, dateCreation=dateCreation)
                result = user_service.user_register(new_user)
                ref = cs.jsonify(result)
                return make_response(ref, 201)
            else:
                return make_response(jsonify(errorTypes), 404)


class SearchUser(Resource):
       def get(self, id):
           user = user_service.user_list_id(id)  
           if user is None:
               return make_response(jsonify("Usuário não encontrado"), 404)
           cs = user_schema.UserSchema()
           return make_response(cs.jsonify(user), 200)

class updatePass(Resource):
     def put(self, id):
        user_bd = user_service.user_list_id(id)
        if user_bd is None:
            return make_response(jsonify("Usuário não encontrado"), 404)
        cs = user_schema.updatePass()
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 404)
        else:
            password = request.json["password"]
            new_pass = user.updatePass(password=password)
            
        
        user_service.pass_update(user_bd, new_pass)
        massage = 'Senha atualizada com sucesso.'
        return massage 

api.add_resource(UserList, '/user&list')
api.add_resource(Register, '/user&register')
api.add_resource(updatePass, '/update&password/<int:id>')
api.add_resource(UserSearchId, '/search&user/<int:id>')