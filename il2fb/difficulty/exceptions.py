# -*- coding: utf-8 -*-


class LockedParameterException(Exception):
    """
    Raise this exception when someone wants to toggle some parameter while it's
    locked by some another parameter accordingly to the rules.
    """
