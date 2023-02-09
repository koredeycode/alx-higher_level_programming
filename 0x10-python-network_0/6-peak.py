#!usr/bin/python3
"""This module contain a funtion that find a peak in a list"""


def find_peak(lint):
    """find a peak in a list"""

    n = len(lint)
    if n < 3:
        return None
    mid = n // 2
    if n == 1:
        return lint[0]
    if n == 2:
        return max(lint)
    if lint[mid] > lint[mid - 1] and lint[mid] > lint[mid + 1]:
        return lint[mid]
    if lint[mid] < lint[mid + 1]:
        return find_peak(lint[mid:])
    if lint[mid] < lint[mid - 1]:
        return find_peak(lint[:mid])
