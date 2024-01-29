from app import app
from models import Coffee, db

with app.app_context():
    Coffee.query.delete()

    cappuccino = Coffee(
        name = "cappuccino",
        image="https://helios-i.mashable.com/imagery/articles/01NoLVpLw0DGTeQB9CfEp2s/hero-image.fill.size_1200x675.v1614273949.jpg",
        price=4.50,
        description="steamed milk and foam on top of a shot of espresso"
    )

    espresso = Coffee(
        name = "espresso",
        image="https://cdn.apartmenttherapy.info/image/upload/f_auto,q_auto:eco,c_fill,g_center,w_730,h_913/stock%2FGettyImages-1270218142",
        price=3.50,
        description="The concentrated coffee made by forcing pressurized hot water through finely ground coffee beans"
    )


    db.session.add_all([cappuccino, espresso])
    db.session.commit()

    print("DONE SEEDING 👌🎍😍 ")