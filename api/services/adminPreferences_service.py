from ..models import adminPreferences_model
from api import db

def create_adminPreferences(token, productsPerPage):
    adminPreferences = adminPreferences_model.AdminPreferences(tokenUser=token, productsPerPage=productsPerPage)
    db.session.add(adminPreferences)
    db.session.commit()
    return adminPreferences


def get_adminPreferences_by_token(token):
    adminPreferences = adminPreferences_model.AdminPreferences.query.filter(adminPreferences_model.AdminPreferences.token == token).first()
    return adminPreferences

def get_adminPreferencesPerpage_by_token(token):
    adminPreferences = adminPreferences_model.AdminPreferences.query.filter(adminPreferences_model.AdminPreferences.tokenUser == token).first()
    return adminPreferences

def update_adminPreferencesPerPage(adminPreferences, productsPerPage):
    adminPreferences.productsPerPage = productsPerPage
    db.session.commit()


def listPerpageProductsEnum():
    enum = adminPreferences_model.productsPerPage
    return [i.value for i in enum]


def get_enum_name_by_value(value):
    for enum_value in adminPreferences_model.productsPerPage:
        if enum_value.value == value:
            return enum_value.name
    return None

