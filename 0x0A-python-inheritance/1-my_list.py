#!/usr/bin/python3
"""
Module that defines a class that inherits form list
"""


class MyList(list):
    """print a list in a ascending order"""
    def print_sorted(self):
        print(sorted(self))
