from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Coffee(db.Model):
    __tablename__ = "coffees"

    id = db.Column(db.Integer, primary_key=True)

    create_at = db.Column(db.DateTime, server_default=db.func.now())

    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    name = db.Column(db.String)
    image = db.Column(db.String)
    price = db.Column(db.Float)
    description = db.Column(db.String)
    