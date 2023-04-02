from flask_restful import Resource
from api import api
from ..schemas import prod_schema
from flask import request, make_response, jsonify
from ..entities import product
from ..services import product_service

class ShowAllProds(Resource):
    def get(self):
        prods = product_service.product_list()
        ps = prod_schema.ProdSchema(many=True)
        return make_response(ps.jsonify(prods), 200)
    
class ProdSearchId(Resource):
    def get(self, id):
        product = product_service.product_list_id(id)
        if product is None:
            return make_response(jsonify("Produto não encontrado"), 404)
        ps = prod_schema.ProdSchema()
        return make_response(ps.jsonify(product), 200)

class ProdSearchFilter(Resource):
    def post(self):
        errorTypes = {}
        verify = True
        filterApply = []
        if 'prodName' in request.json:
            name = request.json['prodName']
            teste = product_service.searchProdName(name)
            return make_response(jsonify(teste))
      

api.add_resource(ShowAllProds, '/product_list')
api.add_resource(ProdSearchId, '/product_search/<int:id>')
api.add_resource(ProdSearchFilter, '/product_search_by_filter/<int:id>')