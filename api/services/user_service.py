from ..models import user_model, address_model
from api import db
from passlib.hash import pbkdf2_sha256


##register
def user_register(user):
    user_bd = user_model.User(firstName=user.firstName, lastName=user.lastName, email=user.email, password=user.password, cpf=user.cpf, genre=user.genre, token=user.token, dateCreation=user.dateCreation, adminAccess=user.adminAccess, phone=user.phone)
    user_bd.encrypt_pass()
    db.session.add(user_bd)
    db.session.commit()

    return user_bd
################################################



##config
def get_user_id(id):
    return user_model.User.query.filter_by(id=id).first()

def get_user(id):
     user = user_model.User.query.filter_by(id=id).first()
     token = user.token
     return token

def get_user_token(token):
    user = user_model.User.query.filter_by(token=token).first()
    return user

def user_email(email):
    return user_model.User.query.filter_by(email=email).first()


#################################################



##search
def user_list():
    users = user_model.User.query.all()
    return users

def user_list_email(email):
    user = user_model.User.query.filter_by(email=email).first()
    if user:
        result = db.session.query(address_model.Address).join(user_model.User).filter(address_model.Address.tokenUser==user.token).all()
        userList = []
        userList.append({
                "firstName": user.firstName,
                "lastName": user.lastName,
                "email": user.email,
                "cpf":user.cpf,
                "genre":str(user.genre),
                "phone":user.phone
        })
        if result:
            for i in result:
                userList.append({
                    "neighborhood":i.neighborhood,
                    "complement":i.complement,
                    "street":i.street,
                    "number":i.number,
                    "state":i.state,
                    "city":i.city,
                    "zipCode":i.zipCode
                })
            return userList
        
        else: 
            return user
    else:
        msgm = 'User not found'
        return msgm

def user_list_cpf(cpf):
    user = user_model.User.query.filter_by(cpf=cpf).first()
    if user:
        result = db.session.query(address_model.Address).join(user_model.User).filter(address_model.Address.tokenUser==user.token).all()
        userList = []
        userList.append({
                "firstName": user.firstName,
                "lastName": user.lastName,
                "email": user.email,
                "cpf":user.cpf,
                "genre":str(user.genre),
                "phone":user.phone
        })
        if result:
            for i in result:
                userList.append({
                    "neighborhood":i.neighborhood,
                    "complement":i.complement,
                    "street":i.street,
                    "number":i.number,
                    "state":i.state,
                    "city":i.city,
                    "zipCode":i.zipCode
                })
            return userList
        
        else: 
            return user
    else:
        msgm = 'User not found'
        return msgm
#################################################


##update
def user_update(oldUser, newUser):
    newUser.password = pbkdf2_sha256.hash(newUser.password)
    oldUser.firstName = newUser.firstName
    oldUser.lastName = newUser.lastName
    oldUser.email = newUser.email
    oldUser.adminAccess = newUser.adminAccess
    oldUser.cpf = newUser.cpf
    oldUser.genre = newUser.genre
    oldUser.password = newUser.password
    oldUser.dateCreation = newUser.dateCreation
    oldUser.phone = newUser.phone
    db.session.commit()
##################################################

##Delete
def search_for_delete(id):
    user = user_model.User.query.filter_by(id=id).first()
    if user:
        result = db.session.query(address_model.Address).join(user_model.User).filter(address_model.Address.tokenUser==user.token).all()
        if result:
            idBody = []
            for i in result:
                idBody.append({i})
            return idBody
        else:
            return user
    else:
        msgm = 'Usuário não encontrado.'
        return msgm

def user_delete(id):
    db.session.delete(id)
    db.session.commit()

def user_delete_adresses(id):
    db.session.delete(id)
    db.session.commit()