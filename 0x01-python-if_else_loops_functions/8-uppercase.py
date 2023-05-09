#!/usr/bin/python3
def uppercase(str):
    for c in str:
        check = ord(c) <= 122 and ord(c) >= 97
        char = char(ord(c) - 32)
        print("{}".format(char) if check else "{}".format(c), end="")
    print()
