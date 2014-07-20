# -*- coding: utf-8 -*-
import unittest

from il2fb.difficulty.utils import inverse_dict, flatten_settings


class UtilsTestCase(unittest.TestCase):

    def test_inverse_dict(self):
        self.assertEqual(inverse_dict({'one': 1, 'two': 2, }),
                         {1: 'one', 2: 'two', })

    def test_flatten_settings(self):
        settings = {
            'tab1': {
                'one': 1,
                'two': 2,
            },
            'tab2': {
                'three': 3,
            },
            'tab3': {
                'four': 4,
            },
        }

        self.assertEqual(flatten_settings(settings), {
            'one': 1,
            'two': 2,
            'three': 3,
            'four': 4,
        })
