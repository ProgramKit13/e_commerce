from api import ma
from ..models import cart_model
from marshmallow import fields

class CartSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = cart_model.Cart
        load_instance = True
        fields = ('id', 'tokenUser', 'token', 'discountTotal', 'valueTtotal', 'openCart', 'status')

    id = fields.Integer(dump_only=True)
    tokenUser = fields.String(required=True)
    token = fields.String(required=True)
    discountTotal = fields.Float(required=True)
    valueTtotal = fields.Float(required=True)
    openCart = fields.Boolean(required=True)
    status = fields.String(required=True)