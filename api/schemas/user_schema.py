from api import ma
from ..models import user_model
from marshmallow import fields

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = user_model.User
        load_instance = True
        fields = ('id', 'name', 'email', 'password', 'neighborhood', 'street', 'number', 'state', 'city', 'zipCode', 'adminAccess')

    name = fields.String(required=True)
    email = fields.String(required=True)
    password = fields.String(required=True)     
    adminAccess = fields.Boolean(required=False)

