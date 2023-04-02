from ..models import product_model
from api import db


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

def searchProdName(name):
    search = "%{}%".format(name)
    detailsProduct = []

    def returnProduct(option):
        for product in option:
            detailsProduct.append({
                "product_name":product.prodName,
                "value_resale":product.valueResale,
                "cust":product.cust,
                "tax":product.tax,
                "supplier":product.supplier,
                "amount":product.qt,
                "alter_resale":product.alterResale,
                "discount":product.discount,
                "date_purchase":product.datePurchase,
                "dateShelf":product.dateShelf
            })
            
    productsByName = product_model.Product.query.filter(product_model.Product.prodName.like(search)).all()

    if productsByName != []:
        returnProduct(productsByName)

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
    db.session.commit()
####################################


#Delete 
def product_delete(product):
    db.session.delete(product)
    db.session.commit()
####################################
