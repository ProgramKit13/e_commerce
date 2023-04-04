from api import ma
from ..models import userPayments_model
from marshmallow import fields

class UserPayments_Schema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = userPayments_model.UserPayments
        load_instance = True
        fields = ('id', 'typePayment', 'token', 'value', 'status', 'userToken', 'datePayment', 'dateStatus', 'cartToken')

    typePayment = fields.Enum(required=True)
    token = fields.String(required=True)
    value = fields.Float(required=True)
    status = fields.Enum(required=True)     
    userToken = fields.Integer(required=True)
    datePayment = fields.DateTime(required=True)
    dateStatus = fields.DateTime(required=True)
    cartToken = fields.String(required=False)
