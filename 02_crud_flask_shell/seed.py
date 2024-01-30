#contains seed file, create instances 
from faker import Faker # add faker 
from random import choice as rc

from app import app 
from models import Coffee, db 

with app.app_context(): # create app context with app.app_context()
    Coffee.query.delete()

    fake = Faker() # create and initialize a faker generator

    coffee_list = [] #create an empty list

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
            name= rc(["Double Espresso", "Iced Americano", "Frappuccino", "Latte", "Macchiato", "Chai Latte", "Mocha", "Matcha"]),
            image = fake.image_url(),
            price = rc([3.50, 4.50, 4.00, 2.00, 1.50, 7.00, 4.00, 0.99]),
            description = fake.catch_phrase()
        )
        coffee_list.append(cup)

    db.session.add_all([cappuccino, espresso])
    db.session.add_all(coffee_list)

    db.session.commit() #commit! 

    print(" DONE SEEDING!!👌🎍😍")