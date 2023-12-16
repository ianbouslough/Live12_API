# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
# [Clang 6.0 (clang-600.0.57)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Push2/sliced_simpler.py
# Compiled at: 2023-11-21 04:17:31
# Size of source mod 2**32: 734 bytes
from __future__ import absolute_import, print_function, unicode_literals
from pushbase.colors import Pulse
from pushbase.sliced_simpler_component import SlicedSimplerComponent
from .colors import IndexedColor
NEXT_SLICE_PULSE_SPEED = 48

def next_slice_color(track_color_index):
    return Pulse(color1=IndexedColor.from_live_index(track_color_index, shade_level=2),
      color2=IndexedColor.from_live_index(track_color_index, shade_level=1),
      speed=NEXT_SLICE_PULSE_SPEED)


class Push2SlicedSimplerComponent(SlicedSimplerComponent):

    def _next_slice_color(self):
        return next_slice_color(self.song.view.selected_track.color_index)