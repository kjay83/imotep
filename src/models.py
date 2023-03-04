# models.py

from datetime import datetime
from config import db, ma

class People(db.Model):
    __tablename__ = "people"
    id = db.Column(db.Integer, primary_key=True)
    unique_reference = db.Column(db.String(32), unique=True)
    lname1 = db.Column(db.String(32))
    lname2 = db.Column(db.String(32))
    fname1 = db.Column(db.String(32))
    fname2 = db.Column(db.String(32))
    email1 = db.Column(db.String(32))
    email2 = db.Column(db.String(32))
    address1 = db.Column(db.String(32))
    address2 = db.Column(db.String(32))
    phone1 = db.Column(db.String(32))
    phone2 = db.Column(db.String(32))
    sex = db.Column(db.String(32))
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

class PeopleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = People
        load_instance = True
        sqla_session = db.session

people_schema = PeopleSchema()
peoples_schema = PeopleSchema(many=True)