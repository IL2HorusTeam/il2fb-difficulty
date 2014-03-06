# -*- coding: utf-8 -*-
"""
Different validators.
"""
from il2ds_difficulty.constants import NUMBERS_MAPS


def validate_game_version(value):
    if not isinstance(value, basestring):
        raise TypeError(_("Game version is not a string"))
    if not value in NUMBERS_MAPS:
        raise ValueError(_("Unknown game version"))
