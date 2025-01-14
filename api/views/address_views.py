from flask_restful import Resource
from api import api
from ..schemas import address_schema
from flask import request, make_response, jsonify
from ..entities import address
from ..services import address_service, user_service
from ..schemas .validators import validator
import pycep_correios
from pycep_correios.exceptions import InvalidCEP, CEPNotFound
from flask_jwt_extended import jwt_required, get_jwt_identity



class RegisterAddress(Resource):
     @jwt_required()  
     def post(self):
        current_user = get_jwt_identity()
        checkToken = user_service.get_user(current_user)
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
            tokenUser = checkToken

        if "complement" in request.json:
            complement = request.json['complement']
            validateComplament = validator.validate_name(complement)
            if validateComplament is not True:
                verify = False
                errorTypes['complement'] = 'Invalid complement.'
        else:
            complement = None

        
        if len(neighborhood) > 100:
            verify = False
            errorTypes['neighborhood'] = 'Field contains more than 100 characters.'
        
        if len(street) > 100:
            verify = False
            errorTypes['street'] = 'Field contains more than 100 characters.'

        
        if not zipCode.isnumeric() or len(zipCode) != 8:
            verify = False
            errorTypes['zipCode'] = 'Invalid zipcode'

        if verify == True:
            try:
                addressFind = pycep_correios.get_address_from_cep(zipCode)
            except CEPNotFound as exc:
                verify = False
                errorTypes['zipCode'] = 'Invalid zipcode'

        if number.isdecimal() is not True:
            verify = False
            errorTypes['number'] = 'Invalid date.'
        
        if state.isalpha() is not True or len(state) > 2:
            verify = False
            errorTypes['state'] = 'Invalid date'
        
        
        if activate != "1" and activate != "2" or activate.isdecimal() is not True:
            verify = False
            errorTypes['activate'] = 'Invalid status.'
            

        if verify == True:
            new_address = address.Address(neighborhood=neighborhood, street=street, number=number, state=state, city=city, zipCode=zipCode, activate=activate, tokenUser=tokenUser, complement=complement)
            result = address_service.address_register(new_address)
            ref = cs.jsonify(result)
            return make_response(ref, 201)
        else:
            return make_response(jsonify(errorTypes), 404)


class ListAdresses(Resource):
    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        checkToken = user_service.get_user(current_user)
        userAddress = address_service.user_address(checkToken)
        if userAddress is None or userAddress == []:
            return make_response(jsonify("No registered address."), 200)
        return make_response(jsonify(userAddress), 200)


class UpdateAddress(Resource):
     @jwt_required()
     def put(self, id):
        errorTypes = {}
        verify = True
        current_user = get_jwt_identity()
        checkToken = user_service.get_user(current_user)
        address_bd = address_service.user_search_address_by_id(id, checkToken)
        if address_bd is None or address_bd is False:
            return make_response(jsonify("Address not fount."), 404)
        ads = address_schema.AddressSchema()
        validate = ads.validate(request.json)
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
            tokenUser = checkToken


        if "complement" in request.json:
            complement = request.json['complement']
            validateComplament = validator.validate_name(complement)
            if validateComplament is not True:
                verify = False
                errorTypes['complement'] = 'Invalid complement.'
        else:
            complement = None

       
        if not zipCode.isnumeric() or len(zipCode) != 8:
            verify = False
            errorTypes['zipCode'] = 'Invalid zipcode'

        if verify == True:
            try:
                addressFind = pycep_correios.get_address_from_cep(zipCode)
            except CEPNotFound as exc:
                verify = False
                errorTypes['zipCode'] = 'Invalid zipcode'

        if number.isdecimal() is not True:
            verify = False
            errorTypes['number'] = 'Invalid date.'
        
        if state.isalpha() is not True or len(state) > 2:
            verify = False
            errorTypes['state'] = 'Invalid date.'
        
        
        if activate != "1" and activate != "2" or activate.isdecimal() is not True:
            verify = False
            errorTypes['activate'] = 'Invalid status.'

        if verify == True:
            new_address = address.Address(neighborhood=neighborhood, street=street, number=number, state=state, city=city, zipCode=zipCode, activate=activate, tokenUser=tokenUser, complement=complement)
            address_service.address_update(address_bd, new_address)
            msgm = 'Address updated successfully.'
            return make_response(jsonify(msgm), 201)
        else:
            return make_response(jsonify(errorTypes), 404)
     

class DeleteAddress(Resource):
    @jwt_required()
    def delete(self, id):
        current_user = get_jwt_identity()
        checkToken = user_service.get_user(current_user)
        address_db = address_service.user_search_address_by_id(id, checkToken)
        if address_db is None or address_db == False:
            return make_response(jsonify("Address not found."), 404)
        address_service.delete_address(address_db)
        return make_response(jsonify("Address deleted successfully."), 204)



api.add_resource(RegisterAddress, '/address_register')

api.add_resource(UpdateAddress, '/address_update/<int:id>')

api.add_resource(ListAdresses, '/my_adresses')

api.add_resource(DeleteAddress, '/address_delete/<int:id>')