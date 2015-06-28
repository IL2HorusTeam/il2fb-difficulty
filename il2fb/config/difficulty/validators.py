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
    """
    >>> from il2fb.commons import GameVersions
    >>> validate_game_version(GameVersions.v4_12)
    >>>
    >>> validate_game_version("4.12")
    Traceback (most recent call last):
        ...
    TypeError: <... 'str'> is invalid type of game version. Instance of <class 'candv.ValueConstant'> was expected.
    >>>
    >>> from candv import ValueConstant
    >>> version = ValueConstant('X.XX')
    >>> validate_game_version(version)
    Traceback (most recent call last):
        ...
    ValueError: Unknown game version 'X.XX'. Supported versions: '4.12...'.
    """
    if not isinstance(value, ValueConstant):
        raise TypeError(
            _("{actual} is invalid type of game version. Instance of "
              "{expected} was expected.")
            .format(actual=type(value), expected=ValueConstant))

    if value not in SETTINGS:
        supported_versions = ', '.join([
            "'{0}'".format(x.value) for x in SETTINGS.keys()
        ])
        raise ValueError(
            _("Unknown game version '{actual}'. Supported versions: "
              "{supported}.")
            .format(actual=value.value, supported=supported_versions))
