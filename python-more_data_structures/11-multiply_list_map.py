#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    return [] if my_list is None else list(map(lambda x: x * number, my_list))
