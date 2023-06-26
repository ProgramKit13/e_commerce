from api import db

class Supplier(db.Model):
    __tablename__ = "suppliers"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    supplierName = db.Column(db.String(50), nullable=False)
    supplierEmail = db.Column(db.String(50), nullable=False)
    supplierState = db.Column(db.String(2), nullable=False)
    supplierCity = db.Column(db.String(50), nullable=False)
    supplierNeighborhood = db.Column(db.String(50), nullable=False)
    supplierStreet = db.Column(db.String(100), nullable=False)
    supplierNumber = db.Column(db.Integer, nullable=False)
    supplierComplement = db.Column(db.String(100), nullable=True)
    supplierZipCode = db.Column(db.String(9), nullable=False)
    supplierCnpj = db.Column(db.String(18), nullable=False)
    supplierPhone_01 = db.Column(db.String(13), nullable=True)
    supplierPhone_02 = db.Column(db.String(13), nullable=True)
    token = db.Column(db.String(16), nullable=False)