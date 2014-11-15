# -*- coding: utf-8 -*-


class LockedParameterException(Exception):
    """
    Raise this exception when someone wants to toggle some parameter while it's
    locked by some another parameter accordingly to the rules.
    """

    def __init__(self, parameter, lockers, game_version):
        self.parameter = parameter
        self.lockers = lockers
        self.game_version = game_version

        lockers = ', '.join(["'%s'" % x.value for x in lockers])

        super(LockedParameterException, self).__init__(
            "Parameter '{:}' is locked by {:} accordingly to the rules of "
            "game version {:}."
            .format(parameter.value, lockers, game_version.value))
