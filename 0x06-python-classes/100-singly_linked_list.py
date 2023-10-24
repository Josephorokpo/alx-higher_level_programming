#!/usr/bin/python3
"""A class Node that defines a node of a singly linked lis."""


class Node:
    """Represents a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """
        Initializes a new Node object.

        Args:
            data (int): The data to store in the node.
            next_node (Node, optional): The next node in the list.
            Defaults to None.

        Raises:
            TypeError: If data is not an integer.
            TypeError: If next_node is not a Node object.
        """
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data

        if next_node is not None and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node

    @property
    def data(self):
        """Gets the data stored in the node."""
        return self.__data

    @property
    def next_node(self):
        """Gets the next node in the list."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the next node in the list.

        Args:
            value (Node or None): The next node to set.

        Raises:
            TypeError: If value is not a Node object when it's not None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """Represents a singly linked list."""

    def __init__(self):
        """Initializes a new SinglyLinkedList object."""
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list
        (in increasing order).

        Args:
            value (int): The value to insert into the list.
        """
        new_node = Node(value)
        if self.__head is None or self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node and current.next_node.data <= value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the list,
        printing each node on a new line.

        Returns:
            str: The string representation of the list.
        """
        result = []
        current = self.__head
        while current:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)
