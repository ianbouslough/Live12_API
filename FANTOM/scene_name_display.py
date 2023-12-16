# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
# [Clang 6.0 (clang-600.0.57)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/FANTOM/scene_name_display.py
# Compiled at: 2023-12-06 17:21:23
# Size of source mod 2**32: 705 bytes
from __future__ import absolute_import, print_function, unicode_literals
from .simple_display import SimpleDisplayElement, adjust_string, as_ascii
from .sysex import NAME_LENGTH, NAME_TERMINATOR

class SceneNameDisplayElement(SimpleDisplayElement):

    def display_data(self, data):
        data_to_send = [
         len(data)]
        for scene in data:
            data_to_send.extend(as_ascii(adjust_string(scene.name, NAME_LENGTH).strip()))
            data_to_send.append(NAME_TERMINATOR)

        self._message_to_send = self._message_header + tuple(data_to_send) + self._message_tail
        self._request_send_message()