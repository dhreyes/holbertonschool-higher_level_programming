#!/usr/bin/python3
""" Learn how to do a linked list with OOP """


class Node:
    """ This will be the setup for class Node """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ Getter for data in class Node """
        return self.__data

    @data.setter
    def data(self, value):
        """ Method for setting new value to data """
        if type(value) is not int:
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """ getter for the value next_node """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ setter for updating value of next_node """
        if not isinstance(value, Node) and value is not None:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """ This class will be for the actual linked list """
    def __init__(self):
        """ This will initiate the first instance of the list (head) """
        self.__head = None

    def sorted_insert(self, value):
        """ This will insert a node into the class SinglyLinkedList """
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            change_node = self.__head
            while (change_node.next_node is not None and
                    change_node.next_node.data < value):
                change_node = change_node.next_node
            new_node.next_node = change_node.next_node
            change_node.next_node = new_node

    def __str__(self):
        """ This will allow the main function to print the values of list """
        linklist = []
        change_node = self.__head
        while change_node is not None:
            linklist.append(str(change_node.data))
            change_node = change_node.next_node
        return ('\n'.join(linklist))
