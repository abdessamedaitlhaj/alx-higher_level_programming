#!/usr/bin/python3
"""
Module that writes a string to a text file (UTF8) and
returns the number of characters written
"""


def write_file(filename="", text=""):
    """Write a text to a file and return number
    of char written

        Args:
            filename(file): the file to write in
            text(str): the content to write

        Return:
            the number of char written
    """
    with open(filename, "w+", encoding='utf-8') as f:
        f.write(text)
    return len(text)
