# -*- coding: utf-8 -*-


def inverse_dict(source):
    """
    >>> inverse_dict({})
    {}
    >>> inverse_dict({'one': 1, 'two': 2, })
    {1: 'one', 2: 'two'}
    """
    return {v: k for k, v in source.items()}


def flatten_settings(settings):
    return {k: v for i in settings.values() for k, v in i.items()}
