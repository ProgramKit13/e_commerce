from api import db
from ..models import supplier_model, cart_models

class Product(db.Model):
    __tablename__="products"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    prodName = db.Column(db.String(100), nullable=False)
    valueResale = db.Column(db.Float(9), nullable=False)
    cust = db.Column(db.Float(9), nullable=False)
    tax = db.Column(db.Float(9), nullable=True)
    supplier = db.Column(db.String(100), nullable=True)
    qt = db.Column(db.Integer, nullable=False)
    alterResale = db.Column(db.Float(9), nullable=True)
    discount = db.Column(db.Float(9), nullable=True)
    description = db.Column(db.Text, nullable=True)
    datePurchase = db.Column(db.DateTime, nullable=False)
    dateShelf = db.Column(db.DateTime, nullable=False)
    token = db.Column(db.String(64), unique=True, nullable=False)
    
    supplier = db.relationship(supplier_model.Supplier, backref="products", lazy="dynamic")

    cart = db.relationship(cart_models.Cart, backref="products", lazy="dynamic")
