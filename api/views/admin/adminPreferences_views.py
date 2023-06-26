from flask_restful import Resource
from api import api
from ...schemas import adminPreferences_schema
from flask import request, make_response, jsonify
from ...entities import adminPreferences
from ...models import adminPreferences_model
from ...services import adminPreferences_service, user_service
from ...decorators import admin_required
from flask_jwt_extended import jwt_required, get_jwt_identity

class CreateAdminPreferences(Resource):
    @admin_required
    def post(self):
        verify = True
        errorTypes = {}
        cs = adminPreferences_schema.AdminPreferencesSchema()
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            token = request.json['token']
            productsPerPage = request.json['productsPerPage']

            adminPreferences = adminPreferences_service.get_adminPreferences_by_token(token)
            if adminPreferences:
                verify = False
                errorTypes['token'] = 'Token already exists.'
            
            if verify:
                adminPreferences = adminPreferences_service.create_adminPreferences(token, productsPerPage)
                return make_response(jsonify(cs.dump(adminPreferences)), 201)
            else:
                return make_response(jsonify(errorTypes), 400)
            

class UpdateAdminPreferences(Resource):
    @admin_required
    def put(self):
        verify = True
        errorTypes = {}
        cs = adminPreferences_schema.AdminPreferencesSchema()
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            token = request.json['token']
            productsPerPage = request.json['productsPerPage']

            adminPreferences = adminPreferences_service.get_adminPreferences_by_token(token)
            if not adminPreferences:
                verify = False
                errorTypes['token'] = 'Token not found.'
            
            if verify:
                adminPreferences = adminPreferences_service.update_adminPreferencesPerPage(adminPreferences, productsPerPage)
                return make_response(jsonify(cs.dump(adminPreferences)), 200)
            else:
                return make_response(jsonify(errorTypes), 400)


class UpdatePreferencePerPageAdmin(Resource):
    @admin_required
    def put(self):
        getdUserIdentify = get_jwt_identity()
        getUser = user_service.get_user_id(getdUserIdentify)
        adminPreferences = adminPreferences_service.get_adminPreferencesPerpage_by_token(getUser.token)  # agora isto é uma instância completa do modelo, não apenas um valor.

        attribute_name = request.json['attribute_name']
        new_value = request.json['new_value']
        new_value_name = adminPreferences_service.get_enum_name_by_value(new_value)
        
        if new_value_name is None:
            return {"message": "Valor inválido"}, 400
        else:
            adminPreferences_service.update_adminPreferencesPerPage(adminPreferences, attribute_name, new_value_name)  # passar a instância completa aqui também
            return {"message": "Valor atualizado com sucesso"}, 200


class ListPerpage(Resource):
    @admin_required
    def post(self):
        attribute_name = request.json['attribute_name']
        listEnum = adminPreferences_service.listPerpage(attribute_name)
        if listEnum:
            return make_response(jsonify(listEnum), 200)
        else:
            return make_response(jsonify({"message": "Atributo não encontrado"}), 400)


api.add_resource(CreateAdminPreferences, '/adminPreferences/create')
api.add_resource(UpdateAdminPreferences, '/adminPreferences/update')
api.add_resource(ListPerpage, '/axiosadmin/adminPreferences/selectPerPage')
api.add_resource(UpdatePreferencePerPageAdmin, '/axiosadmin/adminPreferences/updatePerPage')
