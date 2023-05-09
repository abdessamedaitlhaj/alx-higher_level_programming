#!/usr/bin/python3
def print_last_digit(number):
    num_copy = number;
    if number < 0:
        num_copy = -number
    last = num_copy % 10
    print(last, end = "")
    return last
