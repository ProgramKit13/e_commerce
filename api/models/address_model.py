from api import db
import enum
from sqlalchemy import Enum

class active(enum.Enum):
    active = 1
    inative = 2


class Address(db.Model):
    __tablename__="adresses"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    neighborhood = db.Column(db.String(100), nullable=False)
    street = db.Column(db.String(100), nullable=False)
    number = db.Column(db.Integer, nullable=False)
    state = db.Column(db.String(2), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    zipCode = db.Column(db.String(9), nullable=False)
    activate = db.Column(db.Enum(active), nullable=False)
    idUser = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    

    


