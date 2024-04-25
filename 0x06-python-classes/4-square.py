#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """ represents the square
    Attributes:
        __size(int): one side of the square
        """

    def __init__(self, size=0):
        """ Initializes the square
        Args:
        __size(int):one side of the square
        Returns:
        None"""
        self.size = size

    def area(self):
        """ Calculates the area of a square
        Returns:
        Area of the square"""
        return (self.__size) ** 2

    @property
    def size(self):
        """ getter of size
        Return:
        size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ setter of __size
        args:
            value(int):  the size of square
        returns:
            None
            """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
