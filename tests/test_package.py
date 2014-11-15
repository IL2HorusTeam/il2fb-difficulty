# -*- coding: utf-8 -*-
import unittest

from collections import OrderedDict
from il2fb.commons import GameVersions

from il2fb.difficulty import (
    is_position_set, decompose, decompose_to_tabs, compose, compose_from_tabs,
    get_settings, get_flat_settings, get_presets, get_preset_value,
    get_parameter_position, is_parameter_set, get_rules, get_actual_rules,
    get_parameter_lockers, toggle_parameter, toggle_parameter_raw,
)
from il2fb.difficulty.constants import (
    TABS, PARAMETERS, PRESETS as ALL_PRESETS, RULE_TYPES,
)
from il2fb.difficulty.exceptions import LockedParameterException
from il2fb.difficulty.settings import SETTINGS, RULES, PRESETS


def get_all_settings(value):
    """
    Get all settings for default game version with specified value.
    """
    settings = get_flat_settings()
    values = [value, ] * len(settings)
    return dict(zip(settings.keys(), values))


get_all_enabled_settings = lambda: get_all_settings(True)
get_all_disabled_settings = lambda: get_all_settings(False)


class BaseTestCase(unittest.TestCase):

    game_version = GameVersions.v4_12

    def assertRaisesWithMessage(self, exception_type, message, func, *args, **kwargs):
        try:
            func(*args, **kwargs)
        except exception_type as e:
            self.assertEqual(e.args[0], message)
        else:
            self.fail('"{:}" was expected to throw "{:}" exception'
                      .format(func.__name__, exception_type.__name__))


