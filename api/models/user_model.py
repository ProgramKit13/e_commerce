from api import db
import enum
from sqlalchemy import Enum

from . import cart_model
from ..models import address_model, userPayments_model, adminPreferences_model
from passlib.hash import pbkdf2_sha256

class genre(enum.Enum):
    masculino = 1
    feminino = 2
    outros = 3

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    dateCreation = db.Column(db.DateTime, nullable=False)
    token = db.Column(db.String(16), nullable=False, unique=True)
    adminAccess = db.Column(db.Boolean)

    adresses = db.relationship(address_model.Address, backref="user", lazy="dynamic")
    payments = db.relationship(userPayments_model.UserPayments, backref="user", lazy="dynamic")
    orders = db.relationship('Order', backref='user', lazy='dynamic')
    cart = db.relationship(cart_model.Cart, backref="user", lazy="dynamic")
    adminPreferences = db.relationship(adminPreferences_model.AdminPreferences, backref='user', lazy='dynamic')

    def encrypt_pass(self):
        self.password = pbkdf2_sha256.hash(self.password)

    def verify_pass(self, password):
        return pbkdf2_sha256.verify(password, self.password)