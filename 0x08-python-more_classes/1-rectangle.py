#!/usr/bin/python3
""" Defines a class rectangle """


class Rectangle:
    """ Represents the rectangle """
    
    def __init__(self, width=0, height=0):
        """ initializes the rectangle
            args:
                width (int): smallest side of the rectangle
                height (int): longest side of the rectangle
            returns:
                nothing
                """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ getter for width
            returns:
                width of the rectangle
                """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter for width
            args:
                value (int): the value of width
            return:
                nothing
            """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif  value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ getter for height
            returns:
                height of the rectangle
                """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter for height
        args:
            value (int): value of the height
        returns:
            nothing
            """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

