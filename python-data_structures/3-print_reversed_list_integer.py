#!/usr/bin/python3
def print_reversed_listinterger(my_list=[]):
    """Prints all the intergers of a list in reverse order"""
    if my_list:
        for i in reversed(my_list):
            print("{:d}".format(i))
