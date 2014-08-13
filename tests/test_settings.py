# -*- coding: utf-8 -*-
import unittest

from il2fb.commons import GameVersions, Skills
from il2fb.difficulty.constants import PARAMETERS
from il2fb.difficulty.settings import (
    get_settings, get_flat_settings, normalize_game_version, SETTINGS,
)


class SettingsTestCase(unittest.TestCase):

    def test_normalize_game_version(self):
        self.assertEqual(normalize_game_version('4.12.2'),
                         GameVersions.v4_12_2)
        self.assertEqual(normalize_game_version(GameVersions.v4_12_2),
                         GameVersions.v4_12_2)

        self.assertRaises(TypeError, normalize_game_version, 412)
        self.assertRaises(ValueError, normalize_game_version, Skills.rookie)
        self.assertRaises(ValueError, normalize_game_version, '4.12.99')

    def test_get_settings(self):
        self.assertEqual(get_settings(GameVersions.v4_12),
                         SETTINGS[GameVersions.v4_12])
        self.assertEqual(get_settings('4.12.2'),
                         SETTINGS[GameVersions.v4_12_2])

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
        self.assertEqual(get_flat_settings('4.12.2'), flat)
