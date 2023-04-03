from flask_restful import Resource
from api import api
from ...schemas import prod_schema
from flask import request, make_response, jsonify
from ...entities import product
from ...services import product_service
import secrets
from ...decorators import admin_required


##Product Register
class AdminProdRegister(Resource):
    @admin_required
    def post(self):
        errorTypes = {}
        verify = True 
        ps = prod_schema.ProdSchema()
        validate = ps.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            prodName = request.json['prodName']
            valueResale = request.json['valueResale']
            cust = request.json['cust']
            tax = request.json['tax']
            supplier = request.json['supplier']
            qt = request.json['qt']
            alterResale = request.json['alterResale']
            discount = request.json['discount']
            description = request.json['description']
            datePurchase = request.json['datePurchase']
            dateShelf = request.json['dateShelf']
            token = secrets.token_hex(6)

        if type(valueResale) != float:
            verify = False
            errorTypes['valueResale'] = 'Invalid format.'
        
        if type(cust) != float:
            verify = False
            errorTypes['cust'] = 'Invalid format.'
        
        if tax:
            if type(tax) != float:
                verify = False
                errorTypes['tax'] = 'Invalid format.'
        
        if alterResale:
            if type(alterResale) != float:
                verify = False
                errorTypes['alterResale'] = 'Invalid format.'

        if discount:
            if type(discount) != float:
                verify = False
                errorTypes['discount'] = 'Invalid format.'
        
        if description:
            if len(description) > 1024:
                verify = False
                errorTypes['text'] = 'Number of characters exceeds the allowed.'

        if type(qt) != int:
            verify = False
            errorTypes['qt'] = 'Invalid format.'

        
        if verify:
            new_prod = product.Product(prodName=prodName, valueResale=valueResale, cust=cust, tax=tax, supplier=supplier, qt=qt, alterResale=alterResale, discount=discount, description=description, datePurchase=datePurchase, dateShelf=dateShelf, token=token)
            result = product_service.prod_register(new_prod)
            ref = ps.jsonify(result)
            return make_response(ref, 201)
        else:
            return make_response(jsonify(errorTypes), 404)
###############################################

##List
class AdminShowProducts(Resource):
    @admin_required
    def get(self):
        prods = product_service.product_list()
        ps = prod_schema.ProdSchema(many=True)
        return make_response(ps.jsonify(prods), 200)

  
##Search       
class AdminProdSearchId(Resource):
    @admin_required
    def get(self, id):
        product = product_service.product_list_id(id)
        if product is None:
            return make_response(jsonify("Product not found"), 404)
        ps = prod_schema.ProdSchema()
        return make_response(ps.jsonify(product), 200)

class AdminProdSearchFilter(Resource):
    @admin_required
    def post(self):
        if 'prodName' in request.json:
            name = request.json['prodName']
            list_filter = product_service.AdminsearchProduct(name)
            if list_filter == []:
                return make_response(jsonify('Product not found'), 404)
            return make_response(jsonify(list_filter), 201)
        
 
##Update
class AdminUpdateProd(Resource):
    @admin_required
    def put(self, id):
        product_db = product_service.product_list_id(id)
        verify = True
        errorTypes = {}
        if product_db is None:
            return make_response(jsonify("Product not fount."), 404)
        ps = prod_schema.ProdSchema()
        validate = ps.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 404)
        else:
            prodName = request.json['prodName']
            valueResale = request.json['valueResale']
            cust = request.json['cust']
            tax = request.json['tax']
            supplier = request.json['supplier']
            qt = request.json['qt']
            alterResale = request.json['alterResale']
            discount = request.json['discount']
            description = request.json['description']
            datePurchase = request.json['datePurchase']
            dateShelf = request.json['dateShelf']
            token = product_db.token

        if type(valueResale) != float:
            verify = False
            errorTypes['valueResale'] = 'Invalid format.'
        
        if type(cust) != float:
            verify = False
            errorTypes['cust'] = 'Invalid format.'
        
        if tax:
            if type(tax) != float:
                verify = False
                errorTypes['tax'] = 'Invalid format.'
        
        if alterResale:
            if type(alterResale) != float:
                verify = False
                errorTypes['alterResale'] = 'Invalid format.'

        if discount:
            if type(discount) != float:
                verify = False
                errorTypes['discount'] = 'Invalid format.'
        
        if description:
            if len(description) > 1024:
                verify = False
                errorTypes['text'] = 'Number of characters exceeds the allowed.'

        if type(qt) != int:
            verify = False
            errorTypes['qt'] = 'Invalid format.'

        
        if verify:
            upgrade_product = product.Product(prodName=prodName, valueResale=valueResale, cust=cust, tax=tax, supplier=supplier, qt=qt, alterResale=alterResale, discount=discount, description=description, datePurchase=datePurchase, dateShelf=dateShelf, token=token)
            product_service.product_update(product_db, upgrade_product)
            response = product_service.product_list_id(id)
            return make_response(ps.jsonify(response), 200)
        else:
            return make_response(jsonify(errorTypes), 404)


##Delete
class AdminDeleteProd(Resource):
    @admin_required
    def delete(self, id):
        product_db = product_service.product_list_id(id)
        if product_db is None:
            return make_response(jsonify("Product not found"), 404)
        product_service.product_delete(product_db)
        return make_response(jsonify("Product deleted successfully."), 204)


api.add_resource(AdminShowProducts, '/admin_dashboard/product_list')

api.add_resource(AdminProdRegister, '/admin_dashboard/product_register')

api.add_resource(AdminProdSearchId, '/admin_dashboard/product_search/<int:id>')

api.add_resource(AdminProdSearchFilter, '/admin_dashboard/product_searchByFilter')

api.add_resource(AdminUpdateProd, '/admin_dashboard/product_update/<int:id>')

api.add_resource(AdminDeleteProd, '/admin_dashboard/product_delete/<int:id>')