#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        print("Inside result: ".format(a / b))
    except:
        pass
    finally:
        return a / b if b != 0 else None
