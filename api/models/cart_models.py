from api import db
import enum
from sqlalchemy import Enum

class confirmationOption(enum.Enum):
    confirmation = 1
    canceled = 2

class Cart(db.Model):
    __tablename__ = "carts"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    qt = db.Column(db.Integer, nullable=False)
    value = db.Column(db.Float, nullable=False)
    confirm = db.Column(db.Enum(confirmationOption), nullable=False)
    totalDiscount = db.Column(db.Float(9), nullable=True)
    tokenUser = db.Column(db.String(16), db.ForeignKey("user.token"), nullable=False)
    tokenProduct = db.Column(db.String(16), db.ForeignKey("products.token"), nullable=False)
    tokenPayment = db.Column(db.String(16), db.ForeignKey("user_payments.token"), nullable=False)
    token = db.Column(db.String(16), nullable=False, unique=True)