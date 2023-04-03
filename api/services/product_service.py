from ..models import product_model
from api import db
from sqlalchemy import or_
##Register
def prod_register(prod):
    prod_bd = product_model.Product(prodName=prod.prodName, valueResale=prod.valueResale, cust=prod.cust, tax=prod.tax, supplier=prod.supplier, qt=prod.qt, alterResale=prod.alterResale, discount=prod.discount, description=prod.description, datePurchase=prod.datePurchase, dateShelf=prod.dateShelf, token=prod.token)
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



def AdminsearchProduct(name):
    search = "%{}%".format(name)
    products = product_model.Product.query.filter(or_(product_model.Product.prodName.ilike(search), product_model.Product.description.ilike(search))).all()
    detailsProduct = []
    for product in products:
        detailsProduct.append({
            "product_name":product.prodName,
            "value_resale":product.valueResale,
            "cust":product.cust,
            "tax":product.tax,
            "supplier":product.supplier,
            "amount":product.qt,
            "alter_resale":product.alterResale,
            "discount":product.discount,
            "description":product.description,
            "date_purchase":product.datePurchase,
            "dateShelf":product.dateShelf
        })
    return detailsProduct



def searchProduct(name):
    search = "%{}%".format(name)
    products = product_model.Product.query.filter(or_(product_model.Product.prodName.ilike(search), product_model.Product.description.ilike(search))).all()
    detailsProduct = []
    for product in products:
        detailsProduct.append({
            "name":product.prodName,
            "value":product.valueResale,
            "amount":product.qt,
            "discount":product.discount,
            "description":product.description
        })
    return detailsProduct
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
