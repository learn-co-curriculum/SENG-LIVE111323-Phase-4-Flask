import os
from dotenv import load_dotenv
load_dotenv()

from flask import Flask, request, make_response, session, jsonify, abort, render_template
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError

from config import app, api, db

from models import Coffee, Order, Customer, User

from datetime import datetime


@app.route('/')
@app.route('/main')
@app.route('/<int:id>')
def index(id=0):
    return render_template("index.html")


# @app.before_request
# def check_if_logged_in():
#     open_access_list = [
#         'signup',
#         'login',
#         'check_session'
#     ]

#     if request.endpoint not in open_access_list and 'user_id' not in session:
#         abort(401)


# create dynamic routes decorator
# @app.route("/") # route decorator 
# def index():
#     return '<h1> Hello World!  </h1>'

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


#GET, POST /coffees
@app.route('/coffees', methods=['GET', 'POST'])
@app.route('/coffees/', methods=['GET', 'POST'])
def coffees():
    if request.method == "GET":
        coffees = Coffee.query.all()

        coffees_dict = [ coffee.to_dict(only=("name", "description", "price", )) for coffee in coffees ]

        return make_response(coffees_dict, 200)

    elif request.method == "POST":
        #import ipdb; ipdb.set_trace()
        new_coffee_orm_obj = Coffee( #SQLAlchemy model class, Coffee
            name = request.get_json()['name'],
            image = request.get_json()['image'],
            price = request.get_json()['price'],           
            description = request.get_json()['description']
        )

        db.session.add(new_coffee_orm_obj)
        db.session.commit()

        new_coffee_python_dict = new_coffee_orm_obj.to_dict()

        return make_response(jsonify(new_coffee_python_dict), 201) #make_response function turn `new_coffee_python_dict` to a json object


#GET / coffees/:id 
#<int:id> is a dynamic parameter indicating that the id part of the URL should be an integer
@app.route('/coffees/<int:id>', methods=['GET', 'DELETE'])
def coffee_by_id(id):
    #import ipdb; ipdb.set_trace()
    cup = Coffee.query.filter(Coffee.id==id).first()
    if cup:
        if request.method == 'GET':
            body = cup.to_dict() #use to_dict serializer 
            status = 200
        
        elif request.method == 'DELETE':
            #cascade delete logic
            #delete the orders that include coffee #same as delete-orphan in models.py
            #db.relationship('Order', cascade='all, delete-orphan')
            assoc_coffee_item = Order.query.filter(Order.coffee_id == id).all()
            for row in assoc_coffee_item:
                db.session.delete(row)

            db.session.delete(cup)
            db.session.commit()

            body = {}
            status = 204
            
    else:
        body={
            'message': f'Coffee id {id} not found.'
        }
        status = 404

    return make_response(body, status)


# GET /orders
# POST /orders
class Orders(Resource):#this class name should be 
# different from model class name that we are importing
    #Create a route to /orders for GET requests
    def get(self):
        #Create the query
        quer = Order.query.all()

        orders = []
        #Loop through the query and convert each object into 
        # a dictionary then append it to orders list
        for each_o in quer:
            orders.append({
                "id": each_o.id,
                "date": each_o.date,
                "coffee_id": each_o.coffee_id,
                "customer_id": each_o.customer_id
            })

        #Use make_response and jsonify to return a response
        resp = make_response(jsonify(orders), 200)

        return resp
    
    def post(self):
        #import ipdb; ipdb.set_trace()
        date_str = request.get_json()['date']#get the date string
        date_python = datetime.fromisoformat(date_str)#convert it into python time
        new_order_orm_obj = Order(
            date=date_python,
            coffee_id=request.get_json()['coffee_id'],
            customer_id=request.get_json()['customer_id']
        )
        #Add and commit to db
        db.session.add(new_order_orm_obj)
        db.session.commit()

        #Convert orm obj to dictionary
        order_dict = {
            "id": new_order_orm_obj.id,
            "coffee_id": new_order_orm_obj.coffee_id,
            "customer_id": new_order_orm_obj.customer_id,
            "date": new_order_orm_obj.date
        }


        response = make_response(jsonify(order_dict), 201)

        return response #return as JSON

