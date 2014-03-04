# -*- coding: utf-8 -*-
"""
 Testing the application il2ds_difficulty
"""
import unittest

from il2ds_difficulty import decompose_difficulty
from il2ds_difficulty.constants import DEFAULT_GAME_VERSION


class DecomposeDifficultyTest(unittest.TestCase):

    def test_all_false(self):
        difficulty = 0
        settings = decompose_difficulty(difficulty, DEFAULT_GAME_VERSION)
        self.assertFalse(any(settings.values()))
