from ..models import address_model, user_model
from api import db

def address_register(address):
    address_bd = address_model.Address(neighborhood=address.neighborhood, street=address.street, number=address.number, state=address.state, city=address.city, zipCode=address.zipCode, activate=address.activate, idUser=address.idUser)
    db.session.add(address_bd)
    db.session.commit()

    return address_bd
        

def adressesList(id):
    adressesDetails = []
    adressesList = db.session.query(address_model.Address).join(user_model.User).filter(address_model.Address.idUser==id).all()
    if adressesList:
        for i in adressesList:
            adressesDetails.append(
        {
            'neighborhood':i.neighborhood,
            'street':i.street,
            'number':i.number,
            'state':i.state,
            'city':i.city,
            'zipCode':i.zipCode,
            'activate': str(i.activate),
        }
        )
    return adressesDetails


def delete_address(address):
    db.session.delete(address)
    db.session.commit()


def address_update(oldAdress, newAddress):
    oldAdress.neighborhood = newAddress.neighborhood
    oldAdress.street = newAddress.street
    oldAdress.number = newAddress.number
    oldAdress.state = newAddress.state
    oldAdress.city = newAddress.city
    oldAdress.zipCode = newAddress.zipCode
    oldAdress.idUser = newAddress.idUser
    db.session.commit()


def address_delete(product):
    db.session.delete(product)
    db.session.commit()