## 02 Flask-SQLAlchemy CRUD (Flask Shell)

### - - - - - - crud in flask shell - - - - - - - -
* Use an external library Flask-SQLAlchemy to simplify tasks from earlier ORM lessons.

* Manage database tables and schemas without writing SQL.

* Use the Flask Shell with Flask-SQLAlchemy to create, read, update and delete records in a SQL database.

### - - - - - - Create random fake data in seed file - - - - - - - -
* Initialize a database with sample data
* Use the Faker package to generate random data



# $ flask shell
### CREATE 
>>> iced_americano = Coffee( name="iced americano", price=2.99, description="refreshing and smooth")
>>> iced_americano
<Coffee (transient 4396764176)>
>>> iced_americano.description
'refreshing and smooth'
>>> db.session.add(iced_americano)
>>> db.session.commit()

### READ
* get all the coffees
Coffee.query.all()
[<Coffee 1>, <Coffee 2>, <Coffee 3>, <Coffee 4>]

* get individual coffee name
for coffee in Coffee.query.all():
...     print(coffee.name)

* filter the condition that matches the requirement
>>> Coffee.query.filter(Coffee.name == "cappuccino").all()
[<Coffee 1>]

* access a certain row by its primary key 
>>> Coffee.query.filter_by(id = 3).first()
<Coffee 3>

>>>coffee_3 = db.session.get(Coffee, 3)

* order by the price of the coffee
>>> Coffee.query.order_by('price').all()
[<Coffee 4>, <Coffee 2>, <Coffee 1>, <Coffee 3>]

>>> for coffee in Coffee.query.order_by('price').all():
...     print(coffee.name, coffee.price)
... 
iced americano 2.99
espresso 3.5
cappuccino 4.5
frappuccino 6.0

#### UPDATE


### DELETE