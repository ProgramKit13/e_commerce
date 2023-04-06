from ..models import cart_model, order_model
from api import db
from sqlalchemy import and_

def create_cart(tokenUser, token):
    cart = cart_model.Cart(tokenUser=tokenUser, token=token, openCart=True, status='panding')
    db.session.add(cart)
    db.session.commit()
    return cart


def get_cart_by_token_and_status(token):
    cart = cart_model.Cart.query.filter(and_(cart_model.Cart.tokenUser == token, cart_model.Cart.status == 'panding')).first()
    return cart

def update_cart(cart, status):
    cart.openCart = status
    db.session.commit()


def update_cart_status(cart, status):
    cart.status = status
    db.session.commit()





