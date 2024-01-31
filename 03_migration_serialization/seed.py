#contains seed file, create instances 
from faker import Faker # add faker 
from random import choice as rc

from app import app 
from models import Coffee, Customer, db 

with app.app_context(): # create app context with app.app_context()
    Coffee.query.delete()
    Customer.query.delete()

    fake = Faker() # create and initialize a faker generator

    coffee_list = [] #create an empty list
    customer_list = []

    #create some seeds for coffee and commit them to the db
    cappuccino = Coffee(
        name="cappuccino",
        image="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Cappuccino_at_Sightglass_Coffee.jpg/440px-Cappuccino_at_Sightglass_Coffee.jpg",
        price=4.50,
        description="steamed milk and foam on top of a shot of espresso"
    )

    espresso = Coffee(
        name="espresso",
        image = "espresso.jpeg",
        price=3.50,
        description="the concentrated coffee, very strong!"
    )

    for c in range(250):
        cup = Coffee(
            name= rc(["doubleespresso", "icedamericano", "frappuccino", "latte", "macchiato", "chailatte", "mocha", "matcha"]),
            image = fake.image_url(),
            price = rc([3.50, 4.50, 4.00, 2.00, 1.50, 7.00, 4.00, 0.99]),
            description = fake.catch_phrase()
        )
        coffee_list.append(cup)

    for c in range(5):
        cust = Customer(
            name=fake.name()
        )
        customer_list.append(cust)
        
    print(customer_list)

    for customer in customer_list:
        print(customer.name)

    db.session.add_all([cappuccino, espresso])
    db.session.add_all(coffee_list)
    db.session.add_all(customer_list)

    db.session.commit() #commit! 

    print(" DONE SEEDING!!👌🎍😍")