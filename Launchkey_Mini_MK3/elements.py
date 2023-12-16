# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
# [Clang 6.0 (clang-600.0.57)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launchkey_Mini_MK3/elements.py
# Compiled at: 2023-12-06 17:21:23
# Size of source mod 2**32: 662 bytes
from __future__ import absolute_import, print_function, unicode_literals
from builtins import object, range
from novation.launchkey_elements import LaunchkeyElements

class Elements(LaunchkeyElements):

    def __init__(self, *a, **k):
        (super(Elements, self).__init__)(*a, **k)
        self.record_button_with_shift = self.with_shift(self.record_button)
        self.scene_launch_button_with_shift = self.with_shift(self.scene_launch_buttons_raw[0])
        self.stop_solo_mute_button_with_shift = self.with_shift(self.scene_launch_buttons_raw[1])