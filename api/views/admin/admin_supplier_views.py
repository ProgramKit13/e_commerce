from flask_restful import Resource
from api import api
from ...schemas import supplier_schema
from flask import request, make_response, jsonify
from ...entities import supplier
from ...services import supplier_service
from ...schemas.validators import validator
import secrets
from validate_docbr import CNPJ
from ...decorators import admin_required
import pycep_correios
from pycep_correios.exceptions import CEPNotFound, InvalidCEP


###Register
class AdminRegisterSupplier(Resource):
     def post(self):
        verify = True
        errorTypes = {}
        cs = supplier_schema.Supplier_Schema()
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            name = request.json['name']
            email = request.json['email']
            state = request.json["state"]
            city = request.json["city"]
            neighborhood = request.json["neighborhood"]
            street = request.json["street"]
            number = request.json['number']
            zipCode = request.json['zipCode']
            cnpj = request.json['cnpj']
            token = secrets.token_hex(6)

        if len(name) <= 3 or name.isalpha() == False:
            verify = False
            errorTypes['name'] = 'Invalid format.'

        validateEmail = validator.email_validate(email)
        if validateEmail is not True:
            verify = False
            errorTypes['email'] = 'Invalid email.'
        
        validateCNPJ = CNPJ()
        cnpjValidate = validateCNPJ.validate(cnpj)
        if cnpjValidate == False:
            verify = False
            errorTypes['cnpj'] = 'Invalid cnpj.'
            
        if "phone" in request.json:
            phone = request.json['phone']
        else:
            phone = None

        if "complement" in request.json:
            complement = request.json['complement']
        else:
            complement = None

        if len(neighborhood) > 100:
            verify = False
            errorTypes['neighborhood'] = 'Field contains more than 100 characters.'
        
        if len(street) > 100:
            verify = False
            errorTypes['street'] = 'Field contains more than 100 characters.'

        if len(city) > 100:
            verify = False
            errorTypes['city'] = 'Field contains more than 100 characters.'
    
       
        # try:
        #     addressFind = pycep_correios.get_address_from_cep(zipCode)
        # except CEPNotFound as exc:
        #         verify = False
        #         errorTypes['zipCode'] = 'Invalid zipcode'
        

        if state.isalpha() is not True or len(state) > 2:
            verify = False
            errorTypes['state'] = 'Invalid field.'
     
        if verify:
            new_supplier = supplier.Supplier(name=name, email=email, state=state, city=city, neighborhood=neighborhood, street=street, number=number, complement=complement, zipCode=zipCode, cnpj=cnpj, phone=phone, token=token)
            result = supplier_service.supplier_register(new_supplier)
            ref = cs.jsonify(result)
            return make_response(ref, 201)
        else:
            return make_response(jsonify(errorTypes), 404)
##############################

###List
class AdminShowSuppliers(Resource):
    @admin_required
    def get(self):
        suppliers = supplier_service.supplier_list()
        ss = supplier_schema.Supplier_Schema(many=True)
        return make_response(ss.jsonify(suppliers), 200)
###############################



class AdminSupplierSearchId(Resource):
  
    def get(self, id):
        supplier = supplier_service.supplier_id(id)
        if supplier is None:
            return make_response(jsonify("Supplier not found"), 404)
        ps = supplier_schema.Supplier_Schema()
        return make_response(ps.jsonify(supplier), 200)





api.add_resource(AdminRegisterSupplier, '/admin_dashboard/supplier_register')

api.add_resource(AdminShowSuppliers, '/admin_dashboard/suppliers_list')

api.add_resource(AdminSupplierSearchId, '/admin_dashboard/supplier%<int:id>')
