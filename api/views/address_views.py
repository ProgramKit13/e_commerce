from flask_restful import Resource
from api import api
from ..schemas import address_schema
from flask import request, make_response, jsonify
from ..entities import address
from ..services import address_service
from ..schemas .validators import validator
import pycep_correios
from pycep_correios.exceptions import InvalidCEP

class RegisterAddress(Resource):
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
            idUser = request.json["idUser"]

        if len(zipCode) == 9:
            try:
                addressFind = pycep_correios.get_address_from_cep(zipCode)
            except InvalidCEP as exc:
                verify = False
                errorTypes['zipCode'] = 'Cep Inválido'
        else :
            verify = False
            errorTypes['zipCode'] = 'CEP inválido.'

        if number.isdecimal() is not True:
            verify = False
            errorTypes['number'] = 'Número inválido.'
        
        if state.isalpha() is not True or len(state) > 2:
            verify = False
            errorTypes['state'] = 'Estado inválido.'
        
        
        if activate != "1" and activate != "2" or activate.isdecimal() is not True:
            verify = False
            errorTypes['activate'] = 'Status inválido.'
            

        if verify == True:
            new_address = address.Address(neighborhood=neighborhood, street=street, number=number, state=state, city=city, zipCode=zipCode, activate=activate, idUser=idUser)
            result = address_service.address_register(new_address)
            ref = cs.jsonify(result)
            return make_response(ref, 201)
        else:
            return make_response(jsonify(errorTypes), 404)


class ListAdresses(Resource):
    def get(self, id):
        adressesListAll = address_service.adressesList(id)
        if adressesListAll is None or adressesListAll == []:
            return make_response(jsonify("Sem endereço cadastrado"), 200)
        return make_response(jsonify(adressesListAll), 200)



class updateAddress(Resource):
     def put(self, id):
        address_bd = address_service.address_list_id(id)
        if address_bd is None:
            return make_response(jsonify("Endreço não encontrado"), 404)
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
            idUser = request.json["idUser"]
            new_address = address.Address(neighborhood=neighborhood, street=street, number=number, state=state, city=city, zipCode=zipCode, activate=activate, idUser=idUser)
        
        address_service.address_update(address_bd, new_address)
        msgm = 'Endereço atualizado com sucesso.'
        return msgm
     
class deleteAddress(Resource):
    def delete(self, id):
        address_db = address_service.address_list_id(id)
        if address_db is None:
            return make_response(jsonify("Endereço não encontrado"), 404)
        address_service.address_delete(address_db)
        return make_response(jsonify("Endreço excluído com sucesso!"), 204)

api.add_resource(RegisterAddress, '/address&register')
api.add_resource(updateAddress, '/update&address/<int:id>')
api.add_resource(ListAdresses, '/search&adresses/<int:id>')
api.add_resource(deleteAddress, '/delete&address/<int:id>')