# -*- coding: utf-8 -*-

import unittest

from candv import ValueConstant
from il2fb.commons import GameVersions

from il2fb.difficulty.validators import (
    validate_difficulty, validate_settings, validate_game_version,
)


class ValidatorsTestCase(unittest.TestCase):

    def test_validate_difficulty(self):
        self.assertIsNone(validate_difficulty(123))
        self.assertRaises(TypeError, validate_difficulty, '123')
        self.assertRaises(ValueError, validate_difficulty, -123)

    def test_validate_settings(self):
        self.assertIsNone(validate_settings({}))
        self.assertRaises(TypeError, validate_settings, [])

    def test_validate_game_version(self):
        value = GameVersions.get_default()
        self.assertIsNone(validate_game_version(value))
        self.assertRaises(TypeError, validate_game_version, '123')

        value = ValueConstant(None)
        self.assertRaises(ValueError, validate_game_version, value)
