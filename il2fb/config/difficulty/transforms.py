# -*- coding: utf-8 -*-


def inverse_dict(source):
    return {v: k for k, v in source.items()}


def flatten_settings(settings):
    return {k: v for i in settings.values() for k, v in i.items()}
