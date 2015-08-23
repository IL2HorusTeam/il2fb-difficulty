# -*- coding: utf-8 -*-

import six
import unittest

from il2fb.config.difficulty.constants import (
    PARAMETERS, TABS, RULE_TYPES, PRESET_TYPES, SETTINGS, RULES, PRESETS,
)


class StructuresTestCase(unittest.TestCase):
    """
    This test ensures all settings have a proper data structure which is
    retained across game versions.
    """

    def test_settings_structure(self):
        available_tabs = set(TABS.constants())
        available_paramaters = set(PARAMETERS.constants())

        for tab, paramaters in SETTINGS.items():
            self.assertIn(tab, available_tabs)
            self.assertIsInstance(paramaters, dict)

            for paramater, position in paramaters.items():
                self.assertIn(paramater, available_paramaters)
                self.assertIsInstance(position, six.integer_types)

    def test_rules_structure(self):
        available_paramaters = set(PARAMETERS.constants())
        available_rule_types = set(RULE_TYPES.constants())

        for master, states in RULES.items():
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

        for preset_type, value in PRESETS.items():
            self.assertIn(preset_type, available_preset_types)
            self.assertIsInstance(value, six.integer_types)
