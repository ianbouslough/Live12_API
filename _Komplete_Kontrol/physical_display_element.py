# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
# [Clang 6.0 (clang-600.0.57)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/_Komplete_Kontrol/physical_display_element.py
# Compiled at: 2023-12-06 17:21:23
# Size of source mod 2**32: 647 bytes
from __future__ import absolute_import, print_function, unicode_literals
from builtins import str
from itertools import chain
from ableton.v2.control_surface.elements import PhysicalDisplayElement as PhysicalDisplayElementBase

class PhysicalDisplayElement(PhysicalDisplayElementBase):

    def _build_display_message(self, display):
        return chain(*map(lambda x: self._translate_string(str(x).strip())
, display._logical_segments))

    def _request_send_message(self):
        self._send_message()