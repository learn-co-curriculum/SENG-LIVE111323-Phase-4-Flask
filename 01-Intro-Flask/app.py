from flask import Flask, jsonify, make_response 

from flask_migrate import Migrate 
from models import db, Coffee 

app = Flask(__name__) 

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///app.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route("/")
def index():
    return '<h1> Hello World!! </h1>'

@app.route("/the-most-expensive-coffee")
def get_the_most_expensive_coffee():
    # 7c. Query for the lowest budget coffees

    coffee = Coffee.query.order_by(Coffee.price).first()
     #descending order
   
    cup = {
        "name": coffee.name,
        "description": coffee.description,
        "price": coffee.price
    }
    # 7d. Jsonify and return the response
    return make_response(jsonify(cup), 200)

@app.route('/coffees/<string:name>')
def coffee(name):
    return make_response(jsonify(name))


if __name__ == '__main__':
    app.run(port=5555, debug=True)