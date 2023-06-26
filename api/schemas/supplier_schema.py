from api import ma
from ..models import supplier_model
from marshmallow import fields

class Supplier_Schema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = supplier_model.Supplier
        load_instance = True
        fields = ('id', 'supplierName', 'supplierEmail', 'supplierState', 'supplierCity', 'supplierNeighborhood', 'supplierStreet', 'supplierNumber', 'supplierComplement', 'supplierZipCode', 'supplierCnpj', 'supplierPhone_01', 'supplierPhone_02' )

    supplierName = fields.String(required=True)
    supplierEmail = fields.String(required=True)
    supplierState = fields.String(required=True)
    supplierCity = fields.String(required=True)
    supplierNeighborhood = fields.String(required=True)
    supplierStreet = fields.String(required=True)
    supplierNumber = fields.Integer(required=True)
    supplierComplement = fields.String(required=False)
    supplierZipCode = fields.String(required=True)
    supplierCnpj = fields.String(required=True)
    supplierPhone_01 = fields.String(required=False)
    supplierPhone_02 = fields.String(required=False)
    


