from api import ma
from ..models import sector_model
from marshmallow import fields

class SectorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model: sector_model.Sector
        load_instance = True
        field = ('name', 'token')

    name = fields.String(required=True)
    token = fields.String(required=True)