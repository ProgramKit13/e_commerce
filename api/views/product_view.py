from flask_restful import Resource
from api import api
from ..schemas import prod_schema
from flask import request, make_response, jsonify
from ..entities import product
from ..services import product_service
import secrets

class ShowAllProds(Resource):
    def get(self):
        prods = product_service.product_list()
        ps = prod_schema.ProdSchema(many=True)
        return make_response(ps.jsonify(prods), 200)



class ProdRegister(Resource):
    def get(self):
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
            token = secrets.token_hex(32)


        if type(valueResale) != float:
            verify = False
            errorTypes['valueResale'] = 'Formato inválido.'
        
        if type(cust) != float:
            verify = False
            errorTypes['cust'] = 'Formato inválido.'
        
        if type(tax) != float:
            verify = False
            errorTypes['tax'] = 'Formato inválido.'
        
        if type(alterResale) != float:
            verify = False
            errorTypes['alterResale'] = 'Formato inválido.'

        if type(qt) != int:
            verify = False
            errorTypes['qt'] = 'Formato inválido.'

        
        if verify:
            new_prod = product.Product(prodName=prodName, valueResale=valueResale, cust=cust, tax=tax, supplier=supplier, qt=qt, alterResale=alterResale, token=token)
            result = product_service.prod_register(new_prod)
            ref = ps.jsonify(result)
            return make_response(ref, 201)
        else:
            return make_response(jsonify(errorTypes), 404)
    
    

class ProdSearchId(Resource):
    def get(self, id):
        product = product_service.product_list_id(id)
        if product is None:
            return make_response(jsonify("Produto não encontrado"), 404)
        ps = prod_schema.ProdSchema()
        return make_response(ps.jsonify(product), 200)

class updateProduct(Resource):
    def put(self, id):
        product_db = product_service.product_list_id(id)
        if product_db is None:
            return make_response(jsonify("Produto não encontrado"), 404)
        ps = prod_schema.ProdSchema()
        validate = ps.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 404)
        else:
            prodName = request.json["prodName"]
            valueResale = request.json["valueResale"]
            cust = request.json["cust"]
            tax = request.json["tax"]
            supplier = request.json["supplier"]
            qt = request.json["qt"]
            alerResale = request.json["alterResale"]



            upgrade_product = product.UpdateProduct(prodName=prodName, valueResale=valueResale, cust=cust, tax=tax, supplier=supplier, qt=qt, alterResale=alerResale)
            product_service.product_update(product_db, upgrade_product)
            response = product_service.product_list_id(id)
            return make_response(ps.jsonify(response), 200)


class deleteProduct(Resource):
    def delete(self, id):
        product_db = product_service.product_list_id(id)
        if product_db is None:
            return make_response(jsonify("Produto não encontrado"), 404)
        product_service.product_delete(product_db)
        return make_response(jsonify("Produto excluído com sucesso!"), 204)


api.add_resource(ShowAllProds, '/product&list')
api.add_resource(ProdRegister, '/product&register')
api.add_resource(ProdSearchId, '/product&search/<int:id>')
api.add_resource(updateProduct, '/product&update/<int:id>')
api.add_resource(deleteProduct, '/product&delete/<int:id>')