from api import db

class Product(db.Model):
    __tablename__="products"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    prodName = db.Column(db.String(100), nullable=False)
    valueResale = db.Column(db.Float(10), nullable=False)
    cust = db.Column(db.Float(10), nullable=False)
    tax = db.Column(db.Float(10), nullable=True)
    supplier = db.Column(db.String(100), nullable=True)
    qt = db.Column(db.Integer, nullable=False)
    alterResale = db.Column(db.Float(10), nullable=True)
    token = db.Column(db.String(64), unique=True, nullable=False)
    


