# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
# [Clang 6.0 (clang-600.0.57)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/KeyLab_Essential/transport.py
# Compiled at: 2023-12-06 17:21:23
# Size of source mod 2**32: 1804 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.components import ToggleComponent
from ableton.v2.control_surface.components import TransportComponent as TransportComponentBase
from ableton.v2.control_surface.control import ButtonControl

class TransportComponent(TransportComponentBase):
    play_button = ButtonControl()

    def __init__(self, *a, **k):
        (super(TransportComponent, self).__init__)(*a, **k)
        self._punch_in_toggle = ToggleComponent('punch_in', (self.song), parent=self)
        self._punch_out_toggle = ToggleComponent('punch_out', (self.song), parent=self)

    def set_play_button(self, button):
        self.play_button.set_control_element(button)
        self._update_play_button_color()

    def _update_button_states(self):
        self._update_play_button_color()
        self._update_stop_button_color()

    def _update_play_button_color(self):
        self.play_button.color = 'Transport.PlayOn' if self.song.is_playing else 'Transport.PlayOff'

    def _update_stop_button_color(self):
        self.stop_button.color = 'Transport.StopOff' if self.song.is_playing else 'Transport.StopOn'

    @play_button.pressed
    def play_button(self, _):
        if not self.song.is_playing:
            self.song.is_playing = True

    def _ffwd_value(self, value):
        super(TransportComponent, self)._ffwd_value(value)
        self._ffwd_button.set_light('DefaultButton.On' if value else 'DefaultButton.Off')

    def _rwd_value(self, value):
        super(TransportComponent, self)._rwd_value(value)
        self._rwd_button.set_light('DefaultButton.On' if value else 'DefaultButton.Off')