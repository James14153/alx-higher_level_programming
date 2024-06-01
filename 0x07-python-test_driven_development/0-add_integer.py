#!/usr/bin/python3
"""
This is the "0-add_integer" module

This module supplies one function add_integer(a, b)
"""

def add_integer(a, b=98):
    """
    This function takes two arguments
    Returns the addition of two numbers
    """
    if type(a) is not int or float:
            raise TypeError("a must be an integer")
    
    if type (b) is not int or float:
            raise TypeError("b must be an integer")
    
    a = int(a)
    b = int(b)

    return a + b
