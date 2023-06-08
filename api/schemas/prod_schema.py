from api import ma
from ..models import product_model
from marshmallow import fields

class ProdSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = product_model.Product
        load_instance = True
        fields = ('id', 'prodName', 'description', 'sector', 'supplier', 'supplierCode', 'manufacturer', 'valueResale', 'cust', 'tax', 'qt', 'discount', 'weight', 'weightUnit', 'dimensions', 'dimensionsUnit', 'barcode', 'datePurchase', 'lastUpdated', 'reorderPoint', 'restockTime', 'warrantyInfo', 'batchInfo', 'expiryDate', 'materialOrIngredients', 'safetyRating', 'shippingRestrictions', 'token')

    prodName = fields.String(required=True)
    description = fields.String(required=True)
    sector = fields.String(required=True)
    supplier = fields.String(required=False)
    supplierCode = fields.String(required=False)
    manufacturer = fields.String(required=False)
    valueResale = fields.Float(required=True)
    cust = fields.Float(required=True)
    tax = fields.Float(required=True)
    qt = fields.Integer(required=True)
    discount = fields.Float(required=False)
    weight = fields.Float(required=False)
    weightUnit = fields.String(required=False)
    dimensions = fields.String(required=False)
    dimensionsUnit = fields.String(required=False)
    barcode = fields.String(required=False)
    datePurchase = fields.Date(required=True)
    lastUpdated = fields.Date(required=True)
    reorderPoint = fields.Integer(required=False)
    restockTime = fields.Integer(required=False)
    warrantyInfo = fields.String(required=False)
    batchInfo = fields.String(required=False)
    expiryDate = fields.Date(required=False)
    materialOrIngredients = fields.String(required=False)
    safetyRating = fields.String(required=False)
    shippingRestrictions = fields.String(required=False)
    token = fields.String(required=False)
