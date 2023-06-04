from api import ma
from ..models import product_model
from marshmallow import fields

class ProdSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = product_model.Product
        load_instance = True
        fields = ('id', 'prodName', 'valueResale', 'cust', 'tax', 'supplier', 'qt', 'discount','description', 'datePurchase', 'sector')
 
    prodName = fields.String(required=True)
    valueResale = fields.Float(required=True)
    cust = fields.Float(required=True)
    tax = fields.Float(required=True)
    supplier = fields.String(required=False)
    qt = fields.Integer(required=True)
    description = fields.String(required=True)
    datePurchase = fields.Date(required=True)
    discount = fields.Float(required=True)
    sector = fields.String(required=True)
