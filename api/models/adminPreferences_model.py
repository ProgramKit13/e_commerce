from api import db
import enum
from sqlalchemy import Enum

class productsPerPage(enum.Enum):
    fifty = 50
    hundred = 100
    hundredFifty = 150
    twoHundred = 200


class AdminPreferences(db.Model):
    __tablename__="adminPreferences"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    productsPerPage = db.Column(db.Enum(productsPerPage), nullable=False)
    tokenUser = db.Column(db.String(16), db.ForeignKey("user.token"), nullable=False)