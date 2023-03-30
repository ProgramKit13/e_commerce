from api import ma
from ..models import supplier_model
from marshmallow import fields

class Supplier_Schema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = supplier_model.Supplier
        load_instance = True
        fields = ('id', 'name', 'email', 'uf', 'neighborhood', 'number', 'complement','cnpj', 'idProduct')

    name = fields.String(required=True)
    email = fields.String(required=True)
    uf = fields.String(required=True)     
    neighborhood= fields.String(required=True)
    number = fields.String(required=True)
    complement = fields.String(required=True)
    cnpj = fields.String(required=True)
    idProduct = fields.Integer(required=True)
