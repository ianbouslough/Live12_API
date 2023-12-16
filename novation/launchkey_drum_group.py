# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
# [Clang 6.0 (clang-600.0.57)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/novation/launchkey_drum_group.py
# Compiled at: 2023-11-21 04:17:31
# Size of source mod 2**32: 2118 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.base import listens, liveobj_valid
from ableton.v2.control_surface.components import PlayableComponent
from .drum_group import DrumGroupComponent as DrumGroupComponentBase
from .util import get_midi_color_value_for_track

class DrumGroupComponent(DrumGroupComponentBase):

    def __init__(self, *a, **k):
        (super(DrumGroupComponent, self).__init__)(*a, **k)
        self._track = None
        self._track_color = 0

    def set_parent_track(self, track):
        self._track = track
        self._DrumGroupComponent__on_track_color_changed.subject = track if liveobj_valid(track) else None
        self._DrumGroupComponent__on_track_color_changed()

    def set_drum_group_device(self, drum_group_device):
        super(DrumGroupComponent, self).set_drum_group_device(drum_group_device)
        if not liveobj_valid(self._drum_group_device):
            self._update_assigned_drum_pads()
            self._update_led_feedback()

    def can_scroll_page_up(self):
        if not liveobj_valid(self._drum_group_device):
            return False
        return super(DrumGroupComponent, self).can_scroll_page_up()

    def _update_led_feedback(self):
        PlayableComponent._update_led_feedback(self)

    def _update_button_color(self, button):
        pad = self._pad_for_button(button)
        color = self._color_for_pad(pad) if pad else self._track_color
        if color in ('DrumGroup.PadFilled', 'DrumGroup.PadEmpty'):
            if liveobj_valid(self._track):
                color = self._track_color
        button.color = color

    @listens('color')
    def __on_track_color_changed(self):
        self._track_color = get_midi_color_value_for_track(self._track)
        self._update_led_feedback()