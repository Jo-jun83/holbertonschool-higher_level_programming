#!/usr/bin/python3
"""
Module for singly linked list implementation.

This module defines a Node class for creating nodes in a linked list
and a SinglyLinkedList class for managing a sorted singly linked list.
"""


class Node:
    """Defines a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """
        Initialize a new Node.

        Args:
            data (int): The data value of the node.
            next_node (Node, optional): The next node in the linked list.
                Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve the data stored in the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """
        Set the data value, ensuring it's an integer.

        Args:
            value (int): The value to store.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve the next node in the linked list."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set the next node, ensuring it's either None or a Node object.

        Args:
            value (Node or None): The next node in the list.

        Raises:
            TypeError: If value is not None or a Node instance.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list with sorted insert functionality."""

    def __init__(self):
        """Initialize an empty linked list."""
        self.__head = None

    def sorted_insert(self, value):
        """
        Insert a new Node into the correct sorted position in the list.

        Args:
            value (int): The value to insert into the list.
        """
        new_node = Node(value)

        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """
        Return a string representation of the linked list.

        The elements are printed one per line, in ascending order.
        """
        values = []
        current = self.__head
        while current is not None:
            values.append(str(current.data))
            current = current.next_node
        return "\n".join(values)
