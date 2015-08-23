# -*- coding: utf-8 -*-

import mock
import six
import unittest

from collections import OrderedDict

from il2fb.config.difficulty import (
    get_preset_value, get_actual_rules, decompose, decompose_to_tabs, compose,
    compose_from_tabs,
)
from il2fb.config.difficulty.constants import PRESET_TYPES, PARAMETERS
from il2fb.config.difficulty.utils.transforms import flatten_dict


def __patch_dict__init__(self, in_dict, values=(), clear=False, **kwargs):
    """
    Patch 'mock.patch.dict' so it will not convert 'values' into plain dict,
    but will use passed values. This is important when working with
    OrderedDict.
    """
    if isinstance(in_dict, six.string_types):
        in_dict = mock.mock._importer(in_dict)

    self.in_dict = in_dict
    self.clear = clear
    self._original = None

    if not isinstance(values, dict):
        values = dict(values)

    self.values = values
    self.values.update(kwargs)

mock.patch.dict.__init__ = __patch_dict__init__


class BaseTestCase(unittest.TestCase):

    MOCK_SETTINGS = {}
    MOCK_RULES = {}
    MOCK_PRESETS = {}

    def setUp(self):

        def _patch(path, new_value):
            patcher = mock.patch.dict(path, new_value, clear=True)
            self.addCleanup(patcher.stop)
            patcher.start()

        _patch('il2fb.config.difficulty.constants.SETTINGS',
               self.MOCK_SETTINGS)
        _patch('il2fb.config.difficulty.constants.FLAT_SETTINGS',
               flatten_dict(self.MOCK_SETTINGS))
        _patch('il2fb.config.difficulty.constants.RULES', self.MOCK_RULES)
        _patch('il2fb.config.difficulty.constants.PRESETS', self.MOCK_PRESETS)


class GetPresetValueTestCase(BaseTestCase):

    MOCK_PRESETS = {
        PRESET_TYPES.EASY: 123,
    }

    def test_get_preset_value(self):
        self.assertEqual(get_preset_value(PRESET_TYPES.EASY), 123)

    def test_get_preset_value_for_unknown_preset_type(self):
        self.assertIsNone(get_preset_value(PRESET_TYPES.NORMAL))


class GetActualRulesTestCase(BaseTestCase):

    MOCK_SETTINGS = {
        'tab1': {
            PARAMETERS.NO_OUTSIDE_VIEWS: 0,
            PARAMETERS.NO_MAP_ICONS: 1,
        },
    }
    MOCK_RULES = {
        PARAMETERS.NO_OUTSIDE_VIEWS: {
            True: "rules which are applied when NO_OUTSIDE_VIEWS is on",
            False: "rules which are applied when NO_OUTSIDE_VIEWS is off",
        },
        PARAMETERS.NO_MAP_ICONS: {
            True: "rules which are applied when NO_MAP_ICONS is on",
            False: "rules which are applied when NO_MAP_ICONS is off",
        },
    }

    def test_get_actual_rules_all_off(self):
        rules = get_actual_rules(0)
        self.assertEqual(
            rules[PARAMETERS.NO_OUTSIDE_VIEWS],
            "rules which are applied when NO_OUTSIDE_VIEWS is off"
        )
        self.assertEqual(
            rules[PARAMETERS.NO_MAP_ICONS],
            "rules which are applied when NO_MAP_ICONS is off"
        )

    def test_get_actual_rules_all_on(self):
        rules = get_actual_rules((1 << 0) | (1 << 1))
        self.assertEqual(
            rules[PARAMETERS.NO_OUTSIDE_VIEWS],
            "rules which are applied when NO_OUTSIDE_VIEWS is on"
        )
        self.assertEqual(
            rules[PARAMETERS.NO_MAP_ICONS],
            "rules which are applied when NO_MAP_ICONS is on"
        )

    def test_get_actual_rules_mixed(self):
        rules = get_actual_rules(1 << 1)
        self.assertEqual(
            rules[PARAMETERS.NO_OUTSIDE_VIEWS],
            "rules which are applied when NO_OUTSIDE_VIEWS is off"
        )
        self.assertEqual(
            rules[PARAMETERS.NO_MAP_ICONS],
            "rules which are applied when NO_MAP_ICONS is on"
        )


class CompositionDecompositionTestCase(BaseTestCase):

    MOCK_SETTINGS = OrderedDict([
        ('tab1', OrderedDict([
            ('param1', 0),
            ('param2', 1),
        ])),
        ('tab2', OrderedDict([
            ('param3', 2),
            ('param4', 3),
        ])),
    ])

    def test_decompose(self):
        result = decompose(0)
        self.assertFalse(result['param1'])
        self.assertFalse(result['param2'])
        self.assertFalse(result['param3'])
        self.assertFalse(result['param4'])

        result = decompose(15)
        self.assertTrue(result['param1'])
        self.assertTrue(result['param2'])
        self.assertTrue(result['param3'])
        self.assertTrue(result['param4'])

    def test_decompose_to_tabs(self):
        result = decompose_to_tabs(0)

        self.assertEqual(
            list(result.keys()),
            ['tab1', 'tab2', ]
        )
        self.assertEqual(
            list(result['tab1'].keys()),
            ['param1', 'param2', ]
        )
        self.assertEqual(
            list(result['tab2'].keys()),
            ['param3', 'param4', ]
        )

        self.assertFalse(result['tab1']['param1'])
        self.assertFalse(result['tab1']['param2'])
        self.assertFalse(result['tab2']['param3'])
        self.assertFalse(result['tab2']['param4'])

        result = decompose_to_tabs(15)
        self.assertTrue(result['tab1']['param1'])
        self.assertTrue(result['tab1']['param2'])
        self.assertTrue(result['tab2']['param3'])
        self.assertTrue(result['tab2']['param4'])

    def test_compose(self):
        result = compose({
            'param1': False,
            'param2': False,
            'param3': False,
            'param4': False,
        })
        self.assertEqual(result, 0)

        result = compose({
            'param1': True,
            'param2': True,
            'param3': True,
            'param4': True,
        })
        self.assertEqual(result, 15)

    def test_compose_from_tabs(self):
        result = compose_from_tabs({
            'tab1': {
                'param1': False,
                'param2': False,
            },
            'tab2': {
                'param3': False,
                'param4': False,
            },
        })
        self.assertEqual(result, 0)

        result = compose_from_tabs({
            'tab1': {
                'param1': True,
                'param2': True,
            },
            'tab2': {
                'param3': True,
                'param4': True,
            },
        })
        self.assertEqual(result, 15)
