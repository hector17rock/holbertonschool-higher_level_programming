#!/usr/bin/python3
def print_reversed_list_interger(my_list=[]):
    """Prints all intergers of a list in reverse order"""
    if my_list:
        for i in reversed(my_list):
            print("{:d}".format(i))
