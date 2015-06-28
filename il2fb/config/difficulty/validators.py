# -*- coding: utf-8 -*-

import six

from candv import ValueConstant

from .settings import SETTINGS
from .utils import translations


_ = translations.ugettext


def validate_difficulty(value):
    """
    Check if difficulty value taken from config is valid.

    >>> validate_difficulty(0)
    >>> validate_difficulty(123)
    >>> validate_difficulty(0.0)
    Traceback (most recent call last):
        ...
    TypeError: Difficulty value must be an integer.
    >>> validate_difficulty("0")
    Traceback (most recent call last):
        ...
    TypeError: Difficulty value must be an integer.
    >>> validate_difficulty(-1)
    Traceback (most recent call last):
        ...
    ValueError: Difficulty value must be >= 0.
    """
    if not isinstance(value, six.integer_types):
        raise TypeError(_("Difficulty value must be an integer."))

    if value < 0:
        raise ValueError(_("Difficulty value must be >= 0."))


def validate_settings(value):
    """
    >>> validate_settings({})
    >>> validate_settings([])
    Traceback (most recent call last):
        ...
    TypeError: Settings must be an instance of 'dict' or its subclass.
    """
    if not isinstance(value, dict):
        raise TypeError(
            _("Settings must be an instance of '{expected}' or its subclass.")
            .format(expected=dict.__name__))


def validate_game_version(value):
    if not isinstance(value, ValueConstant):
        raise TypeError(
            _("Type '{actual}' is invalid for game version. '{expected}' was "
              "expected.")
            .format(actual=type(value), expected=ValueConstant))

    if value not in SETTINGS:
        supported_versions = ', '.join([
            "'{0}'".format(x) for x in SETTINGS.keys()
        ])
        raise ValueError(
            _("Unknown game version '{actual}'. Supported versions: "
              "{supported}.")
            .format(actual=value, supported=supported_versions))
