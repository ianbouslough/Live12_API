# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
# [Clang 6.0 (clang-600.0.57)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launchkey_Mini_MK3/skin.py
# Compiled at: 2023-12-06 17:21:23
# Size of source mod 2**32: 872 bytes
from __future__ import absolute_import, print_function, unicode_literals
from builtins import object
from ableton.v2.control_surface import Skin, merge_skins
from novation.colors import Mono, Rgb
from novation.skin import skin as base_skin

class Colors(object):

    class Recording(object):
        On = Mono.ON
        Off = Mono.OFF

    class TrackNavigation(object):
        On = Mono.HALF
        Pressed = Mono.ON

    class SceneNavigation(object):
        On = Mono.HALF
        Pressed = Mono.ON

    class DrumGroup(object):
        PadSelected = Rgb.WHITE
        PadSelectedNotSoloed = Rgb.WHITE
        PadMutedSelected = Rgb.WHITE
        PadSoloedSelected = Rgb.WHITE
        Navigation = Rgb.WHITE_HALF
        NavigationPressed = Rgb.WHITE


skin = merge_skins(base_skin, Skin(Colors)*())