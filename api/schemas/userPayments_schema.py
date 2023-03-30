from api import ma
from ..models import userPayments_model
from marshmallow import fields

class UserPayments_Schema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = userPayments_model.UserPayments
        load_instance = True
        fields = ('id', 'typePayment', 'value', 'status', 'idUser', 'datePayment', 'dateStatus','cnpj')

    typePayment = fields.Enum(required=True)
    value = fields.Float(required=True)
    status = fields.Enum(required=True)     
    idUser= fields.Integer(required=True)
    datePayment = fields.DateTime(required=True)
    dateStatus = fields.DateTime(required=True)
