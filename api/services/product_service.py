from ..models import product_model
from api import db

def prod_register(prod):
    prod_bd = product_model.Product(prodName=prod.prodName, valueResale=prod.valueResale, cust=prod.cust, tax=prod.tax, supplier=prod.supplier, qt=prod.qt, alterResale=prod.alterResale, token=prod.token)
    db.session.add(prod_bd)
    db.session.commit()

    return prod_bd


def product_list():
    products = product_model.Product.query.all()
    return products


def product_list_id(id):
    products = product_model.Product.query.filter_by(id=id).first()
    return products


def product_update(oldData, newData):
    oldData.prodName = newData.prodName
    oldData.valueResale = newData.valueResale
    oldData.cust = newData.cust
    oldData.tax = newData.tax
    oldData.supplier = newData.supplier
    oldData.qt = newData.qt
    oldData.alterResale = newData.alterResale
    db.session.commit()

def product_delete(product):
    db.session.delete(product)
    db.session.commit()