from api import ma
from ..models import phone_model
from marshmallow import fields

class PhoneSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = phone_model.Address
        load_instance = True
        fields = ('id', 'type', 'ddd', 'number', 'idUser')

    type = fields.String(required=True)
    ddd = fields.String(required=True)
    number = fields.String(required=True)     
    idUser= fields.Integer(required=True)
