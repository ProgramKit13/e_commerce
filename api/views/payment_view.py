from api import mercadopago
from api import app
from flask import jsonify
from datetime import datetime
from flask_restful import Resource
from api import api
from flask import request
app.config["APP_ACCESS_TOKEN"] = 'TEST-5349810922644847-040615-9df8e556c60fc6215d5bd736dd04d569-290320970'

##########TESTE DE API DO MERCADO PAGO##################
class PaymentViewPost(Resource):
    def post(self):
        card_token_object = request.json
        card_token_created = mercadopago.card_token().create(card_token_object)

        payment_data = {
             "transaction_amount": 100,
             "token": card_token_created["response"]["id"],
             "description": "Payment description",
             "payment_method_id": 'master',
             "installments": 12,
             "payer": {
                 "email": 'teste@joao.com'
             }
         }

        result = mercadopago.payment().create(payment_data)
        payment = result["response"]
        return jsonify(payment)



api.add_resource(PaymentViewPost, '/payment_post')