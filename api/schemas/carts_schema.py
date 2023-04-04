from api import ma
from ..models import cart_models
from marshmallow import fields

class Supplier_Schema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = cart_models.Cart
        load_instance = True
        fields = ('id', 'qt', 'value', 'confirm', 'totalDiscount', 'tokenUser', 'tokenProduct', 'token')

    qt = fields.Integer(required=True)
    value = fields.Float(required=True)
    confirm = fields.Enum(required=True)     
    totalDiscount= fields.Float(required=True)
    tokenUser = fields.String(required=True)
    tokenProduct = fields.String(required=True)
    token = fields.String(required=False)
