# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
# [Clang 6.0 (clang-600.0.57)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/SL_MkIII/util.py
# Compiled at: 2023-12-06 17:21:23
# Size of source mod 2**32: 1118 bytes
from __future__ import absolute_import, print_function, unicode_literals
from past.utils import old_div
from ableton.v2.base import clamp, liveobj_valid
from ableton.v2.control_surface.components import find_nearest_color
from ableton.v2.control_surface.elements import Color
from novation.colors import CLIP_COLOR_TABLE, RGB_COLOR_TABLE

def normalized_parameter_value(param):
    value = 0.0
    if liveobj_valid(param):
        param_range = param.max - param.min
        value = old_div(float(param.value - param.min), param_range)
    return clamp(value, 0.0, 1.0)


def convert_parameter_value_to_midi_value(param):
    return int(normalized_parameter_value(param) * 127)


def is_song_recording(song):
    return song.session_record or song.record_mode


def color_for_track(track):
    color_value = 0
    if liveobj_valid(track):
        try:
            color_value = CLIP_COLOR_TABLE[track.color]
        except (KeyError, IndexError):
            color_value = find_nearest_color(RGB_COLOR_TABLE, track.color)

        return Color(color_value)