class PackageTestCase(BaseTestCase):

    def test_is_position_set(self):
        # Check 0 does not contain 1
        self.assertFalse(is_position_set(0, 0))

        # Check 1 contains 1
        self.assertTrue(is_position_set(1, 0))

        # Check 5 contains 1
        self.assertTrue(is_position_set(5, 0))
        # Check 5 does not contain 2
        self.assertFalse(is_position_set(5, 1))
        # Check 5 contains 4
        self.assertTrue(is_position_set(5, 2))

    def test_decompose(self):
        settings = get_all_disabled_settings()
        settings.update({
            PARAMETERS.FLUTTER_EFFECT: True,
            PARAMETERS.NO_SPEED_BAR: True,
            PARAMETERS.LIMITED_AMMO: True,
            PARAMETERS.TAKEOFF_LANDING: True,
        })
        self.assertEqual(decompose(4202626), settings)

    def test_decompose_to_tabs(self):
        settings = OrderedDict([
            (TABS.FLIGHT_MODEL, OrderedDict([
                (PARAMETERS.SEPARATE_ENGINE_START, False),
                (PARAMETERS.COMPLEX_ENGINE_MANAGEMENT, False),
                (PARAMETERS.ENGINE_OVERHEAT, False),
                (PARAMETERS.TORQUE_GYRO_EFFECTS, False),

                # 'True' value
                (PARAMETERS.FLUTTER_EFFECT, True),

                (PARAMETERS.STALL_SPINS, False),
                (PARAMETERS.BLACKOUTS_REDOUTS, False),
                (PARAMETERS.OVERLOAD_LIMITS, False),
                (PARAMETERS.RELIABILITY, False),
            ])),
            (TABS.WEAPONS, OrderedDict([
                (PARAMETERS.REALISTIC_GUNNERY, False),

                # 'True' value
                (PARAMETERS.LIMITED_AMMO, True),

                (PARAMETERS.LIMITED_FUEL, False),
                (PARAMETERS.BOMB_FUZES, False),
                (PARAMETERS.FRAGILE_TORPS, False),
                (PARAMETERS.REALISTIC_ROCKETS_SPREAD, False),
            ])),
            (TABS.VIEW, OrderedDict([
                (PARAMETERS.NO_OUTSIDE_VIEWS, False),
                (PARAMETERS.NO_OWN_PLAYER_VIEWS, False),
                (PARAMETERS.NO_FOE_VIEW, False),
                (PARAMETERS.NO_FRIENDLY_VIEW, False),
                (PARAMETERS.NO_AIRCRAFT_VIEWS, False),
                (PARAMETERS.NO_SEA_UNIT_VIEWS, False),
                (PARAMETERS.COCKPIT_ALWAYS_ON, False),

                # 'True' value
                (PARAMETERS.NO_SPEED_BAR, True),

                (PARAMETERS.NO_PADLOCK, False),
                (PARAMETERS.NO_GROUND_PADLOCK, False),
            ])),
            (TABS.ICONS_N_MAP, OrderedDict([
                (PARAMETERS.NO_MAP_ICONS, False),
                (PARAMETERS.NO_PLAYER_ICON, False),
                (PARAMETERS.NO_FOG_OF_WAR_ICONS, False),
                (PARAMETERS.NO_MINIMAP_PATH, False),
                (PARAMETERS.NO_ICONS, False),
            ])),
            (TABS.MISC, OrderedDict([
                (PARAMETERS.VULNERABILITY, False),
                (PARAMETERS.REALISTIC_PILOT_VULNERABILITY, False),
                (PARAMETERS.NO_INSTANT_SUCCESS, False),

                # 'True' value
                (PARAMETERS.TAKEOFF_LANDING, True),

                (PARAMETERS.REALISTIC_LANDING, False),
                (PARAMETERS.REALISTIC_NAVIGATION_INSTRUMENTS, False),
                (PARAMETERS.SHARED_KILLS, False),
                (PARAMETERS.SHARED_KILLS_HISTORICAL, False),
                (PARAMETERS.HEAD_SHAKE, False),
                (PARAMETERS.WIND_TURBULENCE, False),
                (PARAMETERS.CLOUDS, False),
            ])),
        ])
        self.assertEqual(decompose_to_tabs(4202626), settings)

    def test_compose(self):
        settings = get_all_disabled_settings()
        settings.update({
            PARAMETERS.FLUTTER_EFFECT: True,
            PARAMETERS.NO_SPEED_BAR: True,
            PARAMETERS.LIMITED_AMMO: True,
            PARAMETERS.TAKEOFF_LANDING: True,
        })
        self.assertEqual(compose(settings), 4202626)

    def test_compose_from_tabs(self):
        settings = {
            TABS.FLIGHT_MODEL: {
                PARAMETERS.SEPARATE_ENGINE_START: False,
                PARAMETERS.COMPLEX_ENGINE_MANAGEMENT: False,
                PARAMETERS.ENGINE_OVERHEAT: False,
                PARAMETERS.TORQUE_GYRO_EFFECTS: False,

                # 'True' value
                PARAMETERS.FLUTTER_EFFECT: True,

                PARAMETERS.STALL_SPINS: False,
                PARAMETERS.BLACKOUTS_REDOUTS: False,
                PARAMETERS.OVERLOAD_LIMITS: False,
                PARAMETERS.RELIABILITY: False,
            },
            TABS.WEAPONS: {
                PARAMETERS.REALISTIC_GUNNERY: False,

                # 'True' value
                PARAMETERS.LIMITED_AMMO: True,

                PARAMETERS.LIMITED_FUEL: False,
                PARAMETERS.BOMB_FUZES: False,
                PARAMETERS.FRAGILE_TORPS: False,
                PARAMETERS.REALISTIC_ROCKETS_SPREAD: False,
            },
            TABS.VIEW: {
                PARAMETERS.NO_OUTSIDE_VIEWS: False,
                PARAMETERS.NO_OWN_PLAYER_VIEWS: False,
                PARAMETERS.NO_FOE_VIEW: False,
                PARAMETERS.NO_FRIENDLY_VIEW: False,
                PARAMETERS.NO_AIRCRAFT_VIEWS: False,
                PARAMETERS.NO_SEA_UNIT_VIEWS: False,
                PARAMETERS.COCKPIT_ALWAYS_ON: False,

                # 'True' value
                PARAMETERS.NO_SPEED_BAR: True,

                PARAMETERS.NO_PADLOCK: False,
                PARAMETERS.NO_GROUND_PADLOCK: False,
            },
            TABS.ICONS_N_MAP: {
                PARAMETERS.NO_MAP_ICONS: False,
                PARAMETERS.NO_PLAYER_ICON: False,
                PARAMETERS.NO_FOG_OF_WAR_ICONS: False,
                PARAMETERS.NO_MINIMAP_PATH: False,
                PARAMETERS.NO_ICONS: False,
            },
            TABS.MISC: {
                PARAMETERS.VULNERABILITY: False,
                PARAMETERS.REALISTIC_PILOT_VULNERABILITY: False,
                PARAMETERS.NO_INSTANT_SUCCESS: False,

                # 'True' value
                PARAMETERS.TAKEOFF_LANDING: True,

                PARAMETERS.REALISTIC_LANDING: False,
                PARAMETERS.REALISTIC_NAVIGATION_INSTRUMENTS: False,
                PARAMETERS.SHARED_KILLS: False,
                PARAMETERS.SHARED_KILLS_HISTORICAL: False,
                PARAMETERS.HEAD_SHAKE: False,
                PARAMETERS.WIND_TURBULENCE: False,
                PARAMETERS.CLOUDS: False,
            },
        }
        self.assertEqual(compose_from_tabs(settings), 4202626)

    def test_get_settings(self):
        self.assertEqual(
            get_settings(GameVersions.v4_12),
            SETTINGS[GameVersions.v4_12]
        )

    def test_get_flat_settings(self):
        flat = {
            PARAMETERS.BLACKOUTS_REDOUTS: 3,
            PARAMETERS.BOMB_FUZES: 31,
            PARAMETERS.CLOUDS: 17,
            PARAMETERS.COCKPIT_ALWAYS_ON: 8,
            PARAMETERS.COMPLEX_ENGINE_MANAGEMENT: 23,
            PARAMETERS.ENGINE_OVERHEAT: 4,
            PARAMETERS.FLUTTER_EFFECT: 1,
            PARAMETERS.FRAGILE_TORPS: 32,
            PARAMETERS.HEAD_SHAKE: 10,
            PARAMETERS.LIMITED_AMMO: 13,
            PARAMETERS.LIMITED_FUEL: 14,
            PARAMETERS.NO_AIRCRAFT_VIEWS: 36,
            PARAMETERS.NO_FOE_VIEW: 33,
            PARAMETERS.NO_FOG_OF_WAR_ICONS: 30,
            PARAMETERS.NO_FRIENDLY_VIEW: 34,
            PARAMETERS.NO_GROUND_PADLOCK: 41,
            PARAMETERS.NO_ICONS: 11,
            PARAMETERS.NO_INSTANT_SUCCESS: 20,
            PARAMETERS.NO_MAP_ICONS: 18,
            PARAMETERS.NO_MINIMAP_PATH: 21,
            PARAMETERS.NO_OUTSIDE_VIEWS: 9,
            PARAMETERS.NO_OWN_PLAYER_VIEWS: 37,
            PARAMETERS.NO_PADLOCK: 16,
            PARAMETERS.NO_PLAYER_ICON: 29,
            PARAMETERS.NO_SEA_UNIT_VIEWS: 35,
            PARAMETERS.NO_SPEED_BAR: 22,
            PARAMETERS.OVERLOAD_LIMITS: 26,
            PARAMETERS.REALISTIC_GUNNERY: 12,
            PARAMETERS.REALISTIC_LANDING: 6,
            PARAMETERS.REALISTIC_NAVIGATION_INSTRUMENTS: 28,
            PARAMETERS.REALISTIC_PILOT_VULNERABILITY: 27,
            PARAMETERS.REALISTIC_ROCKETS_SPREAD: 38,
            PARAMETERS.RELIABILITY: 25,
            PARAMETERS.SEPARATE_ENGINE_START: 19,
            PARAMETERS.SHARED_KILLS: 39,
            PARAMETERS.SHARED_KILLS_HISTORICAL: 40,
            PARAMETERS.STALL_SPINS: 2,
            PARAMETERS.TAKEOFF_LANDING: 7,
            PARAMETERS.TORQUE_GYRO_EFFECTS: 5,
            PARAMETERS.VULNERABILITY: 15,
            PARAMETERS.WIND_TURBULENCE: 0,
        }

        self.assertEqual(get_flat_settings(GameVersions.v4_12), flat)

    def test_get_presets(self):
        self.assertEqual(
            get_presets(GameVersions.v4_12),
            PRESETS[GameVersions.v4_12]
        )

    def test_get_preset_value(self):
        value = get_preset_value(ALL_PRESETS.EASY, GameVersions.v4_12)
        self.assertEqual(value, 1090682880)

    def test_get_parameter_position(self):
        position = get_parameter_position(PARAMETERS.WIND_TURBULENCE,
                                          GameVersions.v4_12)
        self.assertEqual(position, 0)

    def test_is_parameter_set(self):
        self.assertFalse(is_parameter_set(0, PARAMETERS.WIND_TURBULENCE))
        self.assertTrue(is_parameter_set(1, PARAMETERS.WIND_TURBULENCE))

    def test_get_rules(self):
        self.assertEqual(
            get_rules(self.game_version),
            RULES[self.game_version]
        )

    def test_get_actual_rules(self):
        difficulty = 0

        self.assertEqual(
            get_actual_rules(difficulty, self.game_version),
            {
                PARAMETERS.NO_OUTSIDE_VIEWS: {
                    RULE_TYPES.UNLOCKS: [
                        PARAMETERS.NO_OWN_PLAYER_VIEWS,
                        PARAMETERS.NO_FOE_VIEW,
                        PARAMETERS.NO_FRIENDLY_VIEW,
                        PARAMETERS.NO_AIRCRAFT_VIEWS,
                        PARAMETERS.NO_SEA_UNIT_VIEWS,
                    ],
                },
                PARAMETERS.NO_MAP_ICONS: {
                    RULE_TYPES.TURNS_ON: [
                        PARAMETERS.NO_FOG_OF_WAR_ICONS,
                    ],
                    RULE_TYPES.LOCKS: [
                        PARAMETERS.NO_FOG_OF_WAR_ICONS,
                    ],
                },
                PARAMETERS.SHARED_KILLS: {
                    RULE_TYPES.TURNS_OFF: [
                        PARAMETERS.SHARED_KILLS_HISTORICAL,
                    ],
                    RULE_TYPES.LOCKS: [
                        PARAMETERS.SHARED_KILLS_HISTORICAL,
                    ],
                },
            }
        )

        parameters = [
            PARAMETERS.NO_OUTSIDE_VIEWS, PARAMETERS.NO_MAP_ICONS,
            PARAMETERS.SHARED_KILLS,
        ]
        for parameter in parameters:
            difficulty, __ = toggle_parameter(difficulty,
                                              parameter,
                                              True,
                                              self.game_version)

        self.assertEqual(
            get_actual_rules(difficulty, self.game_version),
            {
                PARAMETERS.NO_OUTSIDE_VIEWS: {
                    RULE_TYPES.TURNS_ON: [
                        PARAMETERS.NO_OWN_PLAYER_VIEWS,
                        PARAMETERS.NO_FOE_VIEW,
                        PARAMETERS.NO_FRIENDLY_VIEW,
                        PARAMETERS.NO_AIRCRAFT_VIEWS,
                        PARAMETERS.NO_SEA_UNIT_VIEWS,
                    ],
                    RULE_TYPES.LOCKS: [
                        PARAMETERS.NO_OWN_PLAYER_VIEWS,
                        PARAMETERS.NO_FOE_VIEW,
                        PARAMETERS.NO_FRIENDLY_VIEW,
                        PARAMETERS.NO_AIRCRAFT_VIEWS,
                        PARAMETERS.NO_SEA_UNIT_VIEWS,
                    ],
                },
                PARAMETERS.NO_MAP_ICONS: {
                    RULE_TYPES.UNLOCKS: [
                        PARAMETERS.NO_FOG_OF_WAR_ICONS,
                    ],
                },
                PARAMETERS.SHARED_KILLS: {
                    RULE_TYPES.UNLOCKS: [
                        PARAMETERS.SHARED_KILLS_HISTORICAL,
                    ],
                },
            }
        )

    def test_get_parameter_lockers(self):
        difficulty = 0

        locker = PARAMETERS.NO_OUTSIDE_VIEWS
        parameter = PARAMETERS.NO_OWN_PLAYER_VIEWS

        self.assertSequenceEqual(
            get_parameter_lockers(difficulty, parameter, self.game_version),
            []
        )

        difficulty, __ = toggle_parameter(difficulty,
                                          locker,
                                          True,
                                          self.game_version)

        self.assertSequenceEqual(
            get_parameter_lockers(difficulty,
                                  parameter,
                                  self.game_version),
            [locker, ]
        )

    def test_toggle_parameter_raw(self):
        settings = get_flat_settings(self.game_version)
        self.assertEqual(
            toggle_parameter_raw(0, PARAMETERS.WIND_TURBULENCE, True, settings),
            1)
        self.assertEqual(
            toggle_parameter_raw(1, PARAMETERS.WIND_TURBULENCE, False, settings),
            0)


