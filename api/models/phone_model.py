from api import db
import enum
from sqlalchemy import Enum

class type(enum.Enum):
    fixed = 1
    cellphone = 2


class Phones(db.Model):
    __tablename__="phones"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    type = db.Column(db.Enum(type), nullable=False)
    ddd = db.Column(db.String(2), nullable=False)
    number = db.Column(db.String(9), nullable=False)
    idUser = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    

    


