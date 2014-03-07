# -*- coding: utf-8 -*-
"""
Difficulty constants.
"""
from collections import OrderedDict
from il2ds_difficulty.helpers import _

# -----------------------------------------------------------------------------
# All settings codes
# -----------------------------------------------------------------------------

WIND_TURBULENCE = 'WindTurbulence'
FLUTTER_EFFECT = 'FlutterEffect'
STALL_SPINS = 'StallSpins'
BLACKOUTS_REDOUTS = 'BlackoutsRedouts'
ENGINE_OVERHEAT = 'EngineOverheat'
TORQUE_GYRO_EFFECTS = 'TorqueGyroEffects'
REALISTIC_LANDING = 'RealisticLanding'
TAKEOFF_LANDING = 'TakeoffLanding'
COCKPIT_ALWAYS_ON = 'CockpitAlwaysOn'
NO_OUTSIDE_VIEWS = 'NoOutSideViews'
HEAD_SHAKE = 'HeadShake'
NO_ICONS = 'NoIcons'
REALISTIC_GUNNERY = 'RealisticGunnery'
LIMITED_AMMO = 'LimitedAmmo'
LIMITED_FUEL = 'LimitedFuel'
VULNERABILITY = 'Vulnerability'
NO_PADLOCK = 'NoPadlock'
CLOUDS = 'Clouds'
NO_MAP_ICONS = 'NoMapIcons'
SEPARATE_ENGINE_START = 'SeparateEStart'
NO_INSTANT_SUCCESS = 'NoInstantSuccess'
NO_MINIMAP_PATH = 'NoMinimapPath'
NO_SPEED_BAR = 'NoSpeedBar'
COMPLEX_ENGINE_MANAGEMENT = 'ComplexEManagement'
RELIABILITY = 'Reliability'
OVERLOAD_LIMITS = 'GLimits'
REALISTIC_PILOT_VULNERABILITY = 'RealisticPilotVulnerability'
REALISTIC_NAVIGATION_INSTRUMENTS = 'RealisticNavigationInstruments'
NO_PLAYER_ICON = 'NoPlayerIcon'
NO_FOG_OF_WAR_ICONS = 'NoFogOfWarIcons'
BOMB_FUZES = 'BombFuzes'
REALISTIC_TORPEDOING = 'RealisticTorpedoing'
REALISTIC_MISSILES_VARIATION = 'RealisticMissilesVariation'
NO_SELF_VIEW = 'NoSelfView'
NO_FOE_VIEW = 'NoFoeView'
NO_FRIENDLY_VIEW = 'NoFriendlyView'
NO_PLANES_VIEW = 'NoPlanesView'
NO_AIRCRAFT_CARRIER_VIEW = 'NoACarrierView'

# -----------------------------------------------------------------------------
# All settings names and descriptions
# -----------------------------------------------------------------------------

SETTINGS_NAMES_MAP = {
    WIND_TURBULENCE: (
        _("Wind and turbulence"),
        None,
    ),
    FLUTTER_EFFECT: (
        _("Flutter"),
        None,
    ),
    STALL_SPINS: (
        _("Stall spins"),
        None,
    ),
    BLACKOUTS_REDOUTS: (
        _("Blackouts and redouts"),
        None,
    ),
    ENGINE_OVERHEAT: (
        _("Engine overheat"),
        None,
    ),
    TORQUE_GYRO_EFFECTS: (
        _("Gyroscopic moment"),
        None,
    ),
    REALISTIC_LANDING: (
        _("Realistic landing"),
        None,
    ),
    TAKEOFF_LANDING: (
        _("Take-off and landing"),
        None,
    ),
    COCKPIT_ALWAYS_ON: (
        _("Cockpit always on"),
        _("Look from cockpit only"),
    ),
    NO_OUTSIDE_VIEWS: (
        _("No outside views"),
        None,
    ),
    HEAD_SHAKE: (
        _("Head shake"),
        None,
    ),
    NO_ICONS: (
        _("No icons"),
        _("Do not display player icons on map"),
    ),
    REALISTIC_GUNNERY: (
        _("Realistic gunnery"),
        None,
    ),
    LIMITED_AMMO: (
        _("Limited ammunition"),
        None,
    ),
    LIMITED_FUEL: (
        _("Limited fuel"),
        None,
    ),
    VULNERABILITY: (
        _("Vulnerability"),
        None,
    ),
    NO_PADLOCK: (
        _("No look fixation"),
        None,
    ),
    CLOUDS: (
        _("Clouds"),
        None,
    ),
    NO_MAP_ICONS: (
        _("No map icons"),
        _("Disable markers on map"),
    ),
    SEPARATE_ENGINE_START: (
        _("Separate engine start"),
        None,
    ),
    NO_INSTANT_SUCCESS: (
        _("No instant success"),
        _("Complete tasks"),
    ),
    NO_MINIMAP_PATH: (
        _("No minimap path"),
        _("Without a route on map"),
    ),
    NO_SPEED_BAR: (
        _("No speed bar"),
        _("Without speed indicator"),
    ),
    COMPLEX_ENGINE_MANAGEMENT: (
        _("Complex engine management"),
        _("Full engine control"),
    ),
    RELIABILITY: (
        _("Reliability"),
        _("Real reliability of engines"),
    ),
    OVERLOAD_LIMITS: (
        _("Overload limits"),
        _("Dynamic overload limits"),
    ),
    REALISTIC_PILOT_VULNERABILITY: (
        _("Realistic pilot vulnerability"),
        None,
    ),
    REALISTIC_NAVIGATION_INSTRUMENTS: (
        _("Realistic navigation instruments"),
        None,
    ),
    NO_PLAYER_ICON: (
        _("No player icon"),
        _("Player icon is not shown on map"),
    ),
    NO_FOG_OF_WAR_ICONS: (
        _("No fog of war icons"),
        _("Disable intelligence icons on map"),
    ),
    BOMB_FUZES: (
        _("Bomb fuses"),
        None,
    ),
    REALISTIC_TORPEDOING: (
        _("Realistic torpedoing"),
        None,
    ),
    REALISTIC_MISSILES_VARIATION: (
        _("Realistic spread of missiles"),
        None,
    ),
    NO_SELF_VIEW: (
        _("No self view"),
        _("Without own view"),
    ),
    NO_FOE_VIEW: (
        _("No foe view"),
        _("Without view of enemies"),
    ),
    NO_FRIENDLY_VIEW: (
        _("No friendly view"),
        _("Without view of friends"),
    ),
    NO_PLANES_VIEW: (
        _("No planes view"),
        _("Without view of aircraft"),
    ),
    NO_AIRCRAFT_CARRIER_VIEW: (
        _("No aircraft carrier view"),
        _("Without view of aircraft carriers"),
    ),
}

