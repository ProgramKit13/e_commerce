from ..models import address_model
from api import db


##Register
def address_register(address):
    address_bd = address_model.Address(neighborhood=address.neighborhood, street=address.street, number=address.number, state=address.state, city=address.city, zipCode=address.zipCode, activate=address.activate, tokenUser=address.tokenUser)
    db.session.add(address_bd)
    db.session.commit()

    return address_bd
########################################

##List
def adresses_list():
    adresses = address_model.Address.query.all()
    return adresses


def user_address(token):
    adresses = address_model.Address.query.filter_by(tokenUser=token).all()
    dictAddress = []
    for address in adresses:
        dictAddress.append({
            "neighborhood":address.neighborhood,
            "street":address.street,
            "number":address.number,
            "state":address.state,
            "city":address.city,
            "zipCode":address.zipCode,
            "activate": str(address.activate)
        })
    return dictAddress

##########################################

##Search address
def search_address_by_id(id):
    address = address_model.Address.query.filter_by(id=id).first()
    return address


def user_search_address_by_id(id, token):
    address = address_model.Address.query.filter_by(id=id).first()
    print(id, token)
    if address.tokenUser == token:
        return address
    else:
        return False


##Delete address
def delete_address(address):
    db.session.delete(address)
    db.session.commit()
#########################################


##Update Address
def address_update(oldAdress, newAddress):
    oldAdress.neighborhood = newAddress.neighborhood
    oldAdress.street = newAddress.street
    oldAdress.number = newAddress.number
    oldAdress.state = newAddress.state
    oldAdress.city = newAddress.city
    oldAdress.zipCode = newAddress.zipCode
    oldAdress.tokenUser = newAddress.tokenUser
    db.session.commit()
##########################################

