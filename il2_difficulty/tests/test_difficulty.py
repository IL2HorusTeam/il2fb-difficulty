# -*- coding: utf-8 -*-
"""
 Testing the application il2_difficulty
"""
import unittest

from il2_difficulty import decompose_difficulty, compose_difficulty
from il2_difficulty.constants import (NUMBERS_MAPS, DEFAULT_GAME_VERSION,
    FLUTTER_EFFECT, NO_SPEED_BAR, LIMITED_AMMO, TAKEOFF_LANDING, )


def get_all_settings(value):
    """
    Get all settings for default game version with specified value.
    """
    numbers_map = NUMBERS_MAPS[DEFAULT_GAME_VERSION]
    values = [value, ] * len(numbers_map)
    return dict(zip(numbers_map.keys(), values))


def get_all_enabled_settings():
    """
    Get all settings for default game version with `True` value.
    """
    return get_all_settings(True)


def get_all_disabled_settings():
    """
    Get all settings for default game version with `False` value.
    """
    return get_all_settings(False)


class DecomposeDifficultyTest(unittest.TestCase):

    def test_all_false(self):
        """
        Test decomposition of zero value.
        """
        difficulty = 0
        settings = decompose_difficulty(difficulty)
        self.assertFalse(any(settings.values()))


class ComposeDifficultyTest(unittest.TestCase):

    def test_all_false(self):
        """
        Test composition of zero value.
        """
        settings = get_all_disabled_settings()
        difficulty = compose_difficulty(settings)
        self.assertEqual(difficulty, 0)

    def test_some_true(self):
        """
        Test composition of difficulty when some settings are true.
        """
        settings = get_all_disabled_settings()
        settings[FLUTTER_EFFECT] = True
        settings[NO_SPEED_BAR] = True
        settings[LIMITED_AMMO] = True
        settings[TAKEOFF_LANDING] = True

        difficulty = compose_difficulty(settings)
        self.assertEqual(difficulty, 4202626)
