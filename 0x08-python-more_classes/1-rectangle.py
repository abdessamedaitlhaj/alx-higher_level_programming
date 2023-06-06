#!/usr/bin/python3
""" Rectangle Module """


class Rectangle:
    """ class Rectangle with attributes width & height """

    def __init__(self, width=0, height=0):
        """ Instantiation with optional width and height
            Args:
                width(int): the width of the rectangle.
                height(int): the height of the rectangle.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ Property to retrieve width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Property to set width
            Args:
                value(int): width's value to set.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Property to retrieve height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Property to set height
            Args:
            value(int): height's vale to set.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if not value:
            raise ValueError("height must be >= 0")
        self.__height = value
