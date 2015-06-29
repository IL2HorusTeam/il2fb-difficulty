# -*- coding: utf-8 -*-

import mock
import unittest

from collections import OrderedDict

from il2fb.commons import GameVersions

from .. import (
    get_settings, get_flat_settings, get_presets, get_preset_value, get_rules,
    get_actual_rules,
)
from ..constants import PRESET_TYPES, PARAMETERS


class BaseTestCase(unittest.TestCase):

    MOCK_SETTINGS = {}
    MOCK_RULES = {}
    MOCK_PRESETS = {}

    def setUp(self):

        def _patch(path, new_value):
            patcher = mock.patch.dict(path, new_value)
            self.addCleanup(patcher.stop)
            patcher.start()

        _patch('il2fb.config.difficulty.settings.SETTINGS', self.MOCK_SETTINGS)
        _patch('il2fb.config.difficulty.settings.RULES', self.MOCK_RULES)
        _patch('il2fb.config.difficulty.settings.PRESETS', self.MOCK_PRESETS)


class GetSettingsTestCase(BaseTestCase):

    MOCK_SETTINGS = {
        GameVersions.get_default(): "settings for default game version",
        GameVersions.v4_12: "settings for v4.12",
    }

    def test_get_settings_for_default_version(self):
        settings = get_settings()
        self.assertEqual(settings, "settings for default game version")

    def test_get_settings_for_specific_version(self):
        settings = get_settings(GameVersions.v4_12)
        self.assertEqual(settings, "settings for v4.12")


class GetFlatSettingsTestCase(BaseTestCase):

    MOCK_SETTINGS = OrderedDict([
        (GameVersions.get_default(), OrderedDict([
            ('tab1', OrderedDict([
                ('param1', 1),
                ('param2', 2),
            ])),
            ('tab2', OrderedDict([
                ('param3', 3),
                ('param4', 4),
            ])),
        ])),
    ])

    def test_get_flat_settings(self):
        settings = get_flat_settings()
        self.assertEqual(settings, OrderedDict([
            ('param1', 1),
            ('param2', 2),
            ('param3', 3),
            ('param4', 4),
        ]))


class GetPresetsTestCase(BaseTestCase):

    MOCK_PRESETS = {
        GameVersions.get_default(): "presets for default game version",
        GameVersions.v4_12: "presets for v4.12",
    }

    def test_get_presets_for_default_version(self):
        rules = get_presets()
        self.assertEqual(rules, "presets for default game version")

    def test_get_presets_for_specific_version(self):
        rules = get_presets(GameVersions.v4_12)
        self.assertEqual(rules, "presets for v4.12")


class GetPresetValueTestCase(BaseTestCase):

    MOCK_PRESETS = {
        GameVersions.get_default(): {
            PRESET_TYPES.EASY: 123,
        },
    }

    def test_get_preset_value(self):
        self.assertEqual(get_preset_value(PRESET_TYPES.EASY), 123)

    def test_get_preset_value_for_unknown_preset_type(self):
        self.assertIsNone(get_preset_value(PRESET_TYPES.NORMAL))


class GetRulesTestCase(BaseTestCase):

    MOCK_RULES = {
        GameVersions.get_default(): "rules for default game version",
        GameVersions.v4_12: "rules for v4.12",
    }

    def test_get_rules_for_default_version(self):
        rules = get_rules()
        self.assertEqual(rules, "rules for default game version")

    def test_get_rules_for_specific_version(self):
        rules = get_rules(GameVersions.v4_12)
        self.assertEqual(rules, "rules for v4.12")


class GetActualRulesTestCase(BaseTestCase):

    MOCK_SETTINGS = {
        GameVersions.get_default(): {
            'tab1': {
                PARAMETERS.NO_OUTSIDE_VIEWS: 0,
                PARAMETERS.NO_MAP_ICONS: 1,
            },
        },
    }
    MOCK_RULES = {
        GameVersions.get_default(): {
            PARAMETERS.NO_OUTSIDE_VIEWS: {
                True: "rules which are applied when NO_OUTSIDE_VIEWS is on",
                False: "rules which are applied when NO_OUTSIDE_VIEWS is off",
            },
            PARAMETERS.NO_MAP_ICONS: {
                True: "rules which are applied when NO_MAP_ICONS is on",
                False: "rules which are applied when NO_MAP_ICONS is off",
            },
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
