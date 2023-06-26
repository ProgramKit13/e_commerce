from flask_restful import Resource
from datetime import datetime
from api import api
from ..schemas import user_schema
from flask import request, make_response, jsonify
from ..entities import user, adminPreferences
from ..services import user_service, adminPreferences_service
from ..schemas.validators import validator
import secrets
from validate_docbr import CPF
from flask_jwt_extended import jwt_required, get_jwt_identity

class UserRegister(Resource):
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
            adminAccess = True
            dateCreation = datetime.today()
            token = secrets.token_hex(6)

            ##Preferences
            productsPerPage = 'fifty'
            suppliersPerPage = 'fifty'
                
            validateEmail = validator.email_validate(email)
            if validateEmail is not True:
                verify = False
                errorTypes['email'] = 'Invalid email.'

            validatePass =validator.pass_validate(password)
            if validatePass == False:
                verify = False
                errorTypes['password'] = 'Password out of standard.'

            validateName = validator.validate_text(name)
            if validateName != True:
                verify = False
                errorTypes['firstName'] = validateName
            
       


            if verify:
                new_user = user.User(name=name, email=email, password=password, token=token, dateCreation=dateCreation, adminAccess=adminAccess)
                result = user_service.user_register(new_user)

                adminPreferences_service.create_adminPreferences(token, productsPerPage, suppliersPerPage)
                ref = cs.jsonify(result)
                return make_response(ref, 201)
            else:
                return make_response(jsonify(errorTypes), 404)


class UserUpdate(Resource):
    @jwt_required()
    def post(self):
        current_user = get_jwt_identity()
        get_token = user_service.get_user(current_user)
        get_user = user_service.get_user_token(get_token)
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
            phone = request.json['phone']
            adminAccess = False
            dateCreation = datetime.today()
            token = get_user.token

            if "phone" in request.json:
                phone = request.json['phone']
            else:
                phone = None
                
            validateEmail = validator.email_validate(email)
            if validateEmail is not True:
                verify = False
                errorTypes['email'] = 'Invalid email.'

            validatePass =validator.pass_validate(password)
            if validatePass == False:
                verify = False
                errorTypes['password'] = 'Password out of standard.'

            validateFirstName = validator.validate_name(firstName)
            if validateFirstName != True:
                verify = False
                errorTypes['firstName'] = validateFirstName
            
            validateLastName = validator.validate_name(lastName)
            if validateLastName != True:
                verify = False
                errorTypes['lastName'] = validateLastName

            validateCPF = CPF()
            cpfValidate = validateCPF.validate(cpf)
            if cpfValidate == False:
                verify = False
                errorTypes['cpf'] = 'Invalid cpf.'
            
            if genre != '1' and genre != '2' and genre != '3':
                verify = False
                errorTypes['genre'] = 'Option invalid.'



            if verify:
                    updateUser = user.User(firstName=firstName, lastName=lastName, email=email, password=password, cpf=cpf, genre=genre, token=token, dateCreation=dateCreation, adminAccess=adminAccess, phone=phone)
                    user_service.user_update(get_user,updateUser)
                    response = user_service.get_user_token(get_token)
                    return make_response(cs.jsonify(response), 200)
            else:
                 return make_response(jsonify(errorTypes), 404)


class UserDelete(Resource):
    @jwt_required()
    def delete(self):
        current_user = get_jwt_identity()
        get_token = user_service.get_user(current_user)
        get_user = user_service.get_user_token(get_token)
        idAddress = user_service.search_for_delete(get_user.id)
        idUser = user_service.get_user_id(get_user.id)
        if idAddress and type(idAddress) == list:
            for address in idAddress:
                for values in address:
                   user_service.user_delete_adresses(values)
        if idUser is None:
             return make_response(jsonify("User not found"), 404)
        user_service.user_delete(idUser)
        return make_response(jsonify("User deleted successfully!"), 204)




api.add_resource(UserRegister, '/register')
api.add_resource(UserUpdate, '/update')
api.add_resource(UserDelete, '/delete')
