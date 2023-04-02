from api import ma
from ..models import address_model
from marshmallow import fields

class AddressSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = address_model.Address
        load_instance = True
        fields = ('id', 'neighborhood', 'street', 'number', 'state', 'city', 'zipCode','activate', 'tokenUser',)

    neighborhood = fields.String(required=True)
    street = fields.String(required=True)
    number = fields.Integer(required=True)     
    state= fields.String(required=True)
    city = fields.String(required=True)
    zipCode = fields.String(required=True)
    activate = fields.String(required=True)
    tokenUser = fields.String(required=False)
