#!/usr/bin/python3
"""
Module that defines a BaseGeometry class
"""


class BaseGeometry():
    """return an erreor if in case of calling area ft
    bcz is not implemented yet
    """
    def area(self):
        raise Exception("area() is not implemented")
