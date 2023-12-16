# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
# [Clang 6.0 (clang-600.0.57)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/_APC/MixerComponent.py
# Compiled at: 2023-12-06 17:21:23
# Size of source mod 2**32: 1927 bytes
from __future__ import absolute_import, print_function, unicode_literals
from _Framework.ChannelStripComponent import ChannelStripComponent as ChannelStripComponentBase
from _Framework.MixerComponent import MixerComponent as MixerComponentBase
TRACK_FOLD_DELAY = 5

class ChanStripComponent(ChannelStripComponentBase):

    def __init__(self, *a, **k):
        (super(ChanStripComponent, self).__init__)(*a, **k)
        self._toggle_fold_ticks_delay = -1
        self._register_timer_callback(self._on_timer)

    def disconnect(self):
        self._unregister_timer_callback(self._on_timer)
        super(ChanStripComponent, self).disconnect()

    def _select_value(self, value):
        super(ChanStripComponent, self)._select_value(value)
        if self.is_enabled():
            if self._track != None:
                if self._track.is_foldable and self._select_button.is_momentary() and value != 0:
                    self._toggle_fold_ticks_delay = TRACK_FOLD_DELAY
                else:
                    self._toggle_fold_ticks_delay = -1

    def _on_timer(self):
        if self.is_enabled():
            if self._track != None:
                if self._toggle_fold_ticks_delay > -1:
                    if self._toggle_fold_ticks_delay == 0:
                        self._track.fold_state = not self._track.fold_state
                    self._toggle_fold_ticks_delay -= 1


class MixerComponent(MixerComponentBase):

    def tracks_to_use(self):
        return tuple(self.song().visible_tracks) + tuple(self.song().return_tracks)

    def _create_strip(self):
        return ChanStripComponent()