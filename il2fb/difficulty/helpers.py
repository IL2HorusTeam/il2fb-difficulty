# -*- coding: utf-8 -*-
"""
Different helpers.
"""
try:
    from django.conf import settings
    if settings.configured:
        from django.utils.translation import ugettext_lazy as _
    else:
        raise ImportError()
except ImportError:
    from gettext import gettext as _


def evaluate_string(value):
    return None if value is None else unicode(value)
