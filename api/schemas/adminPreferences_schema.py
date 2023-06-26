from api import ma
from ..models import adminPreferences_model
from marshmallow import fields

class AdminPreferencesSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = adminPreferences_model.AdminPreferences
        load_instance = True
        fields = ('id', 'productsPerPage', 'suppliersPerPage', 'token')
    
    id = fields.Integer(dump_only=True)
    productsPerPage = fields.Integer(required=True)
    productsPerPage = fields.Integer(required=True)
    token = fields.String(required=True)
