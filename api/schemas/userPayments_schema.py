from api import ma
from ..models import userPayments_model
from marshmallow import fields

class UserPaymentsSchema(ma.SQLAlchemyAutoSchema):
    class meta():
        model = userPayments_model.UserPayments
        load_instance = True
        field = ('id', 'userToken', 'cartToken', 'typePayment', 'value', 'status', 'datePayment', 'dateStatus', 'token')

    userToken = fields.String(required=True)
    cartToken = fields.String(required=True)
    typePayment = fields.String(required=True)
    value = fields.Float(required=True)
    status = fields.String(required=True)
    datePayment = fields.DateTime(required=True)
    dateStatus = fields.DateTime(required=True)
    token = fields.String(required=True)
    
