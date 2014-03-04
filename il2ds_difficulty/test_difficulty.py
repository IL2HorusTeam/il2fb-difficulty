# -*- coding: utf-8 -*-
"""
 Testing the application il2ds_difficulty
"""
import unittest

from il2ds_difficulty.constants import DifficultyParams
from il2ds_difficulty.difficulty import get_difficulty_settings


class DifficultyTest(unittest.TestCase):

    def test_difficulty_code(self):
        code = 6704004351
        get_difficulty_settings(DifficultyParams, code)