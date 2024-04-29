#!/usr/bin/python3
""" Defines a class rectangle """


class Rectangle:
    """ Represents the rectangle """

    number_of_instances = 0

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
        Rectangle.number_of_instances += 1

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
        elif value < 0:
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

    def area(self):
        """ calculates the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """ calculates the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width + self.__height) * 2)

    def __str__(self):
        """ prints the rectangle using the # character"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = ""
        for i in range(self.__height):
            rect += "#" * self.__width + "\n"
        return rect.rstrip()

    def __repr__(self):
        """ returns astring representation of the rectangle for reproduction"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """ prints a message when an instance is deleted """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
