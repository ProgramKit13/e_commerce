from ..models import product_model
from api import db
from sqlalchemy import or_

##Register
def prod_register(prod):
    prod_bd = product_model.Product(
        prodName=prod.prodName, 
        description=prod.description,
        sector=prod.sector,
        supplier=prod.supplier,
        supplierCode=prod.supplierCode,
        manufacturer=prod.manufacturer,
        valueResale=prod.valueResale,
        cust=prod.cust,
        tax=prod.tax,
        qt=prod.qt,
        discount=prod.discount,
        weight=prod.weight,
        weightUnit=prod.weightUnit,
        dimensions=prod.dimensions,
        dimensionsUnit=prod.dimensionsUnit,
        barcode=prod.barcode,
        datePurchase=prod.datePurchase,
        lastUpdated=prod.lastUpdated,
        reorderPoint=prod.reorderPoint,
        restockTime=prod.restockTime,
        warrantyInfo=prod.warrantyInfo,
        batchInfo=prod.batchInfo,
        expiryDate=prod.expiryDate,
        materialOrIngredients=prod.materialOrIngredients,
        safetyRating=prod.safetyRating,
        shippingRestrictions=prod.shippingRestrictions,
        token=prod.token
    )
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
