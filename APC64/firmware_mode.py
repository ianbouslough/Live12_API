# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
# [Clang 6.0 (clang-600.0.57)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/APC64/firmware_mode.py
# Compiled at: 2023-12-06 17:21:23
# Size of source mod 2**32: 1663 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v3.control_surface.elements import SysexElement

class FirmwareModeElement(SysexElement):

    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        self._suppress_next_send_value = False

    def receive_value(self, value):
        self._suppress_next_send_value = True
        super().receive_value(value)

    def send_value(self, *a, **k):
        if self._suppress_next_send_value:
            self._suppress_next_send_value = False
            return
        (super().send_value)(*a, **k)

    def clear_send_cache(self):
        self._suppress_next_send_value = True