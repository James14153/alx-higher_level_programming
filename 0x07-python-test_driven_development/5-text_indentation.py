#!/usr/bin/python3
"""
This is the "text_identation module"

This module supplies the text_identation function
"""
def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The text to be formatted.

    Raises:
        TypeError: If the text is not a string.

    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    
    flag = 0

    for i in text:
        if flag == 0:
            if i == ' ':
                continue
            else:
                flag = 1
        if flag == 1:
            if i == '?' or i == '.' or i == ':':
                print(i)
                print()
                flag = 0
            else:
                print(i, end="")
