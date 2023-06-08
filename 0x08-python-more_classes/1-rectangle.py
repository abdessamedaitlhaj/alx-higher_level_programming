#!/usr/bin/python3
"""
Module that defines a rectangle
"""


class Rectangle:
    """
    a class Rectangle that defines a rectangle.
    """
    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle with specified width and height.
        """
        self.width = width
        self.height = height

    def width(self):
        """getter methode to retrieve the width"""
        return self.__width

    def width(self, value):
        """setter method to set the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def height(self):
        """getter method to retrieve the height."""
        return self.__height

    def height(self, value):
        """setter method to set the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    width = property(width, width)
    height = property(height, height)
