#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """represents the square
        Attributes:
            __size(int): size of a side of the square
        """
    def __init__(self, size=0):
        """initializes the square
        Args:
            size(int): size of a side of square
        Returns:
            None
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
