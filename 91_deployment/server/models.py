from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin

from config import db, bcrypt

class Coffee(db.Model, SerializerMixin): 
    __tablename__ = "coffees" 

    serialize_rules = ('-orders.coffee', )

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    name = db.Column(db.String)
    price = db.Column(db.Float)
    image = db.Column(db.String)
    description = db.Column(db.String)

    # Relationship mapping the coffee to related orders
    orders = db.relationship('Order', back_populates='coffee', cascade='all, delete-orphan')

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
 
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

    #Relationship mapping the customer to related orders
    orders=db.relationship(
        'Order', back_populates='customer', cascade='all, delete-orphan'
    )
    #back_populates attribute is used to define a bidirectional relationship
    
    #back_populates:how changes made to one side of the relationship should be reflected on the other side. 


    def __repr__(self):
        return f'<Customer {self.id}, {self.name}>'

class Order(db.Model, SerializerMixin):#intermidiary class / join table
    __tablename__="orders"

    serialize_rules = ('-coffee.orders', '-customer.orders', )

    id=db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)

    # Foreign key to store the coffee id
    coffee_id = db.Column(db.Integer, db.ForeignKey('coffees.id'))
    #Foreign key to store the customer id
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))

    # Relationship mapping the order to related coffee
    coffee = db.relationship('Coffee', back_populates='orders')
    #back_populates attribute is used to define a bidirectional relationship between two tables or models
    #back_populates:how changes made to one side of the relationship should be reflected on the other side.

    # Relationship mapping the order to related customer
    customer=db.relationship('Customer', back_populates='orders')

    def __repr__(self):
        return f'<Order {self.id}, {self.date}, {self.coffee.name}, {self.customer.name}>'
    

class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    serialize_rules = ("-_password_hash", "-coffees.user", )

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    _password_hash = db.Column(db.String)
    # '_' underscore is for internal use 
    #bcrypt will have access to the pw 

    coffees = db.relationship('Coffee', backref='user')

    @hybrid_property
    #decorator from SQLAlchemy -- getter / setter 
    
    #getter 
    def password_hash(self):
        #return self._password_hash 
        raise AttributeError('Password Hashes should not be viewed! ')
    
    #setter
    @password_hash.setter
    def password_hash(self, password):
        #1. password.encode('utf-8') ---https://docs.python.org/3/howto/unicode.html
        #2. bcrypt.generate_password_hash() ---- https://flask-bcrypt.readthedocs.io/en/1.0.1/
        #3. save it in the variable
        new_hashed_password = bcrypt.generate_password_hash(password.encode('utf-8'))

        #set the hashed pw
        self._password_hash  = new_hashed_password.decode('utf-8')

    #login 
    def authenticate(self, password):
        return bcrypt.check_password_hash(
            self._password_hash, # from DB 
            password.encode('utf-8') # user passed in pw, argument
        )
    
    def __repr__(self):
        return f'<User {self.id} username: {self.name}>'