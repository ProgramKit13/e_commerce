from api import db
import enum
from sqlalchemy import Enum

class type(enum.Enum):
    fixed = 1
    cellphone = 2


class SupPhones(db.Model):
    __tablename__="suppliers_phones"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    type = db.Column(db.Enum(type), nullable=False)
    ddd = db.Column(db.String(2), nullable=False)
    number = db.Column(db.String(9), nullable=False)
    idSups = db.Column(db.Integer, db.ForeignKey("suppliers.id"), nullable=False)
    

    


