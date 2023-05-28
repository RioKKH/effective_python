#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Regarding polymorphism, class methods can indeed be used
to implement this concept. In the context of object-oriented programming,
polymorphism refers to the ability of an object to behave in multiple ways,
depending on its type or class.

Here is an example of how @classmethod could be used in a polymorphic context:
"""


class Animal:
    # class-level attribute
    name = 'Animal'

    @classmethod
    def sound(cls):
        return f'I am {cls.name}, I do not have a specific sound.'


class Dog(Animal):
    # class-level attribute
    name = 'Dog'

    @classmethod
    def sound(cls):
        return f'I am a {cls.name}, I say woof-woof.'


class Cat(Animal):
    name = 'Cat'

    @classmethod
    def sound(cls):
        return f'I am a {cls.name}, I say meow-meow.'


class Hose(Animal):
    name = "hose"

    def sound(cls):
        return f'I am a {cls.name}, I say hihi-nn.'


def make_sound(animal_class):
    print(animal_class.sound())

"""
In this example, we define a general Animal class with a sound class method,
and then subclass Animal to create Dog and Cat classes,
each with its own implementation of the sound class method.

This demonstrates polymorphism: the function make_sound takes an animal class
as an argument and calls its sound method.
The specific behavior of the sound method depends on the class
that is passed to make_sound, even though the interface is the same.
"""

make_sound(Animal) # I am Animal, I do not have a specific sound.
make_sound(Dog) # I am a Dog, I say woof-woof.
make_sound(Cat) # I am a Cat, I say meow-meow.    
# Error since sound method uses cls as an argument but this is
# not class method so no cls is given.
make_sound(Hose) 

