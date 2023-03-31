from ..models import user_model, address_model
from api import db

def user_register(user):
    print(user)
    user_bd = user_model.User(firstName=user.firstName, lastName=user.lastName, email=user.email, password=user.password, cpf=user.cpf, genre=user.genre, token=user.token, dateCreation=user.dateCreation)
    user_bd.encrypt_pass()
    db.session.add(user_bd)
    db.session.commit()

    return user_bd


def user_list():
    users = user_model.User.query.all()
    return users



def user_list_id(id):
    result = db.session.query(address_model.Address).join(user_model.User).filter(address_model.Address.idUser==id).filter(address_model.Address.activate==1).first()
    if result:
        user = {}
        user = {
            "name": result.user.name,
            "email": result.user.email,
            "cpf":result.user.cpf,
            "genre":result.user.genre,
            "neighborhood":result.neighborhood,
            "street":result.street,
            "number":result.number,
            "state":result.state,
            "city":result.city,
            "zipCode":result.zipCode
        }
        return user
    
    else: 
        user = user_model.User.query.filter_by(id=id).first()

        return user


def pass_update(oldPass, newPass):
    oldPass.password = newPass.password
    db.session.commit()



def user_email(email):
    return user_model.User.query.filter_by(email=email).first()