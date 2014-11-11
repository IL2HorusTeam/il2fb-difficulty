# -*- coding: utf-8 -*-

from candv import ValueConstant
from collections import OrderedDict
from il2fb.commons import GameVersions
from six import string_types

from il2fb.difficulty.utils import translations, flatten_dict

from .v4_12 import SETTINGS as SETTINGS_4_12, PRESETS as PRESETS_4_12


_ = translations.ugettext

SETTINGS = OrderedDict([
    (GameVersions.v4_12, SETTINGS_4_12),
    (GameVersions.v4_12_1, SETTINGS_4_12),
    (GameVersions.v4_12_2, SETTINGS_4_12),
])

PRESETS = OrderedDict([
    (GameVersions.v4_12, PRESETS_4_12),
    (GameVersions.v4_12_1, PRESETS_4_12),
    (GameVersions.v4_12_2, PRESETS_4_12),
])


def get_settings(game_version=None):
    game_version = normalize_game_version(game_version)
    return SETTINGS[game_version]


def get_flat_settings(game_version=None):
    return flatten_dict(get_settings(game_version))


def get_presets(game_version=None):
    game_version = normalize_game_version(game_version)
    return PRESETS[game_version]


def normalize_game_version(value):

    value = value or GameVersions.get_default()

    if isinstance(value, ValueConstant):
        if value.name in GameVersions:
            version = value
        else:
            _on_invalid_version(value)
    else:
        if not isinstance(value, string_types):
            raise TypeError(_("Game version is not a string"))
        try:
            version = GameVersions.get_by_value(value)
        except ValueError:
            _on_invalid_version(value)

    if version not in SETTINGS:
        _on_invalid_version(value)

    return version


def _on_invalid_version(value):
    supported_versions = ', '.join([str(x.value) for x in SETTINGS.keys()])
    raise ValueError(_("Unknown game version '{:}'. Supported versions: {:}.")
                     .format(value, supported_versions))
