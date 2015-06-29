# -*- coding: utf-8 -*-

import six
import unittest

from il2fb.commons import GameVersions

from ..constants import PARAMETERS, TABS, RULE_TYPES, PRESET_TYPES
from ..settings import SETTINGS, RULES, PRESETS


class StructuresTestCase(unittest.TestCase):
    """
    This test ensures all settings have a proper data structure which
    is retained across game versions.
    """

    @classmethod
    def setUpClass(cls):
        cls.available_versions = set(GameVersions.constants())

    def test_settings_structure(self):
        available_tabs = set(TABS.constants())
        available_paramaters = set(PARAMETERS.constants())

        for version, settings in SETTINGS.items():
            self.assertIn(version, self.available_versions)
            self.assertIsInstance(settings, dict)

            for tab, paramaters in settings.items():
                self.assertIn(tab, available_tabs)
                self.assertIsInstance(paramaters, dict)

                for paramater, position in paramaters.items():
                    self.assertIn(paramater, available_paramaters)
                    self.assertIsInstance(position, six.integer_types)

    def test_rules_structure(self):
        available_paramaters = set(PARAMETERS.constants())
        available_rule_types = set(RULE_TYPES.constants())

        for version, rules in RULES.items():
            self.assertIn(version, self.available_versions)
            self.assertIsInstance(rules, dict)

            for master, states in rules.items():
                self.assertIn(master, available_paramaters)
                self.assertIsInstance(states, dict)

                for state, rules in states.items():
                    self.assertIsInstance(state, bool)
                    self.assertIsInstance(rules, dict)

                    for rule_type, slaves in rules.items():
                        self.assertIn(rule_type, available_rule_types)
                        self.assertIsInstance(slaves, list)

                        for slave in slaves:
                            self.assertIn(slave, available_paramaters)

    def test_presets_structure(self):
        available_preset_types = set(PRESET_TYPES.constants())

        for version, presets in PRESETS.items():
            self.assertIn(version, self.available_versions)
            self.assertIsInstance(presets, dict)

            for preset_type, value in presets.items():
                self.assertIn(preset_type, available_preset_types)
                self.assertIsInstance(value, six.integer_types)
