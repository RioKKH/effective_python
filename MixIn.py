#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
In Python and other object-oriented programming languages, 
a mix-in is a type of multiple inheritance 
where a class is designed to provide some specific capability
or functionality, and then mixed in to other classes to add this capability.

A mix-in class does not make much sense by itself,
and is not intended to be instantiated on its own.
Instead, its methods and attributes are meant to be used by other classes.
Mix-in classes can be combined with other classes in various ways
to create more complex functionality. This is a form of composition,
and is a powerful tool for making code more modular and reusable.

Here's a simple example of how a mix-in might be used in Python:
"""

class Vehicle:
    pass

class FlyingMixin:
    def fly(self):
        print("Flying...")

class Airplane(Vehicle, FlyingMixin):
    pass

plane = Airplane()
plane.fly()  # prints: Flying...

"""
In this example, the `FlyingMixin` class provides a `fly` method.
The `Airplane` class then inherits from both `Vehicle` and `FlyingMixin`,
meaning that an instance of `Airplane` has the `fly` method available to it.

By convention, mix-ins in Python are often named with a "Mixin" suffix
to make their purpose clear.

It's also typical for mix-ins to not have their own instance variables 
or require a specific initialization, because this allows them 
to be used more flexibly. A mix-in should not depend on the details
of the other classes from which an object inherits.

Here is a more complex example, illustrating the flexibility of mix-ins:
"""

class Vehicle:
    def move(self):
        print("Moving...")

class FlyingMixin:
    def fly(self):
        print("Flying...")

class SwimmingMixin:
    def swim(self):
        print("Swimming...")


class Airplane(Vehicle, FlyingMixin):
    name = "Airplane"
    def __init__(cls):
        print("###", cls.name)

class AmphibiousCar(Vehicle, SwimmingMixin, FlyingMixin):
    name = "Amphiboius car"
    def __init__(cls):
        print("###", cls.name)


plane = Airplane()
plane.move() # prints: Moving
plane.fly() # prints: Flying

car = AmphibiousCar()
car.move() # prints: Moving...
car.swim() # prints: Swimming...
car.fly() # prints: Flying...

"""
In this example, Airplane and AmphibiousCar classes inherit
from the Vehicle base class but mix in different capabilities.
The Airplane class can fly, while the AmphibiousCar class can both fly and swim.
This illustrates how mix-ins can be used to compose classes
with complex behaviors from simpler, reusable components.
"""

