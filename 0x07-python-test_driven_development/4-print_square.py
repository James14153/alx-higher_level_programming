#!/usr/bin/python3
"""
This is the print_square module
This module supplies the print_square function
"""
def print_square(size):
    """
    This function prints a square using #
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print('#' * size)
