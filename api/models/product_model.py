from api import db
from ..models import cart_models


class Product(db.Model):
     __tablename__="products"
     id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
     prodName = db.Column(db.String(100), nullable=False)
     valueResale = db.Column(db.Float(9), nullable=False)
     cust = db.Column(db.Float(9), nullable=False)
     tax = db.Column(db.Float(9), nullable=True)
     supplier = db.Column(db.String(100), nullable=True)
     qt = db.Column(db.Integer, nullable=False)
     alterResale = db.Column(db.Float(9), nullable=True)
     discount = db.Column(db.Float(9), nullable=True)
     description = db.Column(db.Text, nullable=True)
     datePurchase = db.Column(db.Date, nullable=False)
     dateShelf = db.Column(db.Date, nullable=False)
     token = db.Column(db.String(64), unique=True, nullable=False)


     cart = db.relationship(cart_models.Cart, backref="products", lazy="dynamic")




# if __name__ == '__main__' :
#     from sqlalchemy.orm import declarative_base, relationship, sessionmaker
#     from sqlalchemy import create_engine, Column, Integer, Float, String, Date, Text
#     from sqlalchemy.orm import declarative_base
#     USERNAME = 'root'
#     PASSWORD = '1234'
#     SERVER = 'localhost'
#     DB = 'E_COMMERCE'
#     engine = create_engine(f'mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}', echo=True)
#     session = sessionmaker(bind=engine)()

#     Base = declarative_base()

#     class Product(Base):
#         __tablename__="products"
#         id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
#         prodName = Column(String(100), nullable=False)
#         valueResale = Column(Float(9), nullable=False)
#         cust = Column(Float(9), nullable=False)
#         tax = Column(Float(9), nullable=True)
#         supplier = Column(String(100), nullable=True)
#         qt = Column(Integer, nullable=False)
#         alterResale = Column(Float(9), nullable=True)
#         discount = Column(Float(9), nullable=True)
#         description = Column(Text, nullable=True)
#         datePurchase = Column(Date, nullable=False)
#         dateShelf = Column(Date, nullable=False)
#         token = Column(String(64), unique=True, nullable=False)




#     teste = Product(prodName='SDAS', valueResale=2.5, cust=3.5, tax=5.5, supplier='alguem', qt=5, alterResale=5.5, discount=3.2, description='dasdasdas', token='sakdjhaskdjaslkdjaskldjasdklasldsdfashfjk')

#     session.add_all([teste])