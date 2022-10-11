#!/usr/bin/python3
"""Implementation of Singly Linked List"""


class Node:
    """Represent each node in a list"""
    def __init__(self, data, next_node=None):
        """Initialize the object
        Arguments:
            data (int): the data to be stored in the node
            next_node (Node): the next node of the node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """return the data of the node"""
        return (self.__data)

    @data.setter
    def data(self, value):
        """Set the data of the node"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """return the next node of the current node"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """Set the next node of the current node"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        """initialize the Singly LInked List"""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node in a sorted way
        Arguments:
            value (int): value of the node to be inserted"""
        newNode = Node(value)

        if self.__head is None:
            newNode.next_node = None
            self.__head = newNode
        elif self.__head.data > value:
            newNode.next_node = self.__head
            self.__head = newNode
        else:
            tmp = self.__head
            while tmp.next_node is not None and tmp.next_node.data < value:
                tmp = tmp.next_node
            newNode.next_node = tmp.next_node
            tmp.next_node = newNode

    def __repr__(self):
        """Return the string representation of the class SinglyLinkedList"""
        aList = []
        tmp = self.__head
        while tmp is not None:
            aList.append(str(tmp.data))
            tmp = tmp.next_node
        return ("\n".join(aList))
