#!/usr/bin/python3
"""
This module defines the CountedIterator class.
"""


class CountedIterator:
    """
    CountedIterator is an iterator that keeps track of the number of elements
    it has iterated over.
    """
    def __init__(self, iterator, counter=0):
        """
        Initializes CountedIterator with an iterator and an optional counter
        """
        self.iterator = iter(iterator)
        self.counter = counter

    def get_count(self):
        """
        Returns the current count of the iterator.
        """
        return self.counter

    def __next__(self):
        """
        Return the next item from the iterator and increment the counter.
        """
        item = next(self.iterator)
        self.counter += 1
        return item
