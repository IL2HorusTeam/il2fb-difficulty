# -*- coding: utf-8 -*-
"""
Different helpers.
"""

try:
    from django.conf import settings
    if settings.configured:
        from django.utils.translation import ugettext_lazy
        _ = ugettext_lazy
    else:
        raise ImportError()
except ImportError:
    def _(value):
        return value


def evaluate_string(value):
    return None if value is None else unicode(value)
