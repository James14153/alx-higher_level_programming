#/usr/bin/python3

class Square:
    def __init__(self, size=0):
        self.__size = size
        try:
            size.is integer = True
        except TypeError
            print("size must be an integer")
        if size < 0:
            

