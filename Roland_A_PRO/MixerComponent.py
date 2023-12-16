# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
# [Clang 6.0 (clang-600.0.57)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Roland_A_PRO/MixerComponent.py
# Compiled at: 2023-12-06 17:21:23
# Size of source mod 2**32: 1310 bytes
from __future__ import absolute_import, print_function, unicode_literals
from _Framework.Control import ButtonControl
from _Framework.MixerComponent import MixerComponent as MixerComponentBase

class MixerComponent(MixerComponentBase):
    bank_up_button = ButtonControl()
    bank_down_button = ButtonControl()
    track_up_button = ButtonControl()
    track_down_button = ButtonControl()

    def __init__(self, *a, **k):
        (super(MixerComponent, self).__init__)(*a, **k)

    @bank_up_button.pressed
    def bank_up_button_pressed(self, button):
        new_offset = self._track_offset + len(self._channel_strips)
        if len(self.tracks_to_use()) > new_offset:
            self.set_track_offset(new_offset)

    @bank_down_button.pressed
    def bank_down_button_pressed(self, button):
        self.set_track_offset(max(0, self._track_offset - len(self._channel_strips)))

    @track_up_button.pressed
    def track_up_button_pressed(self, button):
        new_offset = self._track_offset + 1
        if len(self.tracks_to_use()) > new_offset:
            self.set_track_offset(new_offset)

    @track_down_button.pressed
    def track_down_button_pressed(self, button):
        self.set_track_offset(max(0, self._track_offset - 1))