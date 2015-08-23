# -*- coding: utf-8 -*-

from .utils import translations


_ = translations.ugettext


class LockedParameterException(Exception):
    """
    Raise this exception when someone wants to toggle some parameter while it's
    locked by some another parameter accordingly to the rules.

    >>> from il2fb.config.difficulty.constants import PARAMETERS
    >>>
    >>> e = LockedParameterException(PARAMETERS.NO_OWN_PLAYER_VIEWS,
    ...                              [PARAMETERS.NO_OUTSIDE_VIEWS, ])
    >>> raise e # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    LockedParameterException: Parameter 'NoOwnPlayerViews' is locked by 'NoOutSideViews' accordingly to the rules of game.
    """

    def __init__(self, parameter, lockers):
        self.parameter = parameter
        self.lockers = lockers

        lockers = ', '.join(["'{0}'".format(x.value) for x in lockers])

        super(LockedParameterException, self).__init__(
            _("Parameter '{parameter}' is locked by {lockers} accordingly "
              "to the rules of game.")
            .format(parameter=parameter.value, lockers=lockers))
