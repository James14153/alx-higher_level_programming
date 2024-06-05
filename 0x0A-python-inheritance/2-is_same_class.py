#!/usr/bin/python3

"""
    This function checks for the type of object abd class
"""

def is_same_class(obj, a_class):
    """ Returns True if obj is an instance of a_class
    """
    if type(obj) == type(a_class):
        return True
    return False
