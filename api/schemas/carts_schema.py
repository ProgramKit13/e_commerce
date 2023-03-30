from api import ma
from ..models import cart_models
from marshmallow import fields

class Supplier_Schema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = cart_models.Cart
        load_instance = True
        fields = ('id', 'qt', 'value', 'confirm', 'totalDiscount', 'idUser', 'idProduct','idPayment', 'idProduct')

    qt = fields.Integer(required=True)
    value = fields.Float(required=True)
    confirm = fields.Enum(required=True)     
    totalDiscount= fields.Float(required=True)
    idUser = fields.Integer(required=True)
    idProduct = fields.Integer(required=True)
    idPayment = fields.Integer(required=True)