SETTINGS_NAMES_MAP = {
    code: {
        'title': title,
        'description': description,
    } for code, (title, description) in SETTINGS_NAMES_MAP.iteritems()
}

# -----------------------------------------------------------------------------
# All tabs codes
# -----------------------------------------------------------------------------

TAB_FLIGHT_MODEL = 'flight_model'
TAB_WEAPONS = 'weapons'
TAB_VIEW = 'view'
TAB_ICONS_N_MAP = 'icons_n_map'
TAB_MISC = 'misc'

# -----------------------------------------------------------------------------
# All tabs names
# -----------------------------------------------------------------------------

TABS_NAMES_MAP = {
    TAB_FLIGHT_MODEL: _("Flight model"),
    TAB_WEAPONS: _("Weapons"),
    TAB_VIEW: _("View"),
    TAB_ICONS_N_MAP: _("Icons and map"),
    TAB_MISC: _("Miscellaneous"),
}

# -----------------------------------------------------------------------------
# Settings set for 4.12
# -----------------------------------------------------------------------------

SETTINGS_4_12 = OrderedDict([
    (TAB_FLIGHT_MODEL, OrderedDict([
        (WIND_TURBULENCE, 0),
        (FLUTTER_EFFECT, 1),
        (STALL_SPINS, 2),
        (BLACKOUTS_REDOUTS, 3),
        (ENGINE_OVERHEAT, 4),
        (TORQUE_GYRO_EFFECTS, 5),
        (REALISTIC_LANDING, 6),
        (TAKEOFF_LANDING, 7),
        (OVERLOAD_LIMITS, 25),
    ])),
    (TAB_VIEW, OrderedDict([
        (COCKPIT_ALWAYS_ON, 8),
        (NO_OUTSIDE_VIEWS, 9),
        (HEAD_SHAKE, 10),
        (NO_PADLOCK, 16),
        (NO_SELF_VIEW, 33),
        (NO_FOE_VIEW, 34),
        (NO_FRIENDLY_VIEW, 35),
        (NO_PLANES_VIEW, 36),
        (NO_AIRCRAFT_CARRIER_VIEW, 37),
    ])),
    (TAB_MISC, OrderedDict([
        (NO_ICONS, 11),
        (REALISTIC_GUNNERY, 12),
        (LIMITED_AMMO, 13),
        (LIMITED_FUEL, 14),
        (VULNERABILITY, 15),
        (CLOUDS, 17),
        (NO_MAP_ICONS, 18),
        (NO_INSTANT_SUCCESS, 20),
        (NO_MINIMAP_PATH, 21),
        (NO_SPEED_BAR, 22),
        (REALISTIC_PILOT_VULNERABILITY, 26),
        (REALISTIC_NAVIGATION_INSTRUMENTS, 27),
        (NO_PLAYER_ICON, 28),
        (NO_FOG_OF_WAR_ICONS, 29),
        (BOMB_FUZES, 30),
        (REALISTIC_TORPEDOING, 31),
        (REALISTIC_MISSILES_VARIATION, 32),
        (ENGINE_OVERHEAT, 4),
        (SEPARATE_ENGINE_START, 19),
        (COMPLEX_ENGINE_MANAGEMENT, 23),
        (RELIABILITY, 24),
    ])),
])

NUMBERS_MAP_4_12 = reduce(lambda x, y: dict(x, **y), SETTINGS_4_12.values())

# -----------------------------------------------------------------------------
# General constants
# -----------------------------------------------------------------------------

SETTINGS = {
    '4.12': SETTINGS_4_12,
    '4.12.1': SETTINGS_4_12,
    '4.12.2': SETTINGS_4_12,
}

NUMBERS_MAPS = {
    '4.12': NUMBERS_MAP_4_12,
    '4.12.1': NUMBERS_MAP_4_12,
    '4.12.2': NUMBERS_MAP_4_12,
}

DEFAULT_GAME_VERSION = '4.12.2'
