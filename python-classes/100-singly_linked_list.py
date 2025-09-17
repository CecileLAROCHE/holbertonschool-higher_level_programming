#!/usr/bin/python3
"""
    Defines a node of a singly linked list
"""


class Node:

    """
    This class defines a data with private attributes
    Args:
        data (int): .

    Attributes:
        __data (int):
    """

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter: returns the data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter: validates data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter: returns the next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter: validates next_node"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Defines a singly linked list
    """

    def __init__(self):
        self.__head = None

    def __str__(self):
        """Prints the entire list, one node number per line"""
        nodes = []
        current = self.__head
        while current is not None:
            nodes.append(str(current.data))
            current = current.next_node
        return "\n".join(nodes)

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position"""
        new_node = Node(value)

        if self.__head is None or value < self.__head.data:
            # Insert at head
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            # Traverse to find insertion point
            current = self.__head
            while (current.next_node is not None and
                    current.next_node.data < value):
                current = current.next_node
            # Insert in the correct position
            new_node.next_node = current.next_node
            current.next_node = new_node
