from api import db
from . import cart_model
import enum
from sqlalchemy import Enum

class type(enum.Enum):
    debit = 1
    credt = 2
    ticket = 3
    pix = 4


class status(enum.Enum):
    aprovade = 1
    reprovade = 2
    panding = 3
    canceled = 4
    extoted = 5

class UserPayments(db.Model):
    __tablename__="user_payments"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    userToken = db.Column(db.String(16), db.ForeignKey("user.token"), nullable=False)
    cartToken = db.Column(db.String(16), db.ForeignKey("carts.token"), nullable=False)
    typePayment = db.Column(db.Enum(type), nullable=False)
    value = db.Column(db.Float, nullable=False)
    status = db.Column(db.Enum(status), nullable=False)
    datePayment = db.Column(db.DateTime, nullable=False)
    dateStatus = db.Column(db.DateTime, nullable=False)
    token = db.Column(db.String(64), nullable=False, unique=True)
    
    

    


