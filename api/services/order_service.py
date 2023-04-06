from ..models import order_model, product_model
from api import db
from sqlalchemy import and_

def create_order(tokenProduct, tokenUser, tokenCart, token, qt, discount, value):
    order = order_model.Order(tokenProduct=tokenProduct, tokenUser=tokenUser, tokenCart=tokenCart, token=token, qt=qt, discount=discount, value=value)
    db.session.add(order)
    db.session.commit()
    return order


def list_order_by_tokenCart(tokenCart):
    order = order_model.Order.query.filter(order_model.Order.tokenCart == tokenCart).all()
    return order

def get_order_by_tokenProduct_and_tokenCart(tokenProduct, tokenCart):
    order = order_model.Order.query.filter(and_(order_model.Order.tokenProduct == tokenProduct, order_model.Order.tokenCart == tokenCart)).first()
    return order

def update_order(order, qt, value, discount):
    order.qt = qt
    order.value = value
    order.discount = discount
    db.session.commit()


def get_order_by_tokenCart(tokenCart):
    order = order_model.Order.query.filter(order_model.Order.tokenCart == tokenCart).all()
    orderList = []
    for item in order:
        product = product_model.Product.query.filter(product_model.Product.token == item.tokenProduct).first()
        serviceOrder = order_model.Order.query.filter(order_model.Order.tokenProduct == item.tokenProduct).first()
        orderList.append({
            'name': product.prodName,
            'valueUnit': product.valueResale,
            'value': serviceOrder.value,
            'discountUnit': product.discount,
            'amount': serviceOrder.qt,
            'discount': serviceOrder.discount,
        })
    return orderList


def delete_order(order):
    db.session.delete(order)
    db.session.commit()