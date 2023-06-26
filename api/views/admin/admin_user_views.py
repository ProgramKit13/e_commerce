from flask_restful import Resource
from datetime import datetime
from api import api
from ...schemas import user_schema
from flask import request, make_response, jsonify
from ...entities import user
from ...services import user_service, adminPreferences_service
from ...schemas.validators import validator
import secrets
from validate_docbr import CPF
from ...decorators import admin_required

###Register
class adminRegister(Resource):
     @admin_required
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
            adminAccess = request.json['adminAccess']
            phone = request.json['phone']
            dateCreation = datetime.today()
            token = secrets.token_hex(6)


            ##Preferences
            productPerPage = 50
            suppliersPerPage = 50

            if productPerPage is None or productPerPage != 50 or productPerPage.isnumeric() is not True:
                productPerPage = 50
            
            if suppliersPerPage is None or suppliersPerPage != 50 or suppliersPerPage.isnumeric() is not True:
                suppliersPerPage = 50

            validateEmail = validator.email_validate(email)
            if validateEmail is not True:
                verify = False
                errorTypes['email'] = 'Invalid email.'

            validatePass =validator.pass_validate(password)
            if validatePass == False:
                verify = False
                errorTypes['password'] = 'Password out of standard.'

            if firstName.isalpha() is not True:
                verify = False
                errorTypes['firstName'] = 'Name with spaces or special characters.'

            
            if lastName.isalpha() is not True:
                verify = False
                errorTypes['lastName'] = 'Name with spaces or special characters.'

            validateCPF = CPF()
            cpfValidate = validateCPF.validate(cpf)
            if cpfValidate == False:
                verify = False
                errorTypes['cpf'] = 'Invalid cpf.'
            
            if genre != '1' and genre != '2' and genre != '3':
                verify = False
                errorTypes['genre'] = 'Invalid option.'

            if verify:
                new_user = user.User(firstName=firstName, lastName=lastName, email=email, password=password, cpf=cpf, genre=genre, token=token, dateCreation=dateCreation, adminAccess=adminAccess, phone=phone)
                result = user_service.user_register(new_user)
                new_preferences = adminPreferences_service.create_adminPreferences(token=token, productPerPage=productPerPage, suppliersPerPage=suppliersPerPage)
                ref = cs.jsonify(result)
                return make_response(ref, 201)
            else:
                return make_response(jsonify(errorTypes), 404)
##############################


##Search
class AdminUserList(Resource):
    @admin_required
    def get(self):
        users = user_service.user_list()
        cs = user_schema.UserSchema(many=True)
        return make_response(cs.jsonify(users), 200)

class UserSearchByEmail(Resource):
    @admin_required
    def get(self, email):
        user = user_service.user_list_email(email)
        if user is None:
            return make_response(jsonify("User not found"), 404)
        
        return make_response(jsonify(user), 200)
    
class UserSearchByCpf(Resource):
    @admin_required
    def get(self, cpf):
        user = user_service.user_list_cpf(cpf)
        if user is None:
            return make_response(jsonify("User not found"), 404)
        
        return make_response(jsonify(user), 200)
#############################

##Update
class UpgradeUser(Resource):
    @admin_required
    def put(self, id):
        verify = True
        errorTypes = {}
        user_db = user_service.get_user_id(id)
        if user_db is None:
            return make_response(jsonify("User not found."), 404)
        ps = user_schema.UserSchema()
        validate = ps.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 404)
        else:
            firstName = request.json["firstName"]
            lastName = request.json["lastName"]
            email = request.json["email"]
            cpf = request.json["cpf"]
            genre = request.json["genre"]
            adminAccess = request.json["adminAccess"]
            password = request.json["password"]
            phone = request.json['phone']
            dateCreation = datetime.today()
            token = user_db.token

            validateEmail = validator.email_validate(email)
            if validateEmail is not True:
                verify = False
                errorTypes['email'] = 'Invalid email.'

            validatePass =validator.pass_validate(password)
            if validatePass == False:
                verify = False
                errorTypes['password'] = 'Password out of standard.'

            if firstName.isalpha() is not True:
                verify = False
                errorTypes['firstName'] = 'Name with spaces or special characters.'

            
            if lastName.isalpha() is not True:
                verify = False
                errorTypes['lastName'] = 'Name with spaces or special characters.'

            validateCPF = CPF()
            cpfValidate = validateCPF.validate(cpf)
            if cpfValidate == False:
                verify = False
                errorTypes['cpf'] = 'Invalid cpf.'
            
            if genre != '1' and genre != '2' and genre != '3':
                verify = False
                errorTypes['genre'] = 'Invalid option.'

            if type(phone) != int:
                verify = False
                errorTypes['phone'] = 'Invalid format.'
            else:
                phone = str(request.json['phone'])

            if verify:
                upgradeUser = user.User(firstName=firstName, lastName=lastName, cpf=cpf, genre=genre, password=password, dateCreation=dateCreation, email=email, adminAccess=adminAccess, token=token, phone=phone)
                user_service.user_update(user_db, upgradeUser)
                response = user_service.get_user_id(id)
                return make_response(ps.jsonify(response), 200)
            else:
                return make_response(jsonify(errorTypes), 404)
#############################


##Delete
class DeleteUser(Resource):
    @admin_required
    def delete(self, id):
        idAddress = user_service.search_for_delete(id)
        idUser = user_service.get_user_id(id)
        if idAddress and type(idAddress) == list:
            for address in idAddress:
                for values in address:
                    user_service.user_delete_adresses(values)
        if idUser is None:
            return make_response(jsonify("User not found"), 404)
        user_service.user_delete(idUser)
        return make_response(jsonify("User deleted successfully!"), 204)




api.add_resource(AdminUserList, '/admin_dashboard/list_user')

api.add_resource(adminRegister, '/admin_dashboard/user_register')

api.add_resource(UserSearchByEmail, '/admin_dashboard/user_search_by_email/<string:email>')

api.add_resource(UpgradeUser, '/admin_dashboard/user_update/<int:id>')

api.add_resource(DeleteUser, '/admin_dashboard/user_delete/<int:id>')