class ParameterTogglerTestCase(BaseTestCase):

    def test_toggle_on(self):
        difficulty, __ = toggle_parameter(0,
                                          PARAMETERS.WIND_TURBULENCE,
                                          True,
                                          self.game_version)
        self.assertEqual(difficulty, 1)

    def test_toggle_off(self):
        difficulty, __ = toggle_parameter(1,
                                          PARAMETERS.WIND_TURBULENCE,
                                          False,
                                          self.game_version)
        self.assertEqual(difficulty, 0)

    def test_no_side_effects_for_toggle_on(self):
        __, side_effects = toggle_parameter(0,
                                            PARAMETERS.WIND_TURBULENCE,
                                            True,
                                            self.game_version)
        self.assertFalse(side_effects)

    def test_no_side_effects_for_toggle_off(self):
        __, side_effects = toggle_parameter(1,
                                            PARAMETERS.WIND_TURBULENCE,
                                            False,
                                            self.game_version)
        self.assertFalse(side_effects)

    def test_positive_side_effects_for_toggle_on(self):
        difficulty, side_effects = toggle_parameter(0,
                                                    PARAMETERS.NO_OUTSIDE_VIEWS,
                                                    True,
                                                    self.game_version)
        self.assertEqual(
            difficulty,
            sum([1 << get_parameter_position(x, self.game_version)
                for x in [
                    PARAMETERS.NO_OUTSIDE_VIEWS,
                    PARAMETERS.NO_OWN_PLAYER_VIEWS,
                    PARAMETERS.NO_FOE_VIEW,
                    PARAMETERS.NO_FRIENDLY_VIEW,
                    PARAMETERS.NO_AIRCRAFT_VIEWS,
                    PARAMETERS.NO_SEA_UNIT_VIEWS,
                ]
            ])
        )
        self.assertEqual(
            side_effects,
            {
                RULE_TYPES.TURNS_ON: [
                    PARAMETERS.NO_OWN_PLAYER_VIEWS,
                    PARAMETERS.NO_FOE_VIEW,
                    PARAMETERS.NO_FRIENDLY_VIEW,
                    PARAMETERS.NO_AIRCRAFT_VIEWS,
                    PARAMETERS.NO_SEA_UNIT_VIEWS,
                ],
                RULE_TYPES.LOCKS: [
                    PARAMETERS.NO_OWN_PLAYER_VIEWS,
                    PARAMETERS.NO_FOE_VIEW,
                    PARAMETERS.NO_FRIENDLY_VIEW,
                    PARAMETERS.NO_AIRCRAFT_VIEWS,
                    PARAMETERS.NO_SEA_UNIT_VIEWS,
                ],
            }
        )

    def test_negative_side_effects_for_toggle_on(self):
        difficulty, side_effects = toggle_parameter(0,
                                                    PARAMETERS.SHARED_KILLS,
                                                    True,
                                                    self.game_version)
        difficulty, side_effects = toggle_parameter(difficulty,
                                                    PARAMETERS.SHARED_KILLS_HISTORICAL,
                                                    True,
                                                    self.game_version)
        difficulty, side_effects = toggle_parameter(difficulty,
                                                    PARAMETERS.SHARED_KILLS,
                                                    False,
                                                    self.game_version)

        self.assertEqual(difficulty, 0)
        self.assertEqual(
            side_effects,
            {
                RULE_TYPES.TURNS_OFF: [
                    PARAMETERS.SHARED_KILLS_HISTORICAL,
                ],
                RULE_TYPES.LOCKS: [
                    PARAMETERS.SHARED_KILLS_HISTORICAL,
                ],
            }
        )

    def test_side_effects_for_toggle_off(self):
        difficulty = sum([
            1 << get_parameter_position(x, self.game_version)
            for x in [
                PARAMETERS.NO_OUTSIDE_VIEWS,
                PARAMETERS.NO_OWN_PLAYER_VIEWS,
                PARAMETERS.NO_FOE_VIEW,
                PARAMETERS.NO_FRIENDLY_VIEW,
                PARAMETERS.NO_AIRCRAFT_VIEWS,
                PARAMETERS.NO_SEA_UNIT_VIEWS,
            ]
        ])
        difficulty, side_effects = toggle_parameter(difficulty,
                                                    PARAMETERS.NO_OUTSIDE_VIEWS,
                                                    False,
                                                    self.game_version)

        self.assertEqual(
            difficulty,
            sum([1 << get_parameter_position(x, self.game_version)
                for x in [
                    PARAMETERS.NO_OWN_PLAYER_VIEWS,
                    PARAMETERS.NO_FOE_VIEW,
                    PARAMETERS.NO_FRIENDLY_VIEW,
                    PARAMETERS.NO_AIRCRAFT_VIEWS,
                    PARAMETERS.NO_SEA_UNIT_VIEWS,
                ]
            ])
        )
        self.assertEqual(
            side_effects,
            {
                RULE_TYPES.UNLOCKS: [
                    PARAMETERS.NO_OWN_PLAYER_VIEWS,
                    PARAMETERS.NO_FOE_VIEW,
                    PARAMETERS.NO_FRIENDLY_VIEW,
                    PARAMETERS.NO_AIRCRAFT_VIEWS,
                    PARAMETERS.NO_SEA_UNIT_VIEWS,
                ],
            }
        )

    def test_toogle_locked_parameter(self):
        difficulty, __ = toggle_parameter(0,
                                          PARAMETERS.NO_OUTSIDE_VIEWS,
                                          True,
                                          self.game_version)

        self.assertRaisesWithMessage(
            LockedParameterException,
            "Parameter 'NoOwnPlayerViews' is locked by 'NoOutSideViews' "
            "accordingly to the rules of game version 4.12.",
            toggle_parameter,
            difficulty,
            PARAMETERS.NO_OWN_PLAYER_VIEWS,
            True,
            self.game_version)
