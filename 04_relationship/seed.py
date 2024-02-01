#contains seed file, create instances 
from faker import Faker # add faker 
from random import choice as rc
from sqlalchemy import func

from app import app 
from models import Coffee, Customer, Order, db 

with app.app_context(): # create app context with app.app_context()
    Coffee.query.delete()
    Customer.query.delete()
    Order.query.delete()

    fake = Faker() # create and initialize a faker generator

    coffee_list = [] #create an empty list
    customer_list = []
    order_list = []

    #create some seeds for coffee and commit them to the db
    mochacappuccino = Coffee(
        name="mochacappuccino",
        image="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Cappuccino_at_Sightglass_Coffee.jpg/440px-Cappuccino_at_Sightglass_Coffee.jpg",
        price=4.50,
        description="steamed milk and foam on top of a shot of espresso with delicious chocolate"
    )

    zaquari = Customer(
        name="Zaquary",
        address = fake.address(),
        phone= fake.phone_number(),
        emoji = fake.emoji()
    )

    o1 = Order(
        date = func.now(),
        customer = zaquari,
        coffee=mochacappuccino
    )

    db.session.add_all([mochacappuccino, zaquari, o1])
    db.session.commit() #commit! 
    print(" DONE SEEDING the FIRST ORDER !!👌🎍😍")


    espresso = Coffee(
        name="espresso",
        image = "espresso.jpeg",
        price=3.50,
        description="the concentrated coffee, very strong!"
    )

    for c in range(8):
        cup = Coffee(
            name= rc(["doubleespresso", "icedamericano", "frappuccino", "latte", "macchiato", "chailatte", "mocha", "matcha"]),
            image = fake.image_url(),
            price = rc([3.50, 4.50, 4.00, 2.00, 1.50, 7.00, 4.00, 0.99]),
            description = fake.catch_phrase()
        )
        coffee_list.append(cup)

    for c in range(20):
        customer = Customer(
            name=fake.name(),
            address = fake.address(),
            phone = fake.phone_number(),
            emoji = fake.emoji()
        )
        customer_list.append(customer)

    db.session.add_all(coffee_list)
    db.session.add_all(customer_list)
    db.session.commit() #commit! 
    print(" ---COFFEE and CUSTOMER have been added !!👌🎍😍")

    customer_rec = Customer.query.all()
    coffee_rec = Coffee.query.all()

    for o in range(20):
        order = Order(
            date=fake.date_time(),
            customer_id=rc([customer.id for customer in customer_rec]),

            coffee_id = rc([coff.id for coff in coffee_rec])
        )
        order_list.append(order)

    db.session.add_all([espresso])
    db.session.add_all(order_list)

    db.session.commit() #commit! 

    print(" DONE SEEDING!!👌🎍😍")