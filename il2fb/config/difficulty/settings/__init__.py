# -*- coding: utf-8 -*-

from collections import OrderedDict
from il2fb.commons import GameVersions

from .v4_12 import (
    SETTINGS as SETTINGS_4_12, PRESETS as PRESETS_4_12,
    RULES as RULES_4_12,
)


ALL_INFO = (

    # v4.12 -------------------------------------------------------------------
    (GameVersions.v4_12, SETTINGS_4_12, RULES_4_12, PRESETS_4_12),
    (GameVersions.v4_12_1, SETTINGS_4_12, RULES_4_12, PRESETS_4_12),
    (GameVersions.v4_12_2, SETTINGS_4_12, RULES_4_12, PRESETS_4_12),
)

SETTINGS = OrderedDict([
    (k, v) for k, v, __, __ in ALL_INFO
])

RULES = OrderedDict([
    (k, v) for k, __, v, __ in ALL_INFO
])

PRESETS = OrderedDict([
    (k, v) for k, __, __, v in ALL_INFO
])
