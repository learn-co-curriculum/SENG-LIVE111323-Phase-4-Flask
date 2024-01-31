# contains model information for our db 

#1. import SQLAlchemy 
from flask_sqlalchemy import SQLAlchemy

#2save SQL Alchemy flask in db var 
db = SQLAlchemy()

#3create a coffee model 
class Coffee(db.Model): # take in sqlalchemy db as an arg
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