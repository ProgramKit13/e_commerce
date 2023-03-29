from api import ma
from ..models import user_model
from marshmallow import fields

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = user_model.User
        load_instance = True
        fields = ('id', 'name', 'email', 'password', 'cpf', 'genre', 'neighborhood', 'street', 'number', 'state', 'city', 'zipCode')

    name = fields.String(required=True)
    email = fields.String(required=True)
    password = fields.String(required=True)     
    cpf = fields.String(required=True)
    genre = fields.String(required=True)

class updatePass(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = user_model.User
        load_instance = True
        fields = ('id', 'password')

    password = fields.String(required=True)


