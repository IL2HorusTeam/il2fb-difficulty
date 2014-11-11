# -*- coding: utf-8 -*-
"""
Convert integer value of game difficulty into dictionary and vice versa.
"""

from collections import OrderedDict
from il2fb.commons import GameVersions

from .settings import SETTINGS, PRESETS
from .utils import flatten_dict
from .validators import (
    validate_difficulty, validate_settings, validate_game_version,
)


def decompose(difficulty, game_version=None):
    """
    Convert an integer value into dictionary of difficulty settings.
    """
    validate_difficulty(difficulty)
    settings = get_flat_settings(game_version)
    return {
        code_name: is_parameter_set(difficulty, number)
        for code_name, number in settings.items()
    }


def decompose_to_tabs(difficulty, game_version=None):
    """
    Convert an integer value into ordered groups of difficulty settings .
    """
    validate_difficulty(difficulty)
    settings = get_settings(game_version)
    return OrderedDict([
        (tab, OrderedDict([
            (parameter, is_parameter_set(difficulty, position))
            for parameter, position in parameters.items()
        ]))
        for tab, parameters in settings.items()
    ])


def is_parameter_set(difficulty, position):
    """
    Check if difficulty parameter is present in difficulty integer value.

    Difficulty value = 2^position, e.g. 1024 = 2^10.
    """
    return ((1 << position) & difficulty) > 0


def compose(settings, game_version=None):
    """
    Convert a dictionary of flat difficulty settings into an integer value.
    """
    validate_settings(settings)

    game_version = game_version or GameVersions.get_default()
    validate_game_version(game_version)

    return _compose(settings, game_version)


def compose_from_tabs(settings, game_version=None):
    """
    Convert a dictionary of difficulty settings groupped by tabs into an integer
    value.
    """
    validate_settings(settings)

    game_version = game_version or GameVersions.get_default()
    validate_game_version(game_version)

    return _compose(flatten_dict(settings), game_version)


def _compose(flat_settings, game_version):
    parameters = get_flat_settings(game_version)
    return sum([1 << parameters[k] for k, v in flat_settings.items() if v])


def get_settings(game_version=None):
    game_version = game_version or GameVersions.get_default()
    validate_game_version(game_version)
    return SETTINGS[game_version]


def get_flat_settings(game_version=None):
    return flatten_dict(get_settings(game_version))


def get_presets(game_version=None):
    game_version = game_version or GameVersions.get_default()
    validate_game_version(game_version)
    return PRESETS[game_version]
