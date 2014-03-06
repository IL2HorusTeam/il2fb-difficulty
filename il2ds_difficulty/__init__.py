# -*- coding: utf-8 -*-
"""
Convert integer value of game difficulty into dictionary and vice versa.
"""
from il2ds_difficulty.constants import NUMBERS_MAPS, DEFAULT_GAME_VERSION
from il2ds_difficulty.helpers import _
from il2ds_difficulty.validators import validate_game_version


def decompose_difficulty(difficulty, game_version=DEFAULT_GAME_VERSION):
    """
    Convert an integer value into difficulty settings dictionary.
    """
    if not isinstance(difficulty, int):
        raise TypeError(_("Difficulty is not an integer"))
    if difficulty < 0:
        raise ValueError(_("Difficulty must be a positive number"))
    validate_game_version(game_version)

    numbers_map = NUMBERS_MAPS[game_version]

    return {
        code_name: ((1 << number) & difficulty) > 0
        for code_name, number in numbers_map.iteritems()
    }


def compose_difficulty(settings, game_version=DEFAULT_GAME_VERSION):
    """
    Convert a difficulty settings dictionary into integer.
    """
    if not isinstance(settings, dict):
        raise TypeError(_("Settings is not a dictionary"))
    validate_game_version(game_version)

    numbers_map = NUMBERS_MAPS[game_version]
    difficulty = 0

    for setting_code, setting_value in settings.iteritems():
        if setting_value:
            setting_integer = (1 << numbers_map[setting_code])
            difficulty += setting_integer

    return difficulty
