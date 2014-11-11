# -*- coding: utf-8 -*-

from collections import OrderedDict
from il2fb.commons import GameVersions

from .v4_12 import SETTINGS as SETTINGS_4_12, PRESETS as PRESETS_4_12


ALL_INFO = (
    (GameVersions.v4_12, SETTINGS_4_12, PRESETS_4_12),
    (GameVersions.v4_12_1, SETTINGS_4_12, PRESETS_4_12),
    (GameVersions.v4_12_2, SETTINGS_4_12, PRESETS_4_12),
)

SETTINGS = OrderedDict([
    (k, v) for k, v, __ in ALL_INFO
])

PRESETS = OrderedDict([
    (k, v) for k, __, v in ALL_INFO
])
