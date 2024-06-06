#!/usr/bin/python3
"""
This module supplies the class mylist
"""


class MyList(list):
    """ a subclass of list"""
    def __init__(self):
        """ Initializes the object """
        super().__init__()

    def print_sorted(self):
        """ prints the sorted list """
        print(sorted(self))
