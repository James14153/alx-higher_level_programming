#!/usr/bin/python3
"""Defines a class square"""


class Square:
    """represents the square
    Attributes:
        size(int): one side of the square
    """
    def __init__(self, size):
        """ initializes the square
        args:
            size (int): this is one side of the square
        Returns:
            None
        """
        self.__size = size

    @property
    def size(self):
        """ getter of __size
        Returns:
            the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter of __size
        Args:
            value (int): the size of one side of the square
        Returns:
            Nothing
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """calculates the area of the square
        Returns:
            area of the square
        """
        return (self.__size) ** 2

    def my_print(self):
        """prints out the square with the character #
        Args:
            size (int): one side of the square
        Returns:
            nothing
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
