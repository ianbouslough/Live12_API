# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
# [Clang 6.0 (clang-600.0.57)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Komplete_Kontrol_S_Mk3/midi.py
# Compiled at: 2023-12-06 17:21:23
# Size of source mod 2**32: 1056 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v3.control_surface.midi import SYSEX_START
MIDI_CHANNEL = 15
SYSEX_HEADER = (
 SYSEX_START, 0, 33, 9, 0, 0, 68, 67, 1, 0)
FOCUS_FOLLOW_HEADER = SYSEX_HEADER + (65, 0, 0)
TRACK_TYPE_HEADER = SYSEX_HEADER + (64, )
TRACK_SELECT_HEADER = SYSEX_HEADER + (66, )
TRACK_MUTE_HEADER = SYSEX_HEADER + (67, )
TRACK_SOLO_HEADER = SYSEX_HEADER + (68, )
TRACK_ARM_HEADER = SYSEX_HEADER + (69, )
TRACK_VOLUME_HEADER = SYSEX_HEADER + (70, 0)
TRACK_PAN_HEADER = SYSEX_HEADER + (71, 0)
TRACK_NAME_HEADER = SYSEX_HEADER + (72, 0)
TRACK_METER_HEADER = SYSEX_HEADER + (73, 2, 0)
TRACK_MUTE_VIA_SOLO_HEADER = SYSEX_HEADER + (74, )
DEFAULT_TRACK_TYPE = 1
MASTER_TRACK_TYPE = 6