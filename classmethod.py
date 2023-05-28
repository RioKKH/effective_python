#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
In Python, @classmethod is a decorator that can be used to define a method
within a class that takes the class object as the first parameter.

This is distinct from an instance method, which takes the instance of a class
(usually denoted as self) as the first parameter.

A class method can be called on the class directly,
without creating an instance of the class. This can be particularly useful
when you want the method to be able to alter the class state,
not the state of individual instances.
"""
class MyClass:
    # class-level attribute: greeting
    greeting = "Hello, World"

    @classmethod
    def greet(cls):
        print(cls.greeting)


MyClass.greet() # prints: Hello, World
