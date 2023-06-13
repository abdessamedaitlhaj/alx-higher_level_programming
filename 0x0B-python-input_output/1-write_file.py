#!/usr/bin/python3
"""Module that defines a write_file function"""


def write_file(filename="", text=""):
    """Write the given content to a given file

        Args:
            filename (file): the file name
            text (str): string to be written

        Return:
            number of character written
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
