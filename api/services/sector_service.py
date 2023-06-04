from ..models import sector_model
from api import db


##Register
def sector_register(sector):
    sector_bd = sector_model.Sector(name=sector.name, token=sector.token)
    db.session.add(sector_bd)
    db.session.commit()

    return sector_bd


##List
def sector_list():
    sectors = sector_model.Sector.query.all()
    listSector = []
    for i in sectors:
        listSector.append(i.name)
    return listSector


#Search
def sector_getBy_name(name):
    sectors = sector_model.Sector.query.filter_by(name=name).first()
    return sectors