# -*- coding: utf-8 -*-
import unittest

from il2fb.difficulty.validators import validate_difficulty, validate_settings


class ValidatorsTestCase(unittest.TestCase):

    def test_validate_difficulty(self):
        self.assertIsNone(validate_difficulty(123))
        self.assertRaises(TypeError, validate_difficulty, '123')
        self.assertRaises(ValueError, validate_difficulty, -123)

    def test_validate_settings(self):
        self.assertIsNone(validate_settings({}))
        self.assertRaises(TypeError, validate_settings, [])
