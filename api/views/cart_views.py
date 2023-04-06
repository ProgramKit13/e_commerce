from flask_restful import Resource
from api import api
from flask import request, make_response, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..services import user_service, product_service, cart_service, order_service
import secrets

class ServiceOrderAdd(Resource):
    @jwt_required()
    def post(self):
        current_user = get_jwt_identity()
        user = user_service.get_user(current_user)
        
        if not user:
            return make_response(jsonify({"message": "User not found"}), 404)
        
        cart = cart_service.get_cart_by_token_and_status(user)
        if not cart:
            cart = cart_service.create_cart(user, secrets.token_hex(32))

        amount = request.json.get('amount')

        if amount < 0:
            return make_response(jsonify({"message": "Amount must be greater than zero"}), 400)

        if type(amount) != int:
            return make_response(jsonify({"message": "Amount must be a integer"}), 400)
        

        tokenProduct = request.json.get('tokenProduct')
        product = product_service.product_list_token(tokenProduct)

        errorTypes = {}
        if not product:
            errorTypes['product'] = 'Product not found.'
            return make_response(jsonify(errorTypes), 404)
        elif product.qt < amount:
            errorTypes['amount'] = 'Amount not available.'
            return make_response(jsonify(errorTypes), 400)
        

        if product.discount and product.discount > 0 and product.discount < 100:
            discountUnit = round((product.discount * product.valueResale) / 100, 2)
            discount = discountUnit * amount
            value = (product.valueResale * amount) - discount
        else:
            value = product.valueResale * amount      

        checkingProduct = order_service.get_order_by_tokenProduct_and_tokenCart(tokenProduct, cart.token)

        if amount == 0:
            if checkingProduct:
                order_service.delete_order(checkingProduct)
                orders = order_service.get_order_by_tokenCart(cart.token)
                if not orders:
                    cart_service.update_cart(cart, False)
                    cart_service.update_cart_status(cart, 'canceled')

        if checkingProduct:
            order_service.update_order(checkingProduct, checkingProduct.qt + amount, checkingProduct.value + value, checkingProduct.discount + discount)
        else:
            order_service.create_order(
                tokenProduct=tokenProduct,
                tokenUser=user,
                tokenCart=cart.token,
                token=secrets.token_hex(32),
                qt=amount,
                discount=discount,
                value=value,
            )
        orders = order_service.get_order_by_tokenCart(cart.token)
        return make_response(jsonify(orders), 200)


class ServiceOrderClosing(Resource):
    @jwt_required()
    def post(self):
        current_user = get_jwt_identity()
        user = user_service.get_user(current_user)
        
        if not user:
            return make_response(jsonify({"message": "User not found"}), 404)
        
        cart = cart_service.get_cart_by_token_and_status(user)
        if not cart:
            return make_response(jsonify({"message": "Cart not found"}), 404)
        
        cart_service.update_cart(cart, False)
        return make_response(jsonify({"message": "Cart closed"}), 200)
    

class ServiceOrderOpening(Resource):
    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        user = user_service.get_user(current_user)
        
        if not user:
            return make_response(jsonify({"message": "User not found"}), 404)
        
        cart = cart_service.get_cart_by_token_and_status(user)
        if not cart:
            return make_response(jsonify({"message": "Cart not found"}), 404)
        
        cart_service.update_cart(cart, True)
        orders = order_service.get_order_by_tokenCart(cart.token)
        return make_response(jsonify(orders), 200)


class ServiceOrderCancel(Resource):
    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        user = user_service.get_user(current_user)
        
        if not user:
            return make_response(jsonify({"message": "User not found"}), 404)
        
        cart = cart_service.get_cart_by_token_and_status(user)
        if not cart:
            return make_response(jsonify({"message": "Cart not found"}), 404)
        
        cart_service.update_cart(cart, False)
        cart_service.update_cart_status(cart, 'canceled')
        orders = order_service.list_order_by_tokenCart(cart.token)
        for order in orders:
            order_service.delete_order(order)
        return make_response(jsonify({"message": "Cart canceled"}), 200)
    

api.add_resource(ServiceOrderAdd, '/add')

api.add_resource(ServiceOrderOpening, '/open')

api.add_resource(ServiceOrderClosing, '/close')

api.add_resource(ServiceOrderCancel, '/cancel')
