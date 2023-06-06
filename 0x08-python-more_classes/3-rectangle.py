#!/usr/bin/python3
class Rectangle:

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    def width(self):
        return self.__width

    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def height(self):
        return self.__height

    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if not value:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return (self.__width + self.__height) * 2

    def __str__(self):
        if not self.__width and not self.__height:
            return ("#" * self.__width + "\n" ) * (self.__height - 1) + \
                    "#" * self.__width
        else:
            return ""

    width = property(width, width)
    height = property(height, height)
