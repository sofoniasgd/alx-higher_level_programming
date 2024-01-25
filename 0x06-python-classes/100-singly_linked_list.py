#!/usr/bin/python3
"""node class module for task 7."""


class Node:
    """Define Node class."""
    def __init__(self, data, next_node=None):
        """define private size attribute
        Args:
            data (int): node data
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """retrieve data attribute"""
        return self.__data

    @data.setter
    def data(self, value):
        """setter for the attriubte data.
        check if data is an int, raise typeerror if not.
        Args:
        value (int): data of node
        """
        if (not isinstance(value, int)):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """retrieve next node of linked list attribute"""
        return self.__next_node
    
    @next_node.setter
    def next_node(self, value):
        """setter for the attriubte next_node.
        check if value is an Node instance, raise typeerror if not.
        Args:
        value (Node): next node of the linkedlist
        """
        if not (isinstance(value, Node) or None):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value

class SinglyLinkedList:
    """Define a singly linked list class."""


    Node head
    def __init__(self):
        head = None
    def sorted_insert(self, value):
        """insert method to the list"""

        if head is None:
            head = Node
