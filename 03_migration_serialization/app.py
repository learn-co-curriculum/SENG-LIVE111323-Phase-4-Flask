# set up flask app configuration, create routes, return responses, take information from our requests

# set up imports 
from flask import Flask, make_response, jsonify # importing an instance of flask class 
#this will be our WSGI (Web Server Gateway Interface )

from flask_migrate import Migrate #for migration of table 

from models import db, Coffee # import sql  alchemy 
#database Coffee class 

# create instances of Flask class
app = Flask(__name__) #for Flask to know where to look for 


# configuration  
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///app.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# migrate the Coffee model 
migrate = Migrate(app, db)

# connect the db to the app
db.init_app(app)


# navigate to seed



# create dynamic routes 
@app.route("/") # route decorator 
def index():
    return '<h1> Hello World!  </h1>'


@app.route('/the-most-expensive-coffee')
def get_the_most_expensive_coffee():
    #query to find the most expensive coffee
    # enter into flask shell to get the object 
    coffee = Coffee.query.order_by(Coffee.price.desc()).first()

    cup = {
        "name": coffee.name,
        "description": coffee.description,
        "price": coffee.price
    }

    # jsonify and return the response  
    return make_response(jsonify(cup), 200) #status code 

#create a dynamic route 
@app.route('/coffees/<string:name>')
def coffee(name):
    quer = Coffee.query.filter_by(name=name).first()

    coffee = {
        "name": quer.name,
        "price": quer.price,
        "description": quer.description
    }
    #return the result as JSON
    return make_response(jsonify(coffee))

@app.route('/coffees/<int:id>')
def coffee_by_id(id):
    cup = Coffee.query.filter(Coffee.id == id).first()

    if cup: 
        # body = {
        #     'id': cup.id,
        #     'name': cup.name,
        #     'price': cup.price
        # }
        body = cup.to_dict()
        status=200
    else:
        body= {
            'message' : f'Coffee {id} not found.'
        }
        status=404

    return make_response(body, status)


@app.route('/names/<string:name>')
def coffee_by_name(name):
    coffees = []

    for coffee in Coffee.query.filter_by(name=name).all():
        coffees.append(coffee.to_dict())

    body={
        'coffee': coffees
    }

    return make_response(body, 200)


# in terminal 
# $flask db init
# $flask db migrate 
# $flask db upgrade 


# $export FLASK_APP=app.py
# $export FLASK_RUN_PORT=5555

if __name__ == '__main__': # if the __name__(current module) is main 
    app.run(port=5555, debug=True) # then run the port at 5555