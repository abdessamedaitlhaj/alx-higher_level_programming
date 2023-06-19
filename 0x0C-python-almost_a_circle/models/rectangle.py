#!/usr/bin/python3
"""Module that defines a Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class that inherits from Base class
    with private attributes width, height, x and y
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor method that set Rectangle attributes

            Args:
                width (int): the width
                height (int): the height
                x (int): position of the rectangle horizontally
                y (int): position of the rectangle vertically

            Raises:
                TypeError <name of the attribute> must be an integer
                ValueError <name of the attribute> must be >/>= 0
        """
        super().__init__(id)
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Getter method for the width

            Returns:
                the width of the rectangle
        """
        return self.__width

    @property
    def height(self):
        """Getter method for the width

            Returns:
                the height of the rectangle
        """
        return self.__height

    @property
    def x(self):
        """Getter method for x attribute

            Returns:
                position of the rectangle horizontally
        """
        return self.__x

    @property
    def y(self):
        """Getter method for x attribute

            Returns: position of the rectangle vertically
        """
        return self.__y

    @width.setter
    def width(self, value):
        """Setter method for the width

            Args:
                value (int): the width

            Raises:
                TypeError width must be an integer
                ValueError width must be > 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Setter method for the height

            Args:
                value (int): the height

            Raises:
                TypeError height must be an integer
                ValueError height must be > 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Setter method for the x attribute

            Args:
                value (int): horizontal position value

            Raises:
                TypeError x must be an integer
                ValueError x must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Setter method for the y attribute

            Args:
                value (int): vertical position value

            Raises:
                TypeError y must be an integer
                ValueError y must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the rectangle

            Returns:
                the rectangle area
        """
        return self.__width * self.__height

    def display(self):
        """Prints in stdout the Rectangle with #"""
        print("\n" * self.__y, end="")
        print(
                (" " * self.__x + ("#" * self.__width + "\n")) *
                (self.__height - 1),
                end=""
            )
        print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """Overiding the str method

            Returns:
                Costume output for Rectangle
        """
        return (
                f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - "
                f"{self.__width}/{self.__height}"
            )

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute

            Args:
                args (str): list of args
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >= 3:
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) >= 5:
                self.__y = args[4]
        if kwargs:
            if "id" in kwargs:
                self.id = kwargs['id']
            if "width" in kwargs:
                self.__width = kwargs['width']
            if "height" in kwargs:
                self.__height = kwargs['height']
            if "x" in kwargs:
                self.__x = kwargs['x']
            if "y" in kwargs:
                self.__y = kwargs['y']

    def to_dictionary(self):
        """Returns the dictionary representation

            Returns:
                dictionary representation of a rectangle
        """
        return {
                'id': self.id,
                'width': self.__width,
                'height': self.__height,
                'x': self.__x,
                'y': self.__y
            }
