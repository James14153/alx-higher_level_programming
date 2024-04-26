#!/usr/bin/python3
"""Defines a class square"""


class Square:
    """ represents the square
    attributes:
        size (int): size of ne side of square
        position (tuple): position of the square in 2D space
        """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the class
        Args:
            size (int): size of one side of the square
            position (tuple): position of the square in 2D Space
        Returns:
            Nothing
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ getter for size
        Returns:
            size of the square
         """
        return self.__size

    @size.setter
    def size(self, value):
        """ setter for __size
        Args:
            value (int): size of one side of square
        Return:
            None
        """
        if type(value) is not tuple:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """ getter for position
        Returns:
            position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ setter for position
        Args:
            value (tuple): position of the square
        Return:
            None
        """
        if type(value) is not tuple or len(value) != 2 or \
                type(value[0]) is not int or value[0] < 0 or \
                type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ calculates the area of the square
        Args:
            size (int): one side of the square
        Returns:
            area of the square
            """
        return (self.__size) ** 2

    def my_print(self):
        """ prints the square using #"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for j in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
