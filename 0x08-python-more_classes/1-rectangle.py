#!/usr/bin/python3
"""Module that define a Rectangle class."""


class Rectangle:
    """Rectangle class with attributes width and height."""

    def __init__(self, width=0, height=0):
        """
        Constructor that initialize width and height
        of a rectangle.

        Parameters:
        width(int): width of the rectangle.
        height(int): height of the rectangle.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Property that retrieve width.

        Return:
        int: width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Property that set width.

        Parameters:
        value(int): width of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Property that retrieve height.

        Return:
        int: height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Property that set height.

        Parameters:
        value(int): height of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
