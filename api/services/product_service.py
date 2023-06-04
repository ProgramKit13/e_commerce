from ..models import product_model
from api import db
from sqlalchemy import or_
##Register
def prod_register(prod):
    prod_bd = product_model.Product(prodName=prod.prodName, valueResale=prod.valueResale, cust=prod.cust, tax=prod.tax, supplier=prod.supplier, qt=prod.qt, discount=prod.discount, description=prod.description, datePurchase=prod.datePurchase, token=prod.token, sector=prod.sector)
    db.session.add(prod_bd)
    db.session.commit()

    return prod_bd
###################################


##List
def product_list():
    products = product_model.Product.query.all()
    return products
###################################

#Search
def product_list_id(id):
    products = product_model.Product.query.filter_by(id=id).first()
    return products



def product_list_token(token):
    product = product_model.Product.query.filter_by(token=token).first()
    return product



###################################


##Update
def product_update(oldData, newData):
    oldData.prodName = newData.prodName
    oldData.valueResale = newData.valueResale
    oldData.cust = newData.cust
    oldData.tax = newData.tax
    oldData.supplier = newData.supplier
    oldData.qt = newData.qt
    oldData.alterResale = newData.alterResale
    oldData.discount = newData.discount
    oldData.description = newData.description
    oldData.datePurchase = newData.datePurchase
    oldData.dateShelf = newData.dateShelf
    oldData.token = newData.token
    db.session.commit()
####################################


#Delete 
def product_delete(product):
    db.session.delete(product)
    db.session.commit()
####################################
