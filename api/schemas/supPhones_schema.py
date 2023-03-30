from api import ma
from ..models import supPhone_model
from marshmallow import fields

class PhoneSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = supPhone_model.SupPhones
        load_instance = True
        fields = ('id', 'type', 'ddd', 'number', 'iUser')

    type = fields.String(required=True)
    ddd = fields.String(required=True)
    number = fields.String(required=True)     
    idSup= fields.Integer(required=True)
