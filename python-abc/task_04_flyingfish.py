#!/usr/bin/python3
"""
This module defines three classes: Fish, Bird, and FlyingFish.
"""


class Fish:
    """
    A module that defines a Fish class.
    """
    def swim(self):
        """
        Prints a message indicating that the fish is swimming.
        """
        print("The fish is swimming")

    def habitat(self):
        """
        Prints a message indicating where the fish lives.
        """
        print("The fish lives in water")


class Bird:
    """
    A class used to represent a Bird
    """
    def fly(self):
        """
        Prints a message indicating that the bird is flying.
        """
        print("The bird is flying")

    def habitat(self):
        """
        Prints a message indicating where the bird lives.
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    FlyingFish class that inherits from both Fish and Bird classes.
    This class represents a flying fish
    """
    def fly(self):
        """
        Prints a message indicating that the Flyingfish is flying.
        """
        print("The flying fish is soaring!")

    def swim(self):
        """
        Prints a message indicating that the flyingfish is swimming.
        """
        print("The flying fish is swimming!")

    def habitat(self):
        """
        Prints a message indicating where the Flyingfish lives.
        """
        print("The flying fish lives both in water and the sky!")
