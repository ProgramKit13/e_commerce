from api import db

class Supplier(db.Model):
    __tablename__ = "suppliers"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(2), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    neighborhood = db.Column(db.String(50), nullable=False)
    street = db.Column(db.String(100), nullable=False)
    number = db.Column(db.Integer, nullable=False)
    complement = db.Column(db.String(100), nullable=True)
    zipCode = db.Column(db.String(9), nullable=False)
    cnpj = db.Column(db.String(18), nullable=False)
    phone = db.Column(db.String(13), nullable=True)
    token = db.Column(db.String(16), nullable=False)