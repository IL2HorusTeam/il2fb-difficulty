# -*- coding: utf-8 -*-
"""
Difficulty constants.
"""
import itertools

try:
    from django.conf import settings
    if settings.configured:
        from django.utils.translation import ugettext as _
    else:
        raise ImportError()
except ImportError:
    def _(value):
        return value

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
        _("Description"),
    ),
    FLUTTER_EFFECT: (
        _("Flutter"),
        _("Description"),
    ),
    STALL_SPINS: (
        _("Tailspin"),
        _("Description"),
    ),
    BLACKOUTS_REDOUTS: (
        _("Overload"),
        _("Description"),
    ),
    ENGINE_OVERHEAT: (
        _("Engine overheating"),
        _("Description"),
    ),
    TORQUE_GYRO_EFFECTS: (
        _("Gyroscopic moment"),
        _("Description"),
    ),
    REALISTIC_LANDING: (
        _("Realistic landing"),
        _("Description"),
    ),
    TAKEOFF_LANDING: (
        _("Take-off and landing"),
        _("Description"),
    ),
    COCKPIT_ALWAYS_ON: (
        _("View only from the cockpit"),
        _("Description"),
    ),
    NO_OUTSIDE_VIEWS: (
        _("No outside views"),
        _("Description"),
    ),
    HEAD_SHAKE: (
        _("Moving head"),
        _("Description"),
    ),
    NO_ICONS: (
        _("Without icons players"),
        _("Description"),
    ),
    REALISTIC_GUNNERY: (
        _("Realistic shooting"),
        _("Description"),
    ),
    LIMITED_AMMO: (
        _("Limited ammunition"),
        _("Description"),
    ),
    LIMITED_FUEL: (
        _("Limited supply of fuel"),
        _("Description"),
    ),
    VULNERABILITY: (
        _("Vulnerability"),
        _("Description"),
    ),
    NO_PADLOCK: (
        _("Disable glance fixation"),
        _("Description"),
    ),
    CLOUDS: (
        _("Clouds"),
        _("Description"),
    ),
    NO_MAP_ICONS: (
        _("Disable the markers on the map"),
        _("Description"),
    ),
    SEPARATE_ENGINE_START: (
        _("Separate engine starting"),
        _("Description"),
    ),
    NO_INSTANT_SUCCESS: (
        _("Complete the task"),
        _("Description"),
    ),
    NO_MINIMAP_PATH: (
        _("Without the route on the map"),
        _("Description"),
    ),
    NO_SPEED_BAR: (
        _("Without speed indicator"),
        _("Description"),
    ),
    COMPLEX_ENGINE_MANAGEMENT: (
        _("Full engine control"),
        _("Description"),
    ),
    RELIABILITY: (
        _("Real reliability of engines"),
        _("Description"),
    ),
    OVERLOAD_LIMITS: (
        _("Dynamic overload restriction"),
        _("Description"),
    ),
    REALISTIC_PILOT_VULNERABILITY: (
        _("Realistic vulnerability pilot"),
        _("Description"),
    ),
    REALISTIC_NAVIGATION_INSTRUMENTS: (
        _("Realistic navigation"),
        _("Description"),
    ),
    NO_PLAYER_ICON: (
        _("To disable a player on the map"),
        _("Description"),
    ),
    NO_FOG_OF_WAR_ICONS: (
        _("Disable icons intelligence on the map"),
        _("Description"),
    ),
    BOMB_FUZES: (
        _("Bomb fuses"),
        _("Description"),
    ),
    REALISTIC_TORPEDOING: (
        _("Realistic torpedoing"),
        _("Description"),
    ),
    REALISTIC_MISSILES_VARIATION: (
        _("Realistic spread of missiles"),
        _("Description"),
    ),
    NO_SELF_VIEW: (
        _("Without your own review"),
        _("Description"),
    ),
    NO_FOE_VIEW: (
        _("Without a review of the enemy"),
        _("Description"),
    ),
    NO_FRIENDLY_VIEW: (
        _("Without friends"),
        _("Description"),
    ),
    NO_PLANES_VIEW: (
        _("Without a review of the aircraft"),
        _("Description"),
    ),
    NO_AIRCRAFT_CARRIER_VIEW: (
        _("Without a review of aircraft carriers"),
        _("Description"),
    ),
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

DIFFICULTY_4_12 = (
    (TAB_FLIGHT_MODEL, (
        (WIND_TURBULENCE, 0),
        (FLUTTER_EFFECT, 1),
        (STALL_SPINS, 2),
        (BLACKOUTS_REDOUTS, 3),
        (ENGINE_OVERHEAT, 4),
        (TORQUE_GYRO_EFFECTS, 5),
        (REALISTIC_LANDING, 6),
        (TAKEOFF_LANDING, 7),
        (OVERLOAD_LIMITS, 25),
    )),
    (TAB_VIEW, (
        (COCKPIT_ALWAYS_ON, 8),
        (NO_OUTSIDE_VIEWS, 9),
        (HEAD_SHAKE, 10),
        (NO_PADLOCK, 16),
        (NO_SELF_VIEW, 33),
        (NO_FOE_VIEW, 34),
        (NO_FRIENDLY_VIEW, 35),
        (NO_PLANES_VIEW, 36),
        (NO_AIRCRAFT_CARRIER_VIEW, 37),
    )),
    (TAB_MISC, (
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
    )),
)

NUMBERS_MAP_4_12 = {
    code: number for code, number
                 in itertools.chain(*dict(DIFFICULTY_4_12).values())
}

print NUMBERS_MAP_4_12

# -----------------------------------------------------------------------------
# General constants
# -----------------------------------------------------------------------------

NUMBERS_MAPS = {
    '4.12': NUMBERS_MAP_4_12,
    '4.12.1': NUMBERS_MAP_4_12,
    '4.12.2': NUMBERS_MAP_4_12,
}

DEFAULT_GAME_VERSION = '4.12.2'
