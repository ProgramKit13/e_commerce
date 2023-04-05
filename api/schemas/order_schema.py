from api import ma
from ..models import order_model
from marshmallow import fields

class OrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model: order_model.Order
        load_instance = True
        field = ('tokenProduct', 'tokenUser', 'tokenCart', 'token', 'qt', 'value', 'discount')

    tokenProduct = fields.String(required=True)
    tokenUser = fields.String(required=True)
    tokenCart = fields.String(required=True)
    token = fields.String(required=True)
    qt = fields.Integer(required=True)
    value = fields.Float(required=True)
    discount = fields.Float(required=True)
    