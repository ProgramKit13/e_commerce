from api import ma
from ..models import product_model
from marshmallow import fields

class ProdSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = product_model.Product
        load_instance = True
        fields = ('id', 'prodName', 'valueResale', 'cust', 'tax', 'supplier', 'qt', 'alterResale')

    prodName = fields.String(required=True)
    valueResale = fields.Float(required=True)
    cust = fields.Float(required=True)
    tax = fields.Float(required=False)
    supplier = fields.String(required=False)
    qt = fields.Integer(required=True)
    alterResale = fields.Float(required=False)

