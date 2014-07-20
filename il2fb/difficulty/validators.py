# -*- coding: utf-8 -*-
"""
Different validators.
"""
from il2fb.difficulty.constants import SETTINGS
from il2fb.difficulty.helpers import _


def validate_difficulty(value):
    if not isinstance(value, (int, long)):
        raise TypeError(_("Difficulty is not an integer"))
    if value < 0:
        raise ValueError(_("Difficulty must be a positive number"))


def validate_game_version(value):
    if not isinstance(value, basestring):
        raise TypeError(_("Game version is not a string"))
    if not value in SETTINGS:
        raise ValueError(_("Unknown game version"))
