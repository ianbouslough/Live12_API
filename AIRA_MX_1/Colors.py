# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
# [Clang 6.0 (clang-600.0.57)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/AIRA_MX_1/Colors.py
# Compiled at: 2023-12-07 14:24:09
# Size of source mod 2**32: 589 bytes
from __future__ import absolute_import, print_function, unicode_literals
from _Framework.ButtonElement import Color
BLINK_LED_CHANNEL = 14

class Blink(Color):

    def draw(self, interface):
        interface.send_value(self.midi_value)
        interface.send_value(0, channel=BLINK_LED_CHANNEL)


class Rgb:
    BLACK = Color(0)
    RED = Color(5)
    RED_BLINK = Blink(5)
    GREEN_HALF = Color(20)
    GREEN = Color(21)
    GREEN_BLINK = Blink(21)
    BLUE_HALF = Color(44)
    BLUE = Color(45)
    BLUE_BLINK = Blink(45)