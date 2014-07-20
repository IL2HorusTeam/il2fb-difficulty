# -*- coding: utf-8 -*-
import os

from verboselib.factory import TranslationsFactory


_here = os.path.abspath(os.path.dirname(__file__))

translations = TranslationsFactory("il2fb-difficulty",
                                   os.path.join(_here, "locale"))


def inverse_dict(source):
    return {v: k for k, v in source.items()}


def flatten_settings(settings):
    return {k: v for i in settings.values() for k, v in i.items()}
