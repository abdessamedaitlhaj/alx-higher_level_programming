#!/usr/bin/python3
"""Function that finds a peak in unsorted list of integers"""

def find_peak(list_of_integers):
    """Return the peak"""
    for i in enumerate(list_of_integers):
        curr = list_of_integers[i[0]]
        nex = list_of_integers[i[0] + 1]
        bef = list_of_integers[i[0] - 1]
        if i[0] == 0 and curr >= nex:
            return curr;
        elif curr >= bef and curr >= nex:
            return curr
