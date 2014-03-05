# -*- coding: utf-8 -*-
"""
Different helpers.
"""

try:
    from django.conf import settings
    if settings.configured:
        from django.utils.translation import ugettext
        _ = ugettext
    else:
        raise ImportError()
except ImportError:
    def _(value):
        return value
