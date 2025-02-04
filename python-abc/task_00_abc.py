#!/usr/bin/python3
"""
This module defines an abstract base class `Animal`
and its concrete subclasses `Dog` and `Cat`.
"""


from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Animal is an abstract base class that defines the blueprint
    for all animal classes.

    Methods:
        sound: An abstract method that must be implemented by any subclass.
        It should define the sound the animal makes.
    """

    @abstractmethod
    def sound(self):
        """
        Produces the sound specific to the object.
        """
        pass


class Dog(Animal):
    """
    Represents a Dog which is a subclass of Animal.
    """
    def sound(self):
        """
        Returns the sound made by the animal.
        """
        return "Bark"


class Cat(Animal):
    """
    Represents a Cat which is a subclass of Animal.
    """
    def sound(self):
        """
        Returns the sound made by the animal.
        """
        return "Meow"
