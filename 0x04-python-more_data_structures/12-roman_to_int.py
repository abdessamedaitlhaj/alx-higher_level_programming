#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return None
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_sub = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
    sum = 0
    for c in roman_sub:
        if c in roman_string:
            sum += roman_sub[c]
            roman_string = roman_string.replace(c, "")

    for c in roman_string:
        sum += roman[c]
    return sum
