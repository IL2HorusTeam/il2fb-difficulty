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
REALISTIC_MISSILES_VARIATION = 'RealisticMissilesVariation'  # delete in version ~ 4.11
NO_SELF_VIEW = 'NoSelfView'
NO_FOE_VIEW = 'NoFoeView'
NO_FRIENDLY_VIEW = 'NoFriendlyView'
NO_PLANES_VIEW = 'NoPlanesView'  # delete in version ~ 4.11
NO_AIRCRAFT_CARRIER_VIEW = 'NoACarrierView'  # delete in version ~ 4.11
NO_GROUND_PADLOCK = 'No_GroundPadlock '  # add in version 4.12
SHARED_KILLS = 'SharedKills'  # add in version 4.12
SHARED_KILLS_HISTORICAL = 'SharedKillsHistorical'  # add in version 4.12
REALISTIC_ROCKETS_SPREAD = 'RealisticRocketSpread '  # add in version 4.12
NO_SEA_UNIT_VIEWS = 'NoSeaUnitViews '  # add in version ~ 4.11
NO_AIRCRAFT_VIEWS = 'NoAircraftViews '  # add in version ~ 4.11
FRAGILE_TORPS = 'FragileTorps '  # add in version ~ 4.11
NO_OWN_PLAYER_VIEWS = 'NoOwnPlayerViews'  # No in client IL-2 FB

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
        None,
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
        _("No look fixation on air targets"),
        None,
    ),
    CLOUDS: (
        _("Clouds"),
        None,
    ),
    NO_MAP_ICONS: (
        _("No map icons"),
        None,
    ),
    SEPARATE_ENGINE_START: (
        _("Separate engine start"),
        None,
    ),
    NO_INSTANT_SUCCESS: (
        _("No instant success"),
        None,
    ),
    NO_MINIMAP_PATH: (
        _("No minimap path"),
        None,
    ),
    NO_SPEED_BAR: (
        _("No speed bar"),
        None,
    ),
    COMPLEX_ENGINE_MANAGEMENT: (
        _("Complex engine management"),
        None,
    ),
    RELIABILITY: (
        _("Reliability"),
        None,
    ),
    OVERLOAD_LIMITS: (
        _("Overload limits"),
        None,
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
        None,
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
        None,
    ),
    NO_AIRCRAFT_CARRIER_VIEW: (
        _("No aircraft carrier view"),
        _("Without view of aircraft carriers"),
    ),
    NO_GROUND_PADLOCK: (
        _("No look fixation on ground targets"),
        None,
    ),
    SHARED_KILLS: (
        _("Group win"),
        None,
    ),
    SHARED_KILLS_HISTORICAL: (
        _("Group win (historical limitation)"),
        None,
    ),
    REALISTIC_ROCKETS_SPREAD: (
        _("Realistic spread of missiles"),
        None,
    ),
    NO_SEA_UNIT_VIEWS: (
        _("No aircraft carrier view"),
        _("Without view of aircraft carriers"),
    ),
    NO_AIRCRAFT_VIEWS: (
        _("No planes view"),
        _("Without view of aircraft"),
    ),
    FRAGILE_TORPS: (
        _("Realistic torpedoing"),
        None,
    ),
    NO_OWN_PLAYER_VIEWS: (
        _("No own view"),
        _("You can look at your own plane from outside only before takeoff"),
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
        (SEPARATE_ENGINE_START, 19),
        (COMPLEX_ENGINE_MANAGEMENT, 23),
        (ENGINE_OVERHEAT, 4),
        (TORQUE_GYRO_EFFECTS, 5),
        (FLUTTER_EFFECT, 1),
        (STALL_SPINS, 2),
        (BLACKOUTS_REDOUTS, 3),
        (OVERLOAD_LIMITS, 26),
        (RELIABILITY, 25),
    ])),
    (TAB_WEAPONS, OrderedDict([
        (REALISTIC_GUNNERY, 12),
        (LIMITED_AMMO, 13),
        (LIMITED_FUEL, 14),
        (BOMB_FUZES, 31),
        (FRAGILE_TORPS, 32),
        (REALISTIC_ROCKETS_SPREAD, 38),
    ])),
    (TAB_VIEW, OrderedDict([
        (NO_OUTSIDE_VIEWS, 9),
        (NO_FOE_VIEW, 33),
        (NO_FRIENDLY_VIEW, 34),
        (NO_AIRCRAFT_VIEWS, 36),
        (NO_SEA_UNIT_VIEWS, 35),
        (COCKPIT_ALWAYS_ON, 8),
        (NO_SPEED_BAR, 22),
        (NO_PADLOCK, 16),
        (NO_GROUND_PADLOCK, 41),
        (NO_OWN_PLAYER_VIEWS, 37),
    ])),
    (TAB_ICONS_N_MAP, OrderedDict([
        (NO_MAP_ICONS, 18),
        (NO_PLAYER_ICON, 29),
        (NO_FOG_OF_WAR_ICONS, 30),
        (NO_MINIMAP_PATH, 21),
        (NO_ICONS, 11),
    ])),
    (TAB_MISC, OrderedDict([
        (VULNERABILITY, 15),
        (REALISTIC_PILOT_VULNERABILITY, 27),
        (NO_INSTANT_SUCCESS, 20),
        (TAKEOFF_LANDING, 7),
        (REALISTIC_LANDING, 6),
        (REALISTIC_NAVIGATION_INSTRUMENTS, 28),
        (SHARED_KILLS, 39),
        (SHARED_KILLS_HISTORICAL, 40),
        (HEAD_SHAKE, 10),
        (WIND_TURBULENCE, 0),
        (CLOUDS, 17),
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
