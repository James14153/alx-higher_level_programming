#!/usr/bin/python3
"""creates a square class"""

class Square:
    """class representing a square

    private attribute:
    __size(int): takes the size of side of square
    """
    def __init__(self, size):
        """initializes a square

        args:
            size(int): size of a side of the square
        Returns: None
        """
        self.__size = size
