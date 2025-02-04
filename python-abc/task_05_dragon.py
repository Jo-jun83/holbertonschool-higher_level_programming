#!/usr/bin/python3
"""
This module defines mixin classes for swimming and flying capabilities,
"""


class SwimMixin:
    """
    Enables an object to swim.
    """
    def swim(self):
        """
        Makes the creature swim and prints a message indicating the action.
        """
        print("The creature swims!")


class FlyMixin:
    """
    FlyMixin is a mixin class that provides flying capabilities
    to other classes.
    """
    def fly(self):
        """
        Makes the creature swim and prints a message indicating the action.
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Dragon class that inherits from SwimMixin and FlyMixin.
    """
    def roar(self):
        """
        Makes the creature swim and prints a message indicating the action.
        """
        print("The dragon roars!")
