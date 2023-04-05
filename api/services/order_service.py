from ..models import order_model
from api import db

def create_order(tokenProduct, tokenUser, tokenCart, token, qt, discount, value):
    order = order_model.Order(tokenProduct=tokenProduct, tokenUser=tokenUser, tokenCart=tokenCart, token=token, qt=qt, discount=discount, value=value)
    db.session.add(order)
    db.session.commit()
    return order