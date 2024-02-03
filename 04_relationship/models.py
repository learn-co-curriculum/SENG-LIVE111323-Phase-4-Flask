from sqlalchemy_serializer import SerializerMixin
#we will have access to `to_dict()` sql obj => python dictionary

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

from sqlalchemy.ext.associationproxy import association_proxy

metadata = MetaData(naming_convention = {
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    })
#fk : foreign key constraints

db = SQLAlchemy(metadata=metadata)

class Coffee(db.Model, SerializerMixin): 
    __tablename__ = "coffees" #table name is coffees

    serialize_rules = ('-orders.coffee', )
    # serialize_only = ('id', 'name', )

    #set up columns 
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    name = db.Column(db.String)
    price = db.Column(db.Float)
    image = db.Column(db.String)
    description = db.Column(db.String)

    #relationship mapping the coffee to related 'orders'
    # orders = db.relationship('Order', 
    #                          back_populates='coffee', cascade='all, delete-orphan')
    orders = db.relationship('Order', 
                             backref='coffee', cascade='all, delete-orphan')
    
    #association proxy to get customers for this coffee through orders
    # customers = association_proxy('orders', 'customer', creator=lambda customer_obj: Order(customer=customer_obj))


    def __repr__(self):
        return f'<Coffee {self.id}, {self.name}, {self.price} >'


class Customer(db.Model, SerializerMixin):
    __tablename__="customers"

    serialize_rules = ('-orders.customer', )

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    address = db.Column(db.String)
    phone = db.Column(db.String)
    emoji = db.Column(db.String)

    #add the relationship mapping the customer to related order
    # orders = db.relationship('Order', back_populates='customer', cascade='all, delete-orphan')  
    orders = db.relationship('Order', backref='customer', cascade='all, delete-orphan')    

    #association proxy to get customers for this coffee through orders
    coffee = association_proxy('orders', 'coffee', creator=lambda coffee_obj: Order(coffee=coffee_obj))

    def __repr__(self):
        return f'<Customer {self.id}, {self.name}>'
    

class Order(db.Model, SerializerMixin): #intermediary class/ join table
    __tablename__="orders"

    serialize_rules = ('-coffee.orders', '-customer.orders', )

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime
                     )
    #foreign keys 
    coffee_id = db.Column(db.Integer, db.ForeignKey('coffees.id'))
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))

    #relationship mapping the order to related coffee
    # coffee = db.relationship('Coffee', back_populates='orders')
    # customer = db.relationship('Customer', back_populates='orders')

    # relationship(): this method allows one model to access its related model 
    #back_populates attributes is used to define a `bi-directional` relationship between 2 models. 
    

    def __resp__(self):
        return f'< Order {self.id}, {self.date}, {self.coffee.name}, {self.customer.name} >'



