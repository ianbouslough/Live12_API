# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
# [Clang 6.0 (clang-600.0.57)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launchpad_Pro_MK3/channel_strip.py
# Compiled at: 2023-11-21 04:17:31
# Size of source mod 2**32: 851 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.base import liveobj_valid
from novation.channel_strip import ChannelStripComponent as ChannelStripComponentBase

class ChannelStripComponent(ChannelStripComponentBase):

    def _track_color_changed(self):
        super(ChannelStripComponent, self)._track_color_changed()
        self._update_select_button()

    def _update_select_button(self):
        if liveobj_valid(self._track) or self.empty_color is None:
            if self.song.view.selected_track == self._track:
                self.select_button.color = self._track_color_value
            else:
                self.select_button.color = 'Mixer.TrackNotSelected'
        else:
            self.select_button.color = self.empty_color