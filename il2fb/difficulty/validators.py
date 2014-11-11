# -*- coding: utf-8 -*-

from candv import ValueConstant
from six import integer_types

from .settings import SETTINGS
from .utils import translations


_ = translations.ugettext


def validate_difficulty(value):
    if not isinstance(value, integer_types):
        raise TypeError(_("Difficulty is not an integer"))
    if value < 0:
        raise ValueError(_("Difficulty must be a positive integer"))


def validate_settings(value):
    if not isinstance(value, dict):
        raise TypeError(_("Settings must be a dictionary"))


def validate_game_version(value):
    if not isinstance(value, ValueConstant):
        raise TypeError(
            _('Type "{:}" is invalid for game version. "{:}" was expected.')
            .format(type(value), ValueConstant))

    if value not in SETTINGS:
        supported_versions = ', '.join([str(x.value) for x in SETTINGS.keys()])
        raise ValueError(
            _('Unknown game version "{:}". Supported versions: {:}.')
            .format(value, supported_versions))
