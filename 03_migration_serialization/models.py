#When a model class inherits from the SerializerMixin, we have access to to_dict(), converts the sql obj -> dict
from sqlalchemy_serializer import SerializerMixin
 
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Coffee(db.Model, SerializerMixin):#Coffee inherits from SerializerMixin
    __tablename__ = "coffees"

    id = db.Column(db.Integer, primary_key=True)

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    name = db.Column(db.String)
    price = db.Column(db.Float)
    image = db.Column(db.String)
    description = db.Column(db.String)

    def __repr__(self):
        return f'<Coffee {self.id}, {self.name}, {self.price}>'
 
class Customer(db.Model):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __repr__(self):
       return f'<Customer {self.id}, {self.name}>'
