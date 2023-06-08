from api import db
from babel.numbers import format_currency

class Product(db.Model):
    __tablename__="products"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    prodName = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    sector = db.Column(db.String(100), nullable=False)
    supplier = db.Column(db.String(100), nullable=True)
    supplierCode = db.Column(db.String(100), nullable=True)
    manufacturer = db.Column(db.String(100), nullable=True)
    valueResale = db.Column(db.Numeric(precision=8, scale=2), nullable=False)
    cust = db.Column(db.Numeric(precision=8, scale=2), nullable=False)
    tax = db.Column(db.Numeric(precision=8, scale=2), nullable=False)
    qt = db.Column(db.Integer, nullable=False)
    discount = db.Column(db.Numeric(precision=4, scale=2), nullable=True)
    weight = db.Column(db.Numeric(precision=8, scale=2), nullable=True)
    weightUnit = db.Column(db.String(50), nullable=True)
    dimensions = db.Column(db.String(100), nullable=True)
    dimensionsUnit = db.Column(db.String(50), nullable=True)
    barcode = db.Column(db.String(50), nullable=True)
    datePurchase = db.Column(db.Date, nullable=False)
    lastUpdated = db.Column(db.Date, nullable=True)
    reorderPoint = db.Column(db.Integer, nullable=True)
    restockTime = db.Column(db.Integer, nullable=True)
    warrantyInfo = db.Column(db.Text, nullable=True)
    batchInfo = db.Column(db.String(100), nullable=True)
    expiryDate = db.Column(db.Date, nullable=True)
    materialOrIngredients = db.Column(db.Text, nullable=True)
    safetyRating = db.Column(db.String(100), nullable=True)
    shippingRestrictions = db.Column(db.Text, nullable=True)
    token = db.Column(db.String(16), unique=True, nullable=False)

    def formatted_price(self, locale='pt_BR'):
        return format_currency(self.valueResale, 'BRL', locale=locale)

    orders = db.relationship('Order', backref='product', lazy='dynamic')
