#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        a = a / b
    except Exception:
        pass
    finally:
        print("Inside result: {}".format(a))
        return a if b != 0 else None
