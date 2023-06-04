from api import db


class Sector(db.Model):
    __tablename__ = "sectors"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    name = db.Column(db.String(100), nullable=False)
    token = db.Column(db.String(16), nullable=False, unique=True)


