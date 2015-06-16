# -*- coding: utf-8 -*-

from collections import OrderedDict
from il2fb.commons import GameVersions

from . import v4_12, v4_13

ALL_INFO = (
    (GameVersions.v4_12, v4_12.SETTINGS, v4_12.RULES, v4_12.PRESETS),
    (GameVersions.v4_13, v4_13.SETTINGS, v4_13.RULES, v4_13.PRESETS),
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
