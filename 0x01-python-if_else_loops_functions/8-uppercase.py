#!/usr/bin/python3
STR = ""
def uppercase(str):
    for c in str:
        check = ord(c) <= 122 and ord(c) >= 97
        print("{}".format(chr(ord(c) - 32)) if check else "{}".format(c), end="")
    print()
