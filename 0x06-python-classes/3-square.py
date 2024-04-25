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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Calculates the area of a square
        Returns:
        Area of the square"""
        return (self.__size) ** 2
