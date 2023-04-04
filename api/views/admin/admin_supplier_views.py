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

        
        validateName = validator.validate_name(name)
        if validateName is not True:
            verify = False
            errorTypes['name'] = validateName

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

###Search  
class AdminSupplierSearchId(Resource):
    @admin_required
    def get(self, id):
        supplier = supplier_service.supplier_id(id)
        if supplier is None:
            return make_response(jsonify("Supplier not found"), 404)
        ps = supplier_schema.Supplier_Schema()
        return make_response(ps.jsonify(supplier), 200)
###############################

###Update
class AdminUpdateSupplier(Resource):
 
    def put(self, id):
        verify = True
        errorTypes = {}
        supplier_bd = supplier_service.supplier_id(id)
        if supplier_bd is None:
            return make_response(jsonify("Supplier not found"), 404)
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
            token = supplier_bd.token

        validateName = validator.validate_name(name)
        if validateName is not True:
            verify = False
            errorTypes['name'] = validateName

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
            new_supplier = supplier.Supplier(name=name, email=email, state=state, city=city, neighborhood=neighborhood, street=street, number=number, complement=complement, zipCode=zipCode, cnpj=cnpj, phone=phone, token=token)
            result = supplier_service.supplier_update(supplier_bd,new_supplier)
            ref = cs.jsonify(result)
            return make_response(ref, 201)
        else:
            return make_response(jsonify(errorTypes), 404)


class AdminSupplierSearchId(Resource):
  
    def get(self, id):
        supplier = supplier_service.supplier_id(id)
        if supplier is None:
            return make_response(jsonify("Supplier not found"), 404)
        ps = supplier_schema.Supplier_Schema()
        return make_response(ps.jsonify(supplier), 200)
    

class AdminDeleteSupplier(Resource):
    @admin_required
    def delete(self, id):
        supplier = supplier_service.supplier_id(id)
        if supplier is None:
            return make_response(jsonify("Supplier not found"), 404)
        supplier_service.supplier_delete(supplier)
        return make_response(jsonify("Supplier deleted"), 200)





api.add_resource(AdminRegisterSupplier, '/admin_dashboard/supplier_register')

api.add_resource(AdminShowSuppliers, '/admin_dashboard/suppliers_list')

api.add_resource(AdminSupplierSearchId, '/admin_dashboard/supplier%<int:id>')

api.add_resource(AdminUpdateSupplier, '/admin_dashboard/supplier_update%<int:id>')

api.add_resource(AdminDeleteSupplier, '/admin_dashboard/supplier_delete%<int:id>')


