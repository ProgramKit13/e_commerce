from flask_restful import Resource
from api import api
from ..schemas import prod_schema
from flask import request, make_response, jsonify
from ..services import product_service
from ..schemas.validators import validator

class ShowAllProds(Resource):
    def get(self):
        prods = product_service.product_list()
        ps = prod_schema.ProdSchema(many=True)
        return make_response(ps.jsonify(prods), 200)
    
class ProdSearchId(Resource):
    def get(self, id):
        product = product_service.product_list_id(id)
        if product is None:
            return make_response(jsonify("Product not found."), 404)
        ps = prod_schema.ProdSchema()
        return make_response(ps.jsonify(product), 200)

class ProdSearchFilter(Resource):
    def post(self):
        if 'search_field' in request.json:
            name = request.json['search_field']
            validateSearch = validator.validate_name(name)
            if validateSearch is not True:
                return make_response(jsonify(validateSearch), 404)
            else:    
                list_filter = product_service.searchProduct(name)
                if list_filter == []:
                    return(make_response(jsonify('Product not found.'), 404))
                else:
                    return make_response(jsonify(list_filter), 201)
        else:
            return make_response(jsonify('Search field not found.'), 404)
        

api.add_resource(ShowAllProds, '/product_list')
api.add_resource(ProdSearchId, '/product_search/<int:id>')
api.add_resource(ProdSearchFilter, '/product_search_by_filter')