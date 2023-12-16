# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
# [Clang 6.0 (clang-600.0.57)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launchpad_Pro_MK3/skin.py
# Compiled at: 2023-12-06 17:21:23
# Size of source mod 2**32: 1264 bytes
from __future__ import absolute_import, print_function, unicode_literals
from builtins import object
from ableton.v2.control_surface import Skin, merge_skins
from novation.colors import Rgb
from novation.skin import skin as base_skin

class Colors(object):

    class Device(object):
        Navigation = Rgb.DARK_BLUE_HALF
        NavigationPressed = Rgb.WHITE

    class Mode(object):

        class Device(object):
            On = Rgb.DARK_BLUE
            Off = Rgb.WHITE_HALF

            class Bank(object):
                Selected = Rgb.DARK_BLUE
                Available = Rgb.WHITE_HALF

        class Sends(object):
            On = Rgb.VIOLET
            Off = Rgb.WHITE_HALF

            class Bank(object):
                Available = Rgb.WHITE_HALF

    class Recording(object):
        Off = Rgb.WHITE_HALF

    class Transport(object):
        PlayOff = Rgb.WHITE_HALF
        PlayOn = Rgb.GREEN
        ContinueOff = Rgb.AQUA
        ContinueOn = Rgb.RED_HALF
        CaptureOff = Rgb.BLACK
        CaptureOn = Rgb.CREAM
        TapTempo = Rgb.CREAM

    class Quantization(object):
        Off = Rgb.RED_HALF
        On = Rgb.AQUA


skin = merge_skins(base_skin, Skin(Colors)*())