from api import db
from ..models import order_model
from babel.numbers import format_currency

class Product(db.Model):
     __tablename__="products"
     id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
     prodName = db.Column(db.String(100), nullable=False)
     valueResale = db.Column(db.Numeric(precision=8, scale=2), nullable=False)
     cust = db.Column(db.Numeric(precision=8, scale=2), nullable=False)
     tax = db.Column(db.Numeric(precision=8, scale=2), nullable=False)
     supplier = db.Column(db.String(100), nullable=True)
     qt = db.Column(db.Integer, nullable=False)
     discount = db.Column(db.Numeric(precision=4, scale=2), nullable=True)
     description = db.Column(db.Text, nullable=True)
     datePurchase = db.Column(db.Date, nullable=False)
     token = db.Column(db.String(16), unique=True, nullable=False)

     def formatted_price(self, locale='pt_BR'):
        return format_currency(self.price, 'BRL', locale=locale)

     orders = db.relationship('Order', backref='product', lazy='dynamic')



