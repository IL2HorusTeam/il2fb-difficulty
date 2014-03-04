# -*- coding: utf-8 -*-
"""
Convert integer value of game difficulty into dictionary and vice versa.
"""
from il2ds_difficulty.constants import DIFFICULTY_MAP


def has_setting(difficulty, setting_number):
    """
    Return the parameter value (True or False)
    """
    return ((1 << setting_number) & difficulty) > 0


def decompose_difficulty(difficulty, settings_map=DIFFICULTY_MAP):
    """
    Retrieves parameters of the digital code.
    """
    return {
        code: has_setting(difficulty, number)
        for number, code in settings_map.iteritems()
    }
