# -*- coding: utf-8 -*-

from .utils import translations


_ = translations.ugettext


class LockedParameterException(Exception):
    """
    Raise this exception when someone wants to toggle some parameter while it's
    locked by some another parameter accordingly to the rules.
    """

    def __init__(self, parameter, lockers, game_version):
        self.parameter = parameter
        self.lockers = lockers
        self.game_version = game_version

        lockers = ', '.join(["'{0}'".format(x.value) for x in lockers])

        super(LockedParameterException, self).__init__(
            _("Parameter '{parameter}' is locked by '{lockers}' accordingly "
              "to the rules of game version '{version}'.")
            .format(parameter=parameter.value,
                    lockers=lockers,
                    version=game_version.value))
