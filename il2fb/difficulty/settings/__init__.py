# -*- coding: utf-8 -*-
from candv import ValueConstant
from il2fb.commons import GAME_VERSIONS
from six import string_types

from il2fb.difficulty.utils import translations, flatten_settings
from .v4_12 import SETTINGS as SETTINGS_4_12


_ = translations.ugettext

DEFAULT_GAME_VERSION = GAME_VERSIONS.v4_12_2

SETTINGS = {
    GAME_VERSIONS.v4_12: SETTINGS_4_12,
    GAME_VERSIONS.v4_12_1: SETTINGS_4_12,
    GAME_VERSIONS.v4_12_2: SETTINGS_4_12,
}


def get_settings(game_version=DEFAULT_GAME_VERSION):
    game_version = normalize_game_version(game_version)
    return SETTINGS[game_version]


def normalize_game_version(value):

    def _on_invalid_version():
        supported_versions = sorted([x.value for x in SETTINGS.keys()])
        raise ValueError(_("Unknown game version. Supported versions: {:}")
                         .format(', '.join(supported_versions)))

    if isinstance(value, ValueConstant):
        if GAME_VERSIONS.contains(value.name):
            version = value
        else:
            _on_invalid_version()
    else:
        if not isinstance(value, string_types):
            raise TypeError(_("Game version is not a string"))
        try:
            version = GAME_VERSIONS.get_by_value(value)
        except ValueError:
            _on_invalid_version()

    if not version in SETTINGS:
        _on_invalid_version()

    return version


def get_flat_settings(game_version=DEFAULT_GAME_VERSION):
    return flatten_settings(get_settings(game_version))
