# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
# [Clang 6.0 (clang-600.0.57)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Push/drum_group_component.py
# Compiled at: 2023-11-21 04:17:31
# Size of source mod 2**32: 508 bytes
from __future__ import absolute_import, print_function, unicode_literals
from pushbase.drum_group_component import DrumGroupComponent as DrumGroupComponentBase

class DrumGroupComponent(DrumGroupComponentBase):

    def __init__(self, selector=None, *a, **k):
        (super(DrumGroupComponent, self).__init__)(*a, **k)
        self._selector = selector

    def select_drum_pad(self, drum_pad):
        self._selector.on_select_drum_pad(drum_pad)