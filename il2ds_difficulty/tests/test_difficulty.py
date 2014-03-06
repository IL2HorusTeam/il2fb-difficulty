# -*- coding: utf-8 -*-
"""
 Testing the application il2ds_difficulty
"""
import unittest

from il2ds_difficulty import decompose_difficulty, callback_difficulty
from il2ds_difficulty.constants import DEFAULT_GAME_VERSION


class DecomposeDifficultyTest(unittest.TestCase):

    def test_all_false(self):
        difficulty = 0
        settings = decompose_difficulty(difficulty, DEFAULT_GAME_VERSION)
        self.assertFalse(any(settings.values()))

    def test_callback_true(self):
        """
        Test il2ds_difficulty.callback_difficulty
        Return value = 4202626
        Settings True: FlutterEffect, TakeoffLanding, LimitedAmmo and NoSpeedBar
        """
        settings = {
            'NoSpeedBar': True,
            'BlackoutsRedouts': False,
            'RealisticGunnery': False,
            'SeparateEStart': False,
            'NoSelfView': False,
            'ComplexEManagement': False,
            'StallSpins': False,
            'RealisticMissilesVariation': False,
            'RealisticNavigationInstruments': False,
            'NoFriendlyView': False,
            'FlutterEffect': True,
            'NoOutSideViews': False,
            'RealisticLanding': False,
            'RealisticPilotVulnerability': False,
            'HeadShake': False,
            'GLimits': False,
            'NoMinimapPath': False,
            'NoMapIcons': False,
            'NoIcons': False,
            'WindTurbulence': False,
            'NoPlayerIcon': False,
            'CockpitAlwaysOn': False,
            'TakeoffLanding': True,
            'BombFuzes': False,
            'NoFoeView': False,
            'Clouds': False,
            'LimitedAmmo': True,
            'TorqueGyroEffects': False,
            'NoFogOfWarIcons': False,
            'EngineOverheat': False,
            'NoPlanesView': False,
            'RealisticTorpedoing': False,
            'Vulnerability': False,
            'NoACarrierView': False,
            'Reliability': False,
            'NoInstantSuccess': False,
            'NoPadlock': False,
            'LimitedFuel': False,
        }
        difficulty = callback_difficulty(settings, DEFAULT_GAME_VERSION)