# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
# [Clang 6.0 (clang-600.0.57)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/MiniLab_3/sysex.py
# Compiled at: 2023-12-06 17:21:23
# Size of source mod 2**32: 1329 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v3.control_surface.elements import SysexElement as SysexElementBase
from .midi import COMMAND_ID_TO_DAW_PROGRAM_ID

class SysexElement(SysexElementBase):

    def receive_value(self, value):
        if len(value) == 2:
            if value[0] in COMMAND_ID_TO_DAW_PROGRAM_ID:
                super().receive_value(int(value[1] == COMMAND_ID_TO_DAW_PROGRAM_ID[value[0]]))