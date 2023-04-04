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

        
        if "complement" in request.json:
            complement = request.json['complement']
            complementValidate = validator.validate_text(complement)
            if complementValidate != True:
                verify = False
                errorTypes['complement'] = complementValidate
        else:
            complement = None
        
        neighborhoodValidate = validator.validate_text(request.json['neighborhood'])
        if neighborhoodValidate != True:
            verify = False
            errorTypes['neighborhood'] = neighborhoodValidate
        
        streetValidate = validator.validate_text(street)
        if streetValidate != True:
            verify = False
            errorTypes['street'] = streetValidate
       
        cityValidate = validator.validate_text(city)
        if cityValidate != True:
            verify = False
            errorTypes['city'] = cityValidate
    
       
        # try:
        #     addressFind = pycep_correios.get_address_from_cep(zipCode)
        # except CEPNotFound as exc:
        #         verify = False
        #         errorTypes['zipCode'] = 'Invalid zipcode'
        

        if state.isalpha() is not True or len(state) > 2:
            verify = False
            errorTypes['state'] = 'Invalid field.'
            

        if verify == True:
            new_address = address.Address(neighborhood=neighborhood, street=street, number=number, state=state, city=city, zipCode=zipCode, activate=activate, tokenUser=tokenUser, complement=complement)
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
            return make_response(jsonify("Address not found."), 404)
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
        
        if "complement" in request.json:
            complement = request.json['complement']
            complementValidate = validator.validate_text(complement)
            if complementValidate != True:
                verify = False
                errorTypes['complement'] = complementValidate
        else:
            complement = None
        
        neighborhoodValidate = validator.validate_text(request.json['neighborhood'])
        if neighborhoodValidate != True:
            verify = False
            errorTypes['neighborhood'] = neighborhoodValidate
        
        streetValidate = validator.validate_text(street)
        if streetValidate != True:
            verify = False
            errorTypes['street'] = streetValidate
       
        cityValidate = validator.validate_text(city)
        if cityValidate != True:
            verify = False
            errorTypes['city'] = cityValidate
    
       
        # try:
        #     addressFind = pycep_correios.get_address_from_cep(zipCode)
        # except CEPNotFound as exc:
        #         verify = False
        #         errorTypes['zipCode'] = 'Invalid zipcode'
        

        if state.isalpha() is not True or len(state) > 2:
            verify = False
            errorTypes['state'] = 'Invalid field.'

        if verify == True:
            new_address = address.Address(neighborhood=neighborhood, street=street, number=number, state=state, city=city, zipCode=zipCode, activate=activate, tokenUser=tokenUser, complement=complement)
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



api.add_resource(AdminRegisterAdresses, '/admin_dashboard/address_register')

api.add_resource(AdminUpdateAdresses, '/admin_dashboard/address_update/<int:id>')

api.add_resource(AdminListAdresses, '/admin_dashboard/adresses_list')

api.add_resource(AdminDeleteAdresses, '/admin_dashboard/address_delete/<int:id>')