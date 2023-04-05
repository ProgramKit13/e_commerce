from flask_restful import Resource
from api import api
from flask import request, make_response, jsonify
from ..schemas .validators import validator
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..services import user_service, product_service, cart_service, order_service
from ..schemas import carts_schema, product_schema,  user_schema, order_schema
import secrets

class OpenCart(Resource):
    @jwt_required()
    def post(self):
        verify = True
        errorTypes = {}
        current_user = get_jwt_identity()
        checkToken = user_service.get_user(current_user)
        tokenUser = checkToken
        if tokenUser is None:
            return make_response(jsonify({"message": "User not found"}), 404)
        else:
            cart = cart_service.get_cart_by_token_and_status(tokenUser)
            if cart is None:
                tokenCart = secrets.token_hex(64)
                tokenOrder = secrets.token_hex(64)
                value = request.json['value']
                amount = request.json['amount']
                discount = request.json['discount']
                tokenProduct = request.json['tokenProduct']

                getProductByToken = product_service.product_list_token(tokenProduct)

                if getProductByToken is None:
                    verify = False
                    errorTypes['amount'] = 'Product not found.'
                
                if getProductByToken.qt < amount:
                    verify = False
                    errorTypes['amount'] = 'Amount not available.'

                if "discount" in request.json:
                    discount = request.json['discount']
                    if discount != getProductByToken.discount:
                        verify = False
                        errorTypes['discount'] = 'Discount not available.'
                    if discount > value:
                        verify = False
                        errorTypes['discount'] = 'Discount not available.'

                if value != getProductByToken.valueResale:
                    verify = False
                    errorTypes['value'] = 'Value not available.'
                


                if verify:
                    new_cart = cart_service.create_cart(tokenUser, tokenCart)

                    new_order = order_service.create_order(tokenProduct=tokenProduct, tokenUser=tokenUser, tokenCart=tokenCart, token=tokenOrder, qt=amount, discount=discount, value=value)

                    return make_response(jsonify(new_order, new_cart), 201)
                else:
                    return make_response(jsonify(errorTypes), 400)
            else:
                return make_response(jsonify({"message": "Cart already open"}), 400)