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
    idUser = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    idProduct = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
    idPayment = db.Column(db.Integer, db.ForeignKey("user_payments.id"), nullable=False)
    token = db.Column(db.String(16), nullable=False, unique=True)