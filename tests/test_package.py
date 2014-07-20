# -*- coding: utf-8 -*-
import unittest

from collections import OrderedDict

from il2fb.difficulty import (
    is_parameter_set, decompose, decompose_to_tabs, compose, compose_from_tabs,
)
from il2fb.difficulty.constants import TABS, PARAMETERS
from il2fb.difficulty.settings import get_flat_settings


def get_all_settings(value):
    """
    Get all settings for default game version with specified value.
    """
    settings = get_flat_settings()
    values = [value, ] * len(settings)
    return dict(zip(settings.keys(), values))


get_all_enabled_settings = lambda: get_all_settings(True)
get_all_disabled_settings = lambda: get_all_settings(False)


class CommonTestCase(unittest.TestCase):

    def test_is_parameter_set(self):
        # Check 0 does not contain 1
        self.assertFalse(is_parameter_set(0, 0))

        # Check 1 contains 1
        self.assertTrue(is_parameter_set(1, 0))

        # Check 5 contains 1
        self.assertTrue(is_parameter_set(5, 0))
        # Check 5 does not contain 2
        self.assertFalse(is_parameter_set(5, 1))
        # Check 5 contains 4
        self.assertTrue(is_parameter_set(5, 2))

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
                (PARAMETERS.NO_FOE_VIEW, False),
                (PARAMETERS.NO_FRIENDLY_VIEW, False),
                (PARAMETERS.NO_AIRCRAFT_VIEWS, False),
                (PARAMETERS.NO_SEA_UNIT_VIEWS, False),
                (PARAMETERS.COCKPIT_ALWAYS_ON, False),

                # 'True' value
                (PARAMETERS.NO_SPEED_BAR, True),

                (PARAMETERS.NO_PADLOCK, False),
                (PARAMETERS.NO_GROUND_PADLOCK, False),
                (PARAMETERS.NO_OWN_PLAYER_VIEWS, False),
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
                PARAMETERS.NO_FOE_VIEW: False,
                PARAMETERS.NO_FRIENDLY_VIEW: False,
                PARAMETERS.NO_AIRCRAFT_VIEWS: False,
                PARAMETERS.NO_SEA_UNIT_VIEWS: False,
                PARAMETERS.COCKPIT_ALWAYS_ON: False,

                # 'True' value
                PARAMETERS.NO_SPEED_BAR: True,

                PARAMETERS.NO_PADLOCK: False,
                PARAMETERS.NO_GROUND_PADLOCK: False,
                PARAMETERS.NO_OWN_PLAYER_VIEWS: False,
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
