# -*- coding: utf-8 -*-
"""
Convert integer value of game difficulty into dictionary and vice versa.
"""
from il2ds_difficulty.constants import NUMBERS_MAPS, DEFAULT_GAME_VERSION


def decompose_difficulty(difficulty, game_version=DEFAULT_GAME_VERSION):
    """
    Retrieves difficulty settings from integer value.
    """
    if not isinstance(difficulty, int):
        raise TypeError("Difficulty is not integer")
    if difficulty < 0:
        raise ValueError("Difficulty must be a positive number")

    if not isinstance(game_version, basestring):
        raise TypeError("Game version must be a string")
    if not game_version in NUMBERS_MAPS:
        raise ValueError("Unknown game version")

    numbers_map = NUMBERS_MAPS[game_version]

    return {
        code_name: ((1 << number) & difficulty) > 0
        for code_name, number in numbers_map.iteritems()
    }
