#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    element = 0
    try:
        for y in range(x):
            print("{:d}".format(my_list[y]), end="")
            element += 1
    except (ValueError, TypeError):
        pass
    finally:
        print()
    return element
