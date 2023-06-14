#!/usr/bin/python3
"""Module that defines a Rectangle class"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class with attributes width and height"""
    def __init__(self, width, height):
        """Constructor for Rectangle class

            Args:
                width (int): the width
                height (int): the height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
