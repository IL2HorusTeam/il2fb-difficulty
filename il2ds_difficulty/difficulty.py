# -*- coding: utf-8 -*-
"""
Convert integer value of game difficulty into dictionary and vice versa.
"""


# Return the parameter value (True or False)
def get_difficulty(self, code):
    code = (1 << code) & self
    if code:
        return True
    else:
        return False


# Retrieves parameters of the digital code
def get_difficulty_settings(self, code):
    difficulty = {}
    if self:
        for key in self:
            difficulty.update({self[key]: get_difficulty(code, key)})
        return difficulty