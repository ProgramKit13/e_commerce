from flask_restful import Resource
from api import api
from ...schemas import supplier_schema
from flask import request, make_response, jsonify, current_app
from ...entities import supplier
from ...models.supplier_model import Supplier
from ...services import supplier_service, adminPreferences_service, user_service
from ...schemas.validators import validator
import secrets
from validate_docbr import CNPJ
from ...decorators import admin_required
from flask_jwt_extended import get_jwt_identity
from pycep_correios.exceptions import CEPNotFound, InvalidCEP
from .advancedfilter import paginate_advanced

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
            name = request.json['supplierName']
            email = request.json['supplierEmail']
            state = request.json["supplierState"]
            city = request.json["supplierCity"]
            neighborhood = request.json["supplierNeighborhood"]
            street = request.json["supplierStreet"]
            number = request.json['supplierNumber']
            zipCode = request.json['supplierZipCode']
            cnpj = request.json['supplierCnpj']
            phone_01 = request.json['supplierPhone_01']
            phone_02 = request.json['supplierPhone_02']
            token = secrets.token_hex(6)

        
        validateName = validator.validateGlobalText(name, True, False, 3, 100)
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
            

        if "complement" in request.json:
            complement = request.json['complement']
            complementValidate = validator.validate_text(complement)
            if complementValidate != True:
                verify = False
                errorTypes['complement'] = complementValidate
        else:
            complement = None
        
        neighborhoodValidate = validator.validateGlobalText(neighborhood, True, False, 3, 100)
        if neighborhoodValidate != True:
            verify = False
            errorTypes['neighborhood'] = neighborhoodValidate
        
        streetValidate = validator.validateGlobalText(street, True, False, 3, 100)
        if streetValidate != True:
            verify = False
            errorTypes['street'] = streetValidate
       
        cityValidate = validator.validateGlobalText(city, True, False, 3, 100)
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
            new_supplier = supplier.Supplier(supplierName=name, supplierEmail=email, supplierState=state, supplierCity=city, supplierNeighborhood=neighborhood, supplierStreet=street, supplierNumber=number, supplierComplement=complement, supplierZipCode=zipCode, supplierCnpj=cnpj, token=token, supplierPhone_01=phone_01, supplierPhone_02=phone_02)
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
    


class GetAllandSearchSupplier(Resource):
    @admin_required
    def get(self):
        try:
            current_user = get_jwt_identity()
            user = user_service.get_user(current_user)
            preferencesPerPageSup = adminPreferences_service.get_adminPreferencesPerpage_by_token(user)
            ps = supplier_schema.Supplier_Schema(many=True)
            filters = request.args.to_dict() 
            if 'per_page' in filters and filters['per_page'] != 'undefined':
                per_page = int(filters.pop('per_page'))
            else:
                per_page = preferencesPerPageSup.suppliersPerPage.value
            infoPaginate = paginate_advanced(Supplier, ps, per_page, **filters)
        except Exception as e:
            current_app.logger.error(f"Error while searching for suppliers: {type(e).__name__} {e}")
            return make_response(jsonify('Error while searching for suppliers'), 500)

        if not infoPaginate['list']:
            return make_response(jsonify('Not supplier registred'), 202)

        return make_response(jsonify(infoPaginate), 200)
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
            name = request.json['supplierName']
            email = request.json['supplierEmail']
            state = request.json["supplierState"]
            city = request.json["supplierCity"]
            neighborhood = request.json["supplierNeighborhood"]
            street = request.json["supplierStreet"]
            number = request.json['supplierNumber']
            zipCode = request.json['supplierZipCode']
            cnpj = request.json['supplierCnpj']
            phone1 = request.json['supplierPhone01']
            phone2 = request.json['supplierPhone02']
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
            new_supplier = supplier.Supplier(supplierName=name, supplierEmail=email, supplierState=state, supplierCity=city, supplierNeighborhood=neighborhood, supplierStreet=street, supplierNumber=number, supplierComplement=complement, supplierZipCode=zipCode, supplierCNPJ=cnpj, supplierPhone1=phone1, supplierPhone2=phone2, supplierPhone=phone, token=token)
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

api.add_resource(GetAllandSearchSupplier, '/axiosadmin/gestao/fornecedores')


