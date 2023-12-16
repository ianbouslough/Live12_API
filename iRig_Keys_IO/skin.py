# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
# [Clang 6.0 (clang-600.0.57)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/iRig_Keys_IO/skin.py
# Compiled at: 2023-12-06 17:21:23
# Size of source mod 2**32: 708 bytes
from __future__ import absolute_import, print_function, unicode_literals
from builtins import object
from ableton.v2.control_surface import Skin
from ableton.v2.control_surface.elements import Color

class Colors(object):

    class DefaultButton(object):
        On = Color(0)
        Off = Color(0)
        Disabled = Color(0)

    class Transport(object):
        PlayOn = Color(0)
        PlayOff = Color(0)

    class Recording(object):
        On = Color(0)
        Off = Color(0)

    class Mixer(object):
        MuteOff = Color(127)
        MuteOn = Color(0)
        SoloOn = Color(127)
        SoloOff = Color(0)


skin = Skin(Colors)