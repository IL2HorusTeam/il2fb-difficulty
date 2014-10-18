# -*- coding: utf-8 -*-

from candv import Constants, Values, VerboseConstant, VerboseValueConstant

from .utils import translations


_ = translations.ugettext_lazy


class PARAMETERS(Values):
    WIND_TURBULENCE = VerboseValueConstant(
        value='WindTurbulence',
        verbose_name=_("Wind and turbulence"),
    )
    FLUTTER_EFFECT = VerboseValueConstant(
        value='FlutterEffect',
        verbose_name=_("Flutter"),
    )
    STALL_SPINS = VerboseValueConstant(
        value='StallSpins',
        verbose_name=_("Stall spins"),
    )
    BLACKOUTS_REDOUTS = VerboseValueConstant(
        value='BlackoutsRedouts',
        verbose_name=_("Blackouts and redouts"),
    )
    ENGINE_OVERHEAT = VerboseValueConstant(
        value='EngineOverheat',
        verbose_name=_("Engine overheat"),
    )
    TORQUE_GYRO_EFFECTS = VerboseValueConstant(
        value='TorqueGyroEffects',
        verbose_name=_("Gyroscopic moment"),
    )
    REALISTIC_LANDING = VerboseValueConstant(
        value='RealisticLanding',
        verbose_name=_("Realistic landing"),
    )
    TAKEOFF_LANDING = VerboseValueConstant(
        value='TakeoffLanding',
        verbose_name=_("Take-off and landing"),
    )
    COCKPIT_ALWAYS_ON = VerboseValueConstant(
        value='CockpitAlwaysOn',
        verbose_name=_("Cockpit always on"),
    )
    NO_OUTSIDE_VIEWS = VerboseValueConstant(
        value='NoOutSideViews',
        verbose_name=_("No outside views"),
    )
    HEAD_SHAKE = VerboseValueConstant(
        value='HeadShake',
        verbose_name=_("Head shake"),
    )
    NO_ICONS = VerboseValueConstant(
        value='NoIcons',
        verbose_name=_("No icons"),
        help_text=_("Do not display player icons on map"),
    )
    REALISTIC_GUNNERY = VerboseValueConstant(
        value='RealisticGunnery',
        verbose_name=_("Realistic gunnery"),
    )
    LIMITED_AMMO = VerboseValueConstant(
        value='LimitedAmmo',
        verbose_name=_("Limited ammunition"),
    )
    LIMITED_FUEL = VerboseValueConstant(
        value='LimitedFuel',
        verbose_name=_("Limited fuel"),
    )
    VULNERABILITY = VerboseValueConstant(
        value='Vulnerability',
        verbose_name=_("Vulnerability"),
    )
    NO_PADLOCK = VerboseValueConstant(
        value='NoPadlock',
        verbose_name=_("No look fixation on air targets"),
    )
    CLOUDS = VerboseValueConstant(
        value='Clouds',
        verbose_name=_("Clouds"),
    )
    NO_MAP_ICONS = VerboseValueConstant(
        value='NoMapIcons',
        verbose_name=_("No map icons"),
    )
    SEPARATE_ENGINE_START = VerboseValueConstant(
        value='SeparateEStart',
        verbose_name=_("Separate start of engines"),
    )
    NO_INSTANT_SUCCESS = VerboseValueConstant(
        value='NoInstantSuccess',
        verbose_name=_("No instant success"),
    )
    NO_MINIMAP_PATH = VerboseValueConstant(
        value='NoMinimapPath',
        verbose_name=_("No minimap path"),
    )
    NO_SPEED_BAR = VerboseValueConstant(
        value='NoSpeedBar',
        verbose_name=_("No speed bar"),
    )
    COMPLEX_ENGINE_MANAGEMENT = VerboseValueConstant(
        value='ComplexEManagement',
        verbose_name=_("Complex engine management"),
    )
    RELIABILITY = VerboseValueConstant(
        value='Reliability',
        verbose_name=_("Reliability"),
    )
    OVERLOAD_LIMITS = VerboseValueConstant(
        value='GLimits',
        verbose_name=_("Overload limits"),
    )
    REALISTIC_PILOT_VULNERABILITY = VerboseValueConstant(
        value='RealisticPilotVulnerability',
        verbose_name=_("Realistic pilot vulnerability"),
    )
    REALISTIC_NAVIGATION_INSTRUMENTS = VerboseValueConstant(
        value='RealisticNavigationInstruments',
        verbose_name=_("Realistic navigation instruments"),
    )
    NO_PLAYER_ICON = VerboseValueConstant(
        value='NoPlayerIcon',
        verbose_name=_("No player icon"),
        help_text=_("Player icon is not shown on map"),
    )
    NO_FOG_OF_WAR_ICONS = VerboseValueConstant(
        value='NoFogOfWarIcons',
        verbose_name=_("No fog of war icons"),
        help_text=_("Disable intelligence icons on map"),
    )
    BOMB_FUZES = VerboseValueConstant(
        value='BombFuzes',
        verbose_name=_("Bomb fuses"),
    )
    REALISTIC_TORPEDOING = VerboseValueConstant(
        value='RealisticTorpedoing',
        verbose_name=_("Realistic torpedoing"),
    )
    #: Deprecated approximately since v4.11
    REALISTIC_MISSILES_VARIATION = VerboseValueConstant(
        value='RealisticMissilesVariation',
        verbose_name=_("Realistic spread of missiles"),
    )
    NO_SELF_VIEW = VerboseValueConstant(
        value='NoSelfView',
        verbose_name=_("No self view"),
    )
    NO_FOE_VIEW = VerboseValueConstant(
        value='NoFoeView',
        verbose_name=_("No foe view"),
        help_text=_("Without view of enemies")
    )
    NO_FRIENDLY_VIEW = VerboseValueConstant(
        value='NoFriendlyView',
        verbose_name=_("No friendly view"),
        help_text=_("Without view of friends"),
    )
    #: Deprecated approximately since v4.11
    NO_PLANES_VIEW = VerboseValueConstant(
        value='NoPlanesView',
        verbose_name=_("No planes view"),
    )
    #: Deprecated approximately since v4.11
    NO_AIRCRAFT_CARRIER_VIEW = VerboseValueConstant(
        value='NoACarrierView',
        verbose_name=_("No aircraft carrier view"),
        help_text=_("Without view of aircraft carriers"),
    )
    #: Introduced in v4.12
    NO_GROUND_PADLOCK = VerboseValueConstant(
        value='No_GroundPadlock',
        verbose_name=_("No look fixation on ground targets"),
    )
    #: Introduced in v4.12
    SHARED_KILLS = VerboseValueConstant(
        value='SharedKills',
        verbose_name=_("Group win"),
    )
    #: Introduced in v4.12
    SHARED_KILLS_HISTORICAL = VerboseValueConstant(
        value='SharedKillsHistorical',
        verbose_name=_("Historical limitation for group win"),
    )
    #: Introduced in v4.12
    REALISTIC_ROCKETS_SPREAD = VerboseValueConstant(
        value='RealisticRocketSpread',
        verbose_name=_("Realistic spread of missiles"),
    )
    #: Introduced approximately in v4.11
    NO_SEA_UNIT_VIEWS = VerboseValueConstant(
        value='NoSeaUnitViews',
        verbose_name=_("No aircraft carrier view"),
        help_text=_("Without view of aircraft carriers"),
    )
    #: Introduced approximately in v4.11
    NO_AIRCRAFT_VIEWS = VerboseValueConstant(
        value='NoAircraftViews',
        verbose_name=_("No planes view"),
        help_text=_("Without view of aircraft"),
    )
    #: Introduced approximately in v4.11
    FRAGILE_TORPS = VerboseValueConstant(
        value='FragileTorps',
        verbose_name=_("Realistic torpedoing"),
    )
    #: Available only for server
    NO_OWN_PLAYER_VIEWS = VerboseValueConstant(
        value='NoOwnPlayerViews',
        verbose_name=_("No self view after takeoff"),
        help_text=_("You can look at your own plane from outside only before "
                    "takeoff")
    )


class TABS(Constants):
    FLIGHT_MODEL = VerboseConstant(_("Flight model"))
    WEAPONS = VerboseConstant(_("Flight model"))
    VIEW = VerboseConstant(_("View"))
    ICONS_N_MAP = VerboseConstant(_("Icons and map"))
    MISC = VerboseConstant(_("Miscellaneous"))
