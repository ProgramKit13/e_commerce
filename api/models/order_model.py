from api import db

class Order(db.Model):
    __tablename__ = "service_order"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    tokenProduct = db.Column(db.String(16), db.ForeignKey("products.token"), nullable=False)
    tokenUser = db.Column(db.String(16), db.ForeignKey("user.token"), nullable=False)
    tokenCart = db.Column(db.String(64), db.ForeignKey("carts.token"), nullable=False)
    token = db.Column(db.String(64), nullable=False, unique=True)
    qt = db.Column(db.Integer, nullable=False)
    value = db.Column(db.Float(9), nullable=False)
    discount = db.Column(db.Float(9), nullable=True)

