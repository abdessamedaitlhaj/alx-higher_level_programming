#!/usr/bin/python3
"""Module that defines a rectangle"""


class Rectangle:
    """Rectangle class that defines a rectangle."""
    def __init__(self, width=0, height=0):
        """
        Initialisation of Rectangle class with width and height.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """getter method to get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter method to set width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter method to get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter method to set height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
