from ..models import supplier_model
from api import db


##Register
def supplier_register(supplier):
    supplier_bd = supplier_model.Supplier(supplierName=supplier.supplierName, supplierEmail=supplier.supplierEmail, supplierState=supplier.supplierState, supplierCity=supplier.supplierCity, supplierNeighborhood=supplier.supplierNeighborhood, supplierStreet=supplier.supplierStreet, supplierNumber=supplier.supplierNumber, supplierComplement=supplier.supplierComplement, supplierZipCode=supplier.supplierZipCode, supplierCnpj=supplier.supplierCnpj, token=supplier.token, supplierPhone_01=supplier.supplierPhone_01, supplierPhone_02=supplier.supplierPhone_02)
    db.session.add(supplier_bd)
    db.session.commit()

    return supplier_bd
########################################


##List
def supplier_list():
    suppliers = supplier_model.Supplier.query.all()
    return suppliers


##Search
def supplier_id(id):
    supplier = supplier_model.Supplier.query.filter_by(id=id).first()
    return supplier
########################################

##Update
def supplier_update(oldSupplier, newSupplier):
        oldSupplier.supplierName = newSupplier.supplierName
        oldSupplier.supplierEmail = newSupplier.supplierEmail
        oldSupplier.supplierState = newSupplier.supplierState
        oldSupplier.supplierCity = newSupplier.supplierCity
        oldSupplier.supplierNeighborhood = newSupplier.supplierNeighborhood
        oldSupplier.supplierStreet = newSupplier.supplierStreet
        oldSupplier.supplierNumber = newSupplier.supplierNumber
        oldSupplier.supplierComplement = newSupplier.supplierComplement
        oldSupplier.supplierZipCode = newSupplier.supplierZipCode
        oldSupplier.supplierCnpj = newSupplier.supplierCnpj
        oldSupplier.supplierPhone_01 = newSupplier.supplierPhone_01
        oldSupplier.supplierPhone_02 = newSupplier.supplierPhone_02
        db.session.commit()
########################################


##Delete
def supplier_delete(supplier):
    db.session.delete(supplier)
    db.session.commit()