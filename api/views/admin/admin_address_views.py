from flask_restful import Resource
from api import api
from ...schemas import address_schema
from flask import request, make_response, jsonify
from ...entities import address
from ...services import address_service
from ...schemas .validators import validator
import pycep_correios
from pycep_correios.exceptions import InvalidCEP
from ...decorators import admin_required


##Register
class AdminRegisterAdresses(Resource):  
     @admin_required
     def post(self):
        verify = True
        errorTypes = {}
        cs = address_schema.AddressSchema()
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            neighborhood = request.json['neighborhood']
            street = request.json["street"]
            number = request.json["number"]
            state= request.json["state"]
            city = request.json['city']
            zipCode = request.json["zipCode"]
            activate = request.json["activate"]
            tokenUser = request.json["tokenUser"]

        if len(neighborhood) > 100:
            verify = False
            errorTypes['neighborhood'] = 'Field contains more than 100 characters.'
        
        if len(street) > 100:
            verify = False
            errorTypes['street'] = 'Field contains more than 100 characters.'

        
        if type(number) != int:
            verify = False
            errorTypes['Invalid field.']
        
        if len(zipCode) == 9:
            try:
                addressFind = pycep_correios.get_address_from_cep(zipCode)
            except InvalidCEP as exc:
                verify = False
                errorTypes['zipCode'] = 'Invalid field'
        else :
            verify = False
            errorTypes['zipCode'] = 'Invalid field.'

        
        if state.isalpha() is not True or len(state) > 2:
            verify = False
            errorTypes['state'] = 'Invalid field.'
        
        
        if activate != "1" and activate != "2" or activate.isdecimal() is not True:
            verify = False
            errorTypes['activate'] = 'Invalid field.'
            

        if verify == True:
            new_address = address.Address(neighborhood=neighborhood, street=street, number=number, state=state, city=city, zipCode=zipCode, activate=activate, tokenUser=tokenUser)
            result = address_service.address_register(new_address)
            ref = cs.jsonify(result)
            return make_response(ref, 201)
        else:
            return make_response(jsonify(errorTypes), 404)
#################################################


##List
class AdminListAdresses(Resource):
     @admin_required
     def get(self):
        users = address_service.adresses_list()
        cs = address_schema.AddressSchema(many=True)
        return make_response(cs.jsonify(users), 200)
#################################################


##Update
class AdminUpdateAdresses(Resource):
     def put(self, id):
        address_bd = address_service.search_address_by_id(id)
        if address_bd is None:
            return make_response(jsonify("Endreço não encontrado"), 404)
        ads = address_schema.AddressSchema()
        validate = ads.validate(request.json)
        verify = True
        errorTypes = {}
        if validate:
            return make_response(jsonify(validate), 404)
        else:
            neighborhood = request.json["neighborhood"]
            street = request.json["street"]
            number = request.json["number"]
            state= request.json["state"]
            city = request.json["city"]
            zipCode = request.json["zipCode"]
            activate = request.json["activate"]
            tokenUser = address_bd.tokenUser
        
        if len(neighborhood) > 100:
            verify = False
            errorTypes['neighborhood'] = 'Field contains more than 100 characters.'
        
        if len(street) > 100:
            verify = False
            errorTypes['street'] = 'Field contains more than 100 characters.'

        
        if type(number) != int:
            verify = False
            errorTypes['Invalid field.']
        
        if len(zipCode) == 9:
            try:
                addressFind = pycep_correios.get_address_from_cep(zipCode)
            except InvalidCEP as exc:
                verify = False
                errorTypes['zipCode'] = 'Invalid field'
        else :
            verify = False
            errorTypes['zipCode'] = 'Invalid field.'

        
        if state.isalpha() is not True or len(state) > 2:
            verify = False
            errorTypes['state'] = 'Invalid field.'
        
        
        if activate != "1" and activate != "2" or activate.isdecimal() is not True:
            verify = False
            errorTypes['activate'] = 'Invalid field.'

        if verify == True:
            new_address = address.Address(neighborhood=neighborhood, street=street, number=number, state=state, city=city, zipCode=zipCode, activate=activate, tokenUser=tokenUser)
            address_service.address_update(address_bd, new_address)
            msgm = 'Address updated successfully.'
            return msgm
        else:
            return make_response(jsonify(errorTypes), 404)
#################################################


##Delete
class AdminDeleteAdresses(Resource):
    @admin_required
    def delete(self, id):
        address_db = address_service.search_address_by_id(id)
        if address_db is None:
            return make_response(jsonify("Address not found"), 404)
        address_service.delete_address(address_db)
        return make_response(jsonify("Address deleted successfully!"), 204)
################################################



api.add_resource(AdminRegisterAdresses, '/admin&dashboard/address&register')

api.add_resource(AdminUpdateAdresses, '/admin&dashboard/update&address/<int:id>')

api.add_resource(AdminListAdresses, '/admin&dashboard/list&adresses')

api.add_resource(AdminDeleteAdresses, '/admin&dashboard/delete&address/<int:id>')