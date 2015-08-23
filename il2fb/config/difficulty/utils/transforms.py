# -*- coding: utf-8 -*-


def flip_dict(source):
    """
    Swap keys and values in a dict.

    >>> flip_dict({})
    {}
    >>> flip_dict({'one': 1, 'two': 2, })
    {1: 'one', 2: 'two'}
    """
    return {v: k for k, v in source.items()}


def flatten_dict(settings):
    """
    Combine all subdictionaries into a single one.

    >>> settings = {
    ...     'tab1': {
    ...         'one': 1,
    ...         'two': 2,
    ...     },
    ...     'tab2': {
    ...         'three': 3,
    ...     },
    ...     'tab3': {
    ...         'four': 4,
    ...     },
    ... }
    >>> flatten = flatten_dict(settings)
    >>> flatten == {'one': 1, 'two': 2, 'three': 3, 'four': 4}
    True
    """
    return {k: v for i in settings.values() for k, v in i.items()}
