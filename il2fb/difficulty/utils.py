# -*- coding: utf-8 -*-

import os

from verboselib.factory import TranslationsFactory


__here__ = os.path.abspath(os.path.dirname(__file__))

locale_dir = os.path.join(__here__, "locale")
translations = TranslationsFactory("il2fb-difficulty", locale_dir)


def inverse_dict(source):
    return {v: k for k, v in source.items()}


def flatten_settings(settings):
    return {k: v for i in settings.values() for k, v in i.items()}
