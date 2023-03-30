from api import db
from ..models import supPhone_model

class Supplier(db.Model):
    __tablename__ = "suppliers"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    uf = db.Column(db.String(2), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    neighborhood = db.Column(db.String(50), nullable=False)
    number = db.Column(db.String(9), nullable=False)
    complement = db.Column(db.String(100), nullable=False)
    cnpj = db.Column(db.String(14), nullable=False)
    idProduct = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)

    supPhone = db.relationship(supPhone_model.SupPhones, backref="suppliers", lazy="dynamic")