#contains seed file, create instances 
from app import app 
from models import Coffee, db 

with app.app_context(): # create app context with app.app_context()
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

    db.session.add_all([cappuccino, espresso])
    db.session.commit() #commit! 

    print(" DONE SEEDING!!👌🎍😍")