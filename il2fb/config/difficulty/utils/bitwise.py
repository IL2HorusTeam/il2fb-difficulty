# -*- coding: utf-8 -*-


def is_bit_set(vector, position):
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
    return ((1 << position) & vector) > 0


def toggle_bit(vector, position, value):
    """
    Set value of a bit in a proper position.

    >>> toggle_bit(0, 0, False)
    0
    >>> toggle_bit(0, 0, True)
    1
    >>> toggle_bit(1, 0, False)
    0
    >>> toggle_bit(1, 0, True)
    1
    >>> toggle_bit(5, 2, False)
    1
    """
    mask = 1 << position

    if value:
        vector |= mask
    else:
        vector &= ~mask

    return vector
