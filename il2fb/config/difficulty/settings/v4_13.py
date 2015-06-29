# -*- coding: utf-8 -*-
from __future__ import absolute_import

from collections import OrderedDict

from ..constants import PARAMETERS, TABS, PRESET_TYPES, RULE_TYPES


SETTINGS = OrderedDict([
    (TABS.FLIGHT_MODEL, OrderedDict([
        (PARAMETERS.SEPARATE_ENGINE_START, 19),
        (PARAMETERS.COMPLEX_ENGINE_MANAGEMENT, 23),
        (PARAMETERS.ENGINE_OVERHEAT, 4),
        (PARAMETERS.TORQUE_N_GYRO_EFFECTS, 5),
        (PARAMETERS.FLUTTER_EFFECT, 1),
        (PARAMETERS.STALLS_N_SPINS, 2),
        (PARAMETERS.BLACKOUTS_N_REDOUTS, 3),
        (PARAMETERS.OVERLOAD_LIMITS, 26),
        (PARAMETERS.RELIABILITY, 25),
    ])),
    (TABS.WEAPONS, OrderedDict([
        (PARAMETERS.REALISTIC_GUNNERY, 12),
        (PARAMETERS.LIMITED_AMMO, 13),
        (PARAMETERS.LIMITED_FUEL, 14),
        (PARAMETERS.BOMB_FUZES, 31),
        (PARAMETERS.FRAGILE_TORPEDOES, 32),
        (PARAMETERS.REALISTIC_ROCKETS_SPREAD, 38),
        (PARAMETERS.REALISTIC_BOMBSIGHTS, 42),
    ])),
    (TABS.VIEW, OrderedDict([
        (PARAMETERS.NO_OUTSIDE_VIEWS, 9),
        (PARAMETERS.NO_OWN_PLAYER_VIEWS, 37),
        (PARAMETERS.NO_ENEMY_VIEWS, 33),
        (PARAMETERS.NO_FRIENDLY_VIEWS, 34),
        (PARAMETERS.NO_AIRCRAFT_VIEWS, 36),
        (PARAMETERS.NO_SEA_UNIT_VIEWS, 35),
        (PARAMETERS.COCKPIT_ALWAYS_ON, 8),
        (PARAMETERS.NO_SPEED_BAR, 22),
        (PARAMETERS.NO_PADLOCK, 16),
        (PARAMETERS.NO_GROUND_PADLOCK, 41),
    ])),
    (TABS.ICONS_N_MAP, OrderedDict([
        (PARAMETERS.NO_MAP_ICONS, 18),
        (PARAMETERS.NO_PLAYER_ICON, 29),
        (PARAMETERS.NO_FOG_OF_WAR_ICONS, 30),
        (PARAMETERS.NO_MINIMAP_PATH, 21),
        (PARAMETERS.NO_ICONS, 11),
    ])),
    (TABS.MISC, OrderedDict([
        (PARAMETERS.VULNERABILITY, 15),
        (PARAMETERS.REALISTIC_PILOT_VULNERABILITY, 27),
        (PARAMETERS.NO_INSTANT_SUCCESS, 20),
        (PARAMETERS.TAKEOFF_N_LANDING, 7),
        (PARAMETERS.REALISTIC_LANDING, 6),
        (PARAMETERS.REALISTIC_NAVIGATION_INSTRUMENTS, 28),
        (PARAMETERS.SHARED_KILLS, 39),
        (PARAMETERS.SHARED_KILLS_HISTORICAL, 40),
        (PARAMETERS.HEAD_SHAKE, 10),
        (PARAMETERS.WIND_N_TURBULENCE, 0),
        (PARAMETERS.CLOUDS, 17),
    ])),
])

RULES = {
    PARAMETERS.NO_OUTSIDE_VIEWS: {
        True: {
            RULE_TYPES.TURNS_ON: [
                PARAMETERS.NO_OWN_PLAYER_VIEWS,
                PARAMETERS.NO_ENEMY_VIEWS,
                PARAMETERS.NO_FRIENDLY_VIEWS,
                PARAMETERS.NO_AIRCRAFT_VIEWS,
                PARAMETERS.NO_SEA_UNIT_VIEWS,
            ],
            RULE_TYPES.LOCKS: [
                PARAMETERS.NO_OWN_PLAYER_VIEWS,
                PARAMETERS.NO_ENEMY_VIEWS,
                PARAMETERS.NO_FRIENDLY_VIEWS,
                PARAMETERS.NO_AIRCRAFT_VIEWS,
                PARAMETERS.NO_SEA_UNIT_VIEWS,
            ],
        },
        False: {
            RULE_TYPES.UNLOCKS: [
                PARAMETERS.NO_OWN_PLAYER_VIEWS,
                PARAMETERS.NO_ENEMY_VIEWS,
                PARAMETERS.NO_FRIENDLY_VIEWS,
                PARAMETERS.NO_AIRCRAFT_VIEWS,
                PARAMETERS.NO_SEA_UNIT_VIEWS,
            ],
        },
    },
    PARAMETERS.NO_MAP_ICONS: {
        True: {
            RULE_TYPES.UNLOCKS: [
                PARAMETERS.NO_FOG_OF_WAR_ICONS,
            ],
        },
        False: {
            RULE_TYPES.TURNS_ON: [
                PARAMETERS.NO_FOG_OF_WAR_ICONS,
            ],
            RULE_TYPES.LOCKS: [
                PARAMETERS.NO_FOG_OF_WAR_ICONS,
            ],
        }
    },
    PARAMETERS.SHARED_KILLS: {
        True: {
            RULE_TYPES.UNLOCKS: [
                PARAMETERS.SHARED_KILLS_HISTORICAL,
            ],
        },
        False: {
            RULE_TYPES.TURNS_OFF: [
                PARAMETERS.SHARED_KILLS_HISTORICAL,
            ],
            RULE_TYPES.LOCKS: [
                PARAMETERS.SHARED_KILLS_HISTORICAL,
            ],
        }
    },
}

PRESETS = OrderedDict([
    (PRESET_TYPES.EASY, 1090682880),
    (PRESET_TYPES.NORMAL, 6704004351),
    (PRESET_TYPES.FULL_REAL, 8796093022207),
])
