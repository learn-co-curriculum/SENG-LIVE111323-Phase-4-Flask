## 004 Relationship
* Use Flask-SQLAlchemy to join models with many-to-many relationship between models.
* Review relationships, Primary keys, and Foreign keys
* Review back_populates property


### back_populates vs. backref 

* back_populates : is a property to establish a `bi-directional` relationship between models. The relationship are propagated to the other side. 

* backref: automatically creates a reverse relationship on the other side. ( less explicit than the back_populates, more flexible, simpler)

```
class Parent():
    children = relationship("Child", backref="parent")
class Child():
    pass

```

```
class Parent():
    children = relationship("Child", back_populates="parent")
class Child():
    parent = relationship("Parent", back_populates="child")
```