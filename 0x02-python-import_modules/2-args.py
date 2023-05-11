#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv
    if len(args) == 1:
        print("{} arguments.".format(0))
    elif len(args) == 2:
        print("{} argument:\n{}: {}".format(1, 1, args[1]))
    else:
        print("{} arguments:".format(len(args) - 1))
        i = 1
        for arg in args[1:]:
            print("{}: {}".format(i, arg))
            i = i + 1
