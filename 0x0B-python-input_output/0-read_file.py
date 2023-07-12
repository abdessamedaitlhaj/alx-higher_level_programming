#!/usr/bin/python3
"""Module that reads a text file and prints it to stdout"""


def read_file(filename=""):
    """Open and print a file

        Args:
            filename(file): the file to be readed and printed
    """
    with open(filename, "r", encoding='utf-8') as f:
        c = f.reads()
        print(c)
