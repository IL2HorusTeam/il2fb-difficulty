# -*- coding: utf-8 -*-
"""
Convert integer value of game difficulty into dictionary and vice versa.
"""

from collections import OrderedDict

from .constants import SETTINGS, FLAT_SETTINGS, RULE_TYPES, RULES
from .exceptions import LockedParameterException
from .utils.bitwise import is_bit_set, toggle_bit
from .utils.transforms import flatten_dict
from .validators import validate_difficulty, validate_settings


def get_actual_rules(difficulty):
    """
    Return subset of rules which are active for a given difficulty value.
    """
    validate_difficulty(difficulty)
    result = {}

    for parameter, rules in RULES.items():
        value = is_parameter_set(difficulty, parameter)
        result[parameter] = rules[value]

    return result


def decompose(difficulty):
    """
    Convert an integer value into dictionary of difficulty settings.
    """
    validate_difficulty(difficulty)
    return {
        code_name: is_bit_set(difficulty, number)
        for code_name, number in FLAT_SETTINGS.items()
    }


def decompose_to_tabs(difficulty):
    """
    Convert an integer value into ordered groups of difficulty settings.
    """
    validate_difficulty(difficulty)
    return OrderedDict([
        (tab, OrderedDict([
            (parameter, is_bit_set(difficulty, position))
            for parameter, position in parameters.items()
        ]))
        for tab, parameters in SETTINGS.items()
    ])


def compose(settings):
    """
    Convert a dictionary of flat difficulty settings into an integer value.
    """
    validate_settings(settings)
    return _compose(settings)


def compose_from_tabs(settings):
    """
    Convert a dictionary of difficulty settings groupped by tabs into an
    integer value.
    """
    validate_settings(settings)
    return _compose(flatten_dict(settings))


def _compose(flat_settings):
    return sum(1 << FLAT_SETTINGS[k]
               for k, v in flat_settings.items()
               if v)


def autocorrect_difficulty(difficulty):
    validate_difficulty(difficulty)

    affected_parameters = {}
    actual_rules = get_actual_rules(difficulty)

    def _autocorrect_rules(difficulty, master, rule_type, expected_value):
        if rule_type in rules:
            for slave in rules[rule_type]:
                value = is_parameter_set(difficulty, slave)
                if value != expected_value:
                    difficulty = toggle_parameter_raw(
                        difficulty, slave, expected_value)
                    affected_parameters[slave] = master

        return difficulty

    for master, rules in actual_rules.items():
        difficulty = _autocorrect_rules(
            difficulty, master, RULE_TYPES.TURNS_ON, True)
        difficulty = _autocorrect_rules(
            difficulty, master, RULE_TYPES.TURNS_OFF, False)

    return difficulty, affected_parameters


def is_parameter_set(difficulty, parameter):
    position = FLAT_SETTINGS[parameter]
    return is_bit_set(difficulty, position)


def get_parameter_lockers(difficulty, parameter):
    actual_rules = get_actual_rules(difficulty)
    return [
        locker
        for locker, rules in actual_rules.items()
        if RULE_TYPES.LOCKS in rules and parameter in rules[RULE_TYPES.LOCKS]
    ]


def toggle_parameter_raw(difficulty, parameter, value):
    position = FLAT_SETTINGS[parameter]
    return toggle_bit(difficulty, position, value)


class ParameterToggler(object):

    __name__ = 'toggle_parameter'

    def __call__(self, difficulty, parameter, value):
        validate_difficulty(difficulty)
        self._check_can_be_toggled(difficulty, parameter)

        difficulty = toggle_parameter_raw(difficulty, parameter, value)
        side_effects = self._get_side_effects(parameter, value)
        difficulty = self._process_side_effects(difficulty, side_effects)

        return difficulty, side_effects

    def _check_can_be_toggled(self, difficulty, parameter):
        lockers = get_parameter_lockers(difficulty, parameter)
        if lockers:
            raise LockedParameterException(parameter, lockers)

    def _get_side_effects(self, parameter, value):
        return RULES[parameter][value] if parameter in RULES else {}

    def _process_side_effects(self, difficulty, side_effects):
        if RULE_TYPES.TURNS_ON in side_effects:
            for parameter in side_effects[RULE_TYPES.TURNS_ON]:
                difficulty = toggle_parameter_raw(difficulty, parameter, True)

        if RULE_TYPES.TURNS_OFF in side_effects:
            for parameter in side_effects[RULE_TYPES.TURNS_OFF]:
                difficulty = toggle_parameter_raw(difficulty, parameter, False)

        return difficulty


toggle_parameter = ParameterToggler()
