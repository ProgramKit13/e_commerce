from ..models import supplier_model
from api import db


##Register
def supplier_register(supplier):
    supplier_bd = supplier_model.Supplier(name=supplier.name, email=supplier.email,  neighborhood=supplier.neighborhood, street=supplier.street, number=supplier.number, state=supplier.state, city=supplier.city, zipCode=supplier.zipCode, complement=supplier.complement, cnpj=supplier.cnpj, phone=supplier.phone, token=supplier.token)
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