api.add_resource(Orders, '/orders')
#api from flask restful, add Orders class and the URL route for the endpoint.


# PATCH /customers/:id
# DELETE /customers/:id

class Customers(Resource):
    def patch(self, id):
        #import ipdb; ipdb.set_trace() #breakpoint
        id_customer = Customer.query.filter(Customer.id == id).one_or_none()

        if id_customer:
            #import ipdb; ipdb.set_trace() #breakpoint
            for key in request.get_json():#loop through the keys in the JSON
                setattr(id_customer, key, request.get_json()[key])
                # set the attributes with the new values

            db.session.add(id_customer)#add the updated object to the db
            db.session.commit()#commit the change to the db

            return make_response(jsonify(id_customer.to_dict()), 200)

        return make_response(jsonify({"error": "Customer Not Found"}), 404)
    
    def delete(self, id):
        id_customer = Customer.query.filter(Customer.id == id).one_or_none()
        if id_customer:
            quer = Customer.query.filter(Customer.id==id).first()
            db.session.delete(quer)
            db.session.commit()
                
            return make_response("Deleted :D ", 200)
        return make_response(jsonify({"error": "Customer Not Found"}), 404)

api.add_resource(Customers, '/customers/<int:id>')


class Users(Resource):
    def get(self):
        all_users = [ users.to_dict() for users in User.query.all()]
        return make_response(all_users, 200)

api.add_resource(Users, '/users')


class Signup(Resource):
    def post(self): #define the POST / sign up method
        new_user = User(
            name = request.get_json()['name']
            # _password_hash = request.get_json()['password']
        )


        try: 
            new_user.password_hash = request.get_json()['password']
            #use the setter method to set password
            
            db.session.add(new_user)
            db.session.commit()

            session['user_id'] = new_user.id # save the new user's id in the session so the user is saved in the session

            #import ipdb; ipdb.set_trace()
            response = make_response(
                new_user.to_dict(),
                201
            )
            return response
        except IntegrityError:
            return {'error': '422 Unprocessable Entity'}, 422

api.add_resource(Signup, '/signup')


class Login(Resource):
    def post(self):
        #import ipdb; ipdb.set_trace()
        # user = User.query.filter_by(name=request.get_json()['name']).one_or_none()
        user = User.query.filter(User.name == request.get_json()['name']).first()
        # import ipdb; ipdb.set_trace()        
        if user and user.authenticate(request.get_json()['password']):
            #.authenticate is the method we built in models.py
            #check if used passed in pw is correct using the .authenticate method.
            session['user_id'] = user.id  #if correct then create session to login
            #import ipdb; ipdb.set_trace()
            response = make_response(
                user.to_dict(),
                200
            )
            print(session)
            return response
        else:
            return make_response({"ERROR":"Incorrect"}, 400)
        
api.add_resource(Login, '/login')


# 6.1 Create a class Logout that inherits from Resource 
class Logout(Resource):
    # 6.2 Create a method called delete
    def delete(self):
    # 6.3 Clear the user id in session by setting the key to None
        session['user_id'] = None
        session.clear()
    # 6.4 create a 204 no content response to send back to the client
        response = make_response({}, 200)
        return response
api.add_resource(Logout, '/logout')

class CheckSession(Resource):
    def get(self):
        #import ipdb; ipdb.set_trace()
        # user = User.query.filter_by(id = session.get('user_id')).first()

        user = User.query.filter(User.id == session['user_id']).first()


        if user:
            response = make_response(
                user.to_dict(),
                200
            )
            #import ipdb; ipdb.set_trace()
            return response
        else:
            abort(401)
api.add_resource(CheckSession, '/check_session')



# in terminal 
# $flask db init
# $flask db migrate 
# $flask db upgrade 


# $export FLASK_APP=app.py
# $export FLASK_RUN_PORT=5555

if __name__ == '__main__': # if the __name__(current module) is main 
    app.run(port=5555, debug=True) # then run the port at 5555