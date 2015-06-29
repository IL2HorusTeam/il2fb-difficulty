# -*- coding: utf-8 -*-


def is_bit_set(value, position):
    """
    Check if bit parameter is present in integer value.

    >>> is_bit_set(0, 0)
    False
    >>> is_bit_set(1, 0)
    True
    >>>
    >>> is_bit_set(5, 0)
    True
    >>> is_bit_set(5, 1)
    False
    >>> is_bit_set(5, 2)
    True
    """
    return ((1 << position) & value) > 0
