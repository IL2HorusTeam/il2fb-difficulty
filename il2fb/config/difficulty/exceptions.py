# -*- coding: utf-8 -*-

from .utils import translations


_ = translations.ugettext


class LockedParameterException(Exception):
    """
    Raise this exception when someone wants to toggle some parameter while it's
    locked by some another parameter accordingly to the rules.

    >>> from verboselib import use_language
    >>> from il2fb.commons import GameVersions
    >>> from il2fb.config.difficulty.constants import PARAMETERS
    >>> e = LockedParameterException(PARAMETERS.NO_OWN_PLAYER_VIEWS,
    ...                              [PARAMETERS.NO_OUTSIDE_VIEWS, ],
    ...                              GameVersions.v4_12)
    >>> use_language('en')
    >>> str(e)
    "Parameter 'NoOwnPlayerViews' is locked by 'NoOutSideViews' accordingly to the rules of game version '4.12'."
    """

    def __init__(self, parameter, lockers, game_version):
        self.parameter = parameter
        self.lockers = lockers
        self.game_version = game_version

        lockers = ', '.join(["'{0}'".format(x.value) for x in lockers])

        super(LockedParameterException, self).__init__(
            _("Parameter '{parameter}' is locked by {lockers} accordingly "
              "to the rules of game version '{version}'.")
            .format(parameter=parameter.value,
                    lockers=lockers,
                    version=game_version.value))
