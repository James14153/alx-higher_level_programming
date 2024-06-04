#!/usr/bin/python3

"""
This is the " say_my_name" module 

This module supplies the function "say_my_name"
"""

def say_my_name(firstname, lastname=""):
    """
    This function prints first name and last name
    """
    if type(firstname) is not str:
        raise TypeError("first_name must be a string")
    if type(lastname) is not str:
        raise TypeError("last_name must be a string")
    print(f"My name is {firstname} {lastname}")
