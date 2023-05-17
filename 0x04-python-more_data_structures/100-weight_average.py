#!/usr/bin/python3
def weight_average(my_list=[]):
    dominator = 0
    denominator = 0
    for item in my_list:
        dominator += item[0] * item[1]
    for item in my_list:
        denominator += item[1]
    return dominator / denominator
