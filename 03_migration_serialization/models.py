
from sqlalchemy_serializer import SerializerMixin
#we will have access to `to_dict()` sql obj => python dictionary

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData()


db = SQLAlchemy(metadata=metadata)


class Coffee(db.Model, SerializerMixin): 
    __tablename__ = "coffees" #table name is coffees

    #set up columns 
    id = db.Column(db.Integer, primary_key=True)

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    # server default is sql keyword 

    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    #columns 
    name = db.Column(db.String)
    price = db.Column(db.Float)
    image = db.Column(db.String)
    description = db.Column(db.String)

    def __repr__(self):
        return f'<Coffee {self.id}, {self.name}, {self.price} >'


class Customer(db.Model, SerializerMixin):
    __tablename__="customers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    address = db.Column(db.String)
    phone = db.Column(db.String)
    emoji = db.Column(db.String)

    def __repr__(self):
        return f'<Customer {self.id}, {self.name}>'

