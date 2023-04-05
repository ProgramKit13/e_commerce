from api import db
import enum
from sqlalchemy import Enum
from ..models import address_model, userPayments_model, cart_models, order_model
from passlib.hash import pbkdf2_sha256

class genre(enum.Enum):
    masculino = 1
    feminino = 2
    outros = 3

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    firstName = db.Column(db.String(50), nullable=False)
    lastName = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    cpf = db.Column(db.String(11), nullable=False)
    genre = db.Column(db.Enum(genre), nullable=False)
    dateCreation = db.Column(db.DateTime, nullable=False)
    phone = db.Column(db.String(13), nullable=True)
    token = db.Column(db.String(16), nullable=False, unique=True)
    adminAccess = db.Column(db.Boolean)

    adresses = db.relationship(address_model.Address, backref="user", lazy="dynamic")
    payments = db.relationship(userPayments_model.UserPayments, backref="user", lazy="dynamic")
    orders = db.relationship('Order', backref='user', lazy='dynamic')
    cart = db.relationship(cart_models.Cart, backref="user", lazy="dynamic")


    def encrypt_pass(self):
        self.password = pbkdf2_sha256.hash(self.password)

    def verify_pass(self, password):
        return pbkdf2_sha256.verify(password, self.password)