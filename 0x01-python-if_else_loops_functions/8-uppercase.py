#!/usr/bin/python3
STR = ""
def uppercase(str):
    for c in str:
        if ord(c) <= 122 and ord(c) >= 97:
            STR += chr(ord(c))
        else:
            STR += c
uppercase("gfgGhjV")
print(STR)
