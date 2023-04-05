from api import db
import enum
from sqlalchemy import Enum
from ..models import order_model

class status(enum.Enum):
    confirmed = 1
    panding = 3
    canceled = 4



class Cart(db.Model):
    __tablename__ = "carts"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    tokenUser = db.Column(db.String(16), db.ForeignKey("user.token"), nullable=False)
    token = db.Column(db.String(64), nullable=False, unique=True)
    discountTotal = db.Column(db.Float(9), nullable=True)
    valueTtotal = db.Column(db.Float(9), nullable=True)
    openCart = db.Column(db.Boolean, nullable=False, default=False)
    status = db.Column(db.Enum(status), nullable=False)

    orders = db.relationship('Order', backref='carts', lazy='dynamic')
