# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
# [Clang 6.0 (clang-600.0.57)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Novation_Impulse/ShiftableTransportComponent.py
# Compiled at: 2023-12-06 17:21:23
# Size of source mod 2**32: 2942 bytes
from __future__ import absolute_import, print_function, unicode_literals
from builtins import range
import Live
import _Framework.ButtonElement as ButtonElement
import _Framework.TransportComponent as TransportComponent

class ShiftableTransportComponent(TransportComponent):

    def __init__(self):
        self._shift_button = None
        self._shift_pressed = False
        TransportComponent.__init__(self)

    def disconnect(self):
        if self._shift_button != None:
            self._shift_button.remove_value_listener(self._shift_value)
            self._shift_button = None
        TransportComponent.disconnect(self)

    def set_shift_button(self, button):
        if self._shift_button != button:
            if self._shift_button != None:
                self._shift_button.remove_value_listener(self._shift_value)
                self._shift_pressed = False
            self._shift_button = button
            if self._shift_button != None:
                self._shift_button.add_value_listener(self._shift_value)

    def _shift_value(self, value):
        if self.is_enabled():
            self._shift_pressed = value > 0

    def _ffwd_value(self, value):
        if self._shift_pressed:
            self.song().current_song_time = self.song().last_event_time
        else:
            TransportComponent._ffwd_value(self, value)

    def _rwd_value(self, value):
        if self._shift_pressed:
            self.song().current_song_time = 0.0
        else:
            TransportComponent._rwd_value(self, value)