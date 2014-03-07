# -*- coding: utf-8 -*-
"""
Convert integer value of game difficulty into dictionary and vice versa.
"""
from collections import OrderedDict

from il2ds_difficulty.constants import (DEFAULT_GAME_VERSION, SETTINGS,
    NUMBERS_MAPS, SETTINGS_NAMES_MAP, TABS_NAMES_MAP, )
from il2ds_difficulty.helpers import _
from il2ds_difficulty.validators import (validate_difficulty,
    validate_game_version, )


def get_setting_value(difficulty, setting_number):
    """
    Check if difficulty setting is present in difficulty integer value.
    """
    return ((1 << setting_number) & difficulty) > 0


def decompose_difficulty(difficulty, game_version=DEFAULT_GAME_VERSION):
    """
    Convert an integer value into difficulty settings dictionary.
    """
    validate_difficulty(difficulty)
    validate_game_version(game_version)

    numbers_map = NUMBERS_MAPS[game_version]
    return {
        code_name: get_setting_value(difficulty, number)
        for code_name, number in numbers_map.iteritems()
    }


def decompose_difficulty_to_tabs(difficulty,
                                 game_version=DEFAULT_GAME_VERSION):
    """
    Convert an integer value into ordered difficulty settings groups.

    Output example:
    {
        'tab1_code': {
            'name': 'tab1_name',
            'settings': {
                'setting1': {
                    'title': 'setting1_title',
                    'description': 'setting1_description',
                    'value': 'setting1_value',
                },
            },
        },
    }
    """
    validate_difficulty(difficulty)
    validate_game_version(game_version)

    settings = SETTINGS[game_version]
    return OrderedDict(tuple(
        (tab_code, {
            'name': TABS_NAMES_MAP[tab_code],
            'settings': OrderedDict(tuple(
                (setting_code, dict(
                    SETTINGS_NAMES_MAP[setting_code], **{
                    'value': get_setting_value(difficulty, setting_number),
                 })) for setting_code, setting_number in tab_settings.items()
            ))
        }) for tab_code, tab_settings in settings.items()
    ))


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
