#!/usr/bin/python3
"""Module that defines MyList class"""

class MyList(list):
    """MyList that defines method to sort a list"""

    def print_sorted(self):
        """Print a sorted list"""
        print (sorted(self))
