from flask_restful import Resource
from api import api
from flask import request, make_response, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..services import user_service, product_service, cart_service, order_service
import secrets

class OpenCart(Resource):
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
        tokenProduct = request.json.get('tokenProduct')
        product = product_service.product_list_token(tokenProduct)

        errorTypes = {}
        if not product:
            errorTypes['product'] = 'Product not found.'
        elif product.qt < amount:
            errorTypes['amount'] = 'Amount not available.'

        if product.discount is not None and (product.discount > 100 or product.discount < 0):
            errorTypes['discount'] = 'Discount not available.'
        elif product.discount is not None:
            total_cart_qty = order_service.get_total_qty_by_cart(cart.token)
            discount = float(product.valueResale) * product.discount * total_cart_qty
            value = float(product.valueResale) * amount - discount
            if len(str(value)) >= 10:
                errorTypes['value'] = 'Value not available.'
        else:
            value = float(product.valueResale) * amount

        if errorTypes:
            return make_response(jsonify(errorTypes), 400)

        new_order = order_service.create_order(
            tokenProduct=tokenProduct,
            tokenUser=user,
            tokenCart=cart.token,
            token=secrets.token_hex(32),
            qt=amount,
            discount=discount if 'discount' in locals() else 0,
            value=value,
        )
        return make_response(jsonify('Produto adicionado com sucesso.'), 201)
        


api.add_resource(OpenCart, '/openCart')

