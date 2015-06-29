# -*- coding: utf-8 -*-
"""
Convert integer value of game difficulty into dictionary and vice versa.
"""

from collections import OrderedDict
from il2fb.commons import GameVersions

from .constants import RULE_TYPES
from .exceptions import LockedParameterException
from .settings import SETTINGS, RULES, PRESETS
from .utils.bitwise import is_bit_set, toggle_bit
from .utils.transforms import flatten_dict
from .validators import (
    validate_difficulty, validate_settings, validate_game_version,
)


def get_settings(game_version=None):
    """
    Get all settings for game version groupped by tabs.
    """
    if not game_version:
        game_version = GameVersions.get_default()

    validate_game_version(game_version)
    return SETTINGS[game_version]


def get_flat_settings(game_version=None):
    """
    Get all settings for game version without groupping.
    """
    return flatten_dict(get_settings(game_version))


def get_presets(game_version=None):
    """
    Get all presets for game version.
    """
    if not game_version:
        game_version = GameVersions.get_default()

    validate_game_version(game_version)
    return PRESETS[game_version]


def get_preset_value(preset_type, game_version=None):
    """
    Get preset value for particular game version.
    """
    return get_presets(game_version).get(preset_type)


def get_rules(game_version=None):
    """
    Get all rules for game version.
    """
    if not game_version:
        game_version = GameVersions.get_default()

    validate_game_version(game_version)
    return RULES[game_version]


def get_actual_rules(difficulty, game_version=None):
    """
    Return subset of rules which are active for a given difficulty value.
    """
    validate_difficulty(difficulty)
    all_rules = get_rules(game_version)
    result = {}

    for parameter, rules in all_rules.items():
        value = is_parameter_set(difficulty, parameter)
        result[parameter] = rules[value]

    return result


def decompose(difficulty, game_version=None):
    """
    Convert an integer value into dictionary of difficulty settings.
    """
    validate_difficulty(difficulty)
    settings = get_flat_settings(game_version)
    return {
        code_name: is_bit_set(difficulty, number)
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
            (parameter, is_bit_set(difficulty, position))
            for parameter, position in parameters.items()
        ]))
        for tab, parameters in settings.items()
    ])


def compose(settings, game_version=None):
    """
    Convert a dictionary of flat difficulty settings into an integer value.
    """
    if not game_version:
        game_version = GameVersions.get_default()

    validate_settings(settings)
    validate_game_version(game_version)

    return _compose(settings, game_version)


def compose_from_tabs(settings, game_version=None):
    """
    Convert a dictionary of difficulty settings groupped by tabs into an
    integer value.
    """
    if not game_version:
        game_version = GameVersions.get_default()

    validate_settings(settings)
    validate_game_version(game_version)

    return _compose(flatten_dict(settings), game_version)


def _compose(flat_settings, game_version):
    parameters = get_flat_settings(game_version)
    return sum(1 << parameters[k] for k, v in flat_settings.items() if v)


def autocorrect_difficulty(difficulty, game_version=None):
    if not game_version:
        game_version = GameVersions.get_default()

    validate_difficulty(difficulty)
    validate_game_version(game_version)

    affected_parameters = {}

    actual_rules = get_actual_rules(difficulty, game_version)
    settings = get_flat_settings(game_version)

    def _autocorrect_rules(difficulty, master, rule_type, expected_value):
        if rule_type in rules:
            for slave in rules[rule_type]:
                value = is_parameter_set(difficulty, slave, game_version)
                if value != expected_value:
                    difficulty = toggle_parameter_raw(
                        difficulty, slave, expected_value, settings,
                    )
                    affected_parameters[slave] = master

        return difficulty

    for master, rules in actual_rules.items():
        difficulty = _autocorrect_rules(
            difficulty, master, RULE_TYPES.TURNS_ON, True,
        )
        difficulty = _autocorrect_rules(
            difficulty, master, RULE_TYPES.TURNS_OFF, False,
        )

    return difficulty, affected_parameters


def is_parameter_set(difficulty, parameter, game_version=None):
    position = get_parameter_position(parameter, game_version)
    return is_bit_set(difficulty, position)


def get_parameter_position(parameter, game_version=None):
    return get_flat_settings(game_version)[parameter]


def get_parameter_lockers(difficulty, parameter, game_version=None):
    actual_rules = get_actual_rules(difficulty, game_version)

    return [
        locker
        for locker, rules in actual_rules.items()
        if RULE_TYPES.LOCKS in rules and parameter in rules[RULE_TYPES.LOCKS]
    ]


def toggle_parameter_raw(difficulty, parameter, value, flat_settings):
    position = flat_settings[parameter]
    return toggle_bit(difficulty, position, value)


class ParameterToggler(object):

    __name__ = 'toggle_parameter'

    def __call__(self, difficulty, parameter, value, game_version=None):
        if not game_version:
            game_version = GameVersions.get_default()

        validate_difficulty(difficulty)
        validate_game_version(game_version)

        self._check_can_be_toggled(difficulty, parameter)
        self.settings = get_flat_settings(self.game_version)

        difficulty = toggle_parameter_raw(
            difficulty, parameter, value, self.settings
        )
        side_effects = self._get_side_effects(parameter, value)
        difficulty = self._process_side_effects(difficulty, side_effects)

        return difficulty, side_effects

    def _check_can_be_toggled(self, difficulty, parameter):
        lockers = get_parameter_lockers(
            difficulty, parameter, self.game_version
        )
        if lockers:
            raise LockedParameterException(
                parameter, lockers, self.game_version
            )

    def _get_side_effects(self, parameter, value):
        rules = get_rules(self.game_version)
        return rules[parameter][value] if parameter in rules else {}

    def _process_side_effects(self, difficulty, side_effects):
        if RULE_TYPES.TURNS_ON in side_effects:
            for parameter in side_effects[RULE_TYPES.TURNS_ON]:
                difficulty = toggle_parameter_raw(
                    difficulty, parameter, True, self.settings,
                )

        if RULE_TYPES.TURNS_OFF in side_effects:
            for parameter in side_effects[RULE_TYPES.TURNS_OFF]:
                difficulty = toggle_parameter_raw(
                    difficulty, parameter, False, self.settings,
                )

        return difficulty


toggle_parameter = ParameterToggler()
