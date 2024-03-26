#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = ()
    add_1 = tuple_a + (0, 0)
    add_2 = tuple_b + (0, 0)
    new_tuple = add_1[0] + add_2[0], add_1[1] + add_2[1]
    return new_tuple
