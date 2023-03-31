from api import ma
from ..models import user_model
from marshmallow import fields

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = user_model.User
        load_instance = True
        fields = ('id','email', 'password')

    email = fields.String(required=True)
    password = fields.String(required=True)     
