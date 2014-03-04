# -*- coding: utf-8 -*-
"""
 Testing the application il2ds_difficulty
"""
import unittest

from il2ds_difficulty import decompose_difficulty
from il2ds_difficulty.constants import DIFFICULTY_MAP


class DecomposeDifficultyTest(unittest.TestCase):

    def test_all_false(self):
        difficulty = 0
        settings = decompose_difficulty(difficulty, DIFFICULTY_MAP)
        self.assertFalse(any(settings.values()))
