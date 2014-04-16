# -*- coding: utf-8 -*-
"""
Convert integer value of game difficulty into dictionary and vice versa.
"""
from il2_difficulty.constants import (DEFAULT_GAME_VERSION, SETTINGS,
    NUMBERS_MAPS, SETTINGS_NAMES_MAP, TABS_NAMES_MAP, )
from il2_difficulty.helpers import _, evaluate_string
from il2_difficulty.validators import (validate_difficulty,
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
    (
        {
            'code': 'tab1_code',
            'name': 'tab1_name',
            'settings': (
                {
                    'code': 'setting1_code',
                    'title': 'setting1_title',
                    'description': 'setting1_description',
                    'value': 'setting1_value',
                },
            ),
        },
    )
    """
    validate_difficulty(difficulty)
    validate_game_version(game_version)

    settings = SETTINGS[game_version]
    return tuple(
        {
            'code': tab_code,
            'title': evaluate_string(TABS_NAMES_MAP[tab_code]),
            'settings': tuple(
                {
                    'code': setting_code,
                    'title': evaluate_string(
                        SETTINGS_NAMES_MAP[setting_code]['title']),
                    'description': evaluate_string(
                        SETTINGS_NAMES_MAP[setting_code]['description']),
                    'value': get_setting_value(difficulty, setting_number),
                } for setting_code, setting_number in tab_settings.items()
            )
        } for tab_code, tab_settings in settings.items()
    )


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
