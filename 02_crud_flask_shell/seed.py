#contains seed file, create instances 
from random import choice as rc
from faker import Faker

from app import app 
from models import Coffee, db 

with app.app_context(): # create app context with app.app_context()
    fake = Faker()
    
    coffee_list = []

    Coffee.query.delete()

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

    for n in range(25):
        cup = Coffee(
            name=rc([ "Double Espresso", "Red Eye", "Black Eye", "Americano", "Long Black", "Macchiato", "Long Macchiato", "Cortado", "Breve", "Flat White", "Cafe Latte", "Mocha", "Vienna", "Affogato", "Cafe au Lait", "Iced Coffee"]),
            image = fake.image_url(),
            price=rc([3.50, 4.00, 4.50, 5.00, 5.50, 7.00]),
            description = fake.catch_phrase()
        )
        coffee_list.append(cup)

    db.session.add_all([cappuccino, espresso])
    db.session.add_all(coffee_list)
    db.session.commit() #commit! 

    print(" DONE SEEDING!!👌🎍😍")