#!/usr/bin/python3
"""Module that defines read_file function"""


def read_file(filename=""):
    """Print the content of a file to stdout

        Args:
        filename (file): the file name
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read())
