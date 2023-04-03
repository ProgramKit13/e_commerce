from api import ma
from ..models import supplier_model
from marshmallow import fields

class Supplier_Schema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = supplier_model.Supplier
        load_instance = True
        fields = ('id', 'name', 'email', 'state', "city", 'neighborhood', 'street', 'number', 'complement','zipCode', 'cnpj', 'phone', 'token')

    name = fields.String(required=True)
    email = fields.String(required=True)
    state = fields.String(required=True) 
    city = fields.String(required=True)    
    neighborhood= fields.String(required=True)
    street= fields.String(required=True)
    number = fields.Integer(required=True)
    complement = fields.String(required=False)
    zipCode = fields.String(required=True)
    cnpj = fields.String(required=True)
    phone = fields.String(required=False)
    token = fields.String(required=False)
