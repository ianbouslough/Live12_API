# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
# [Clang 6.0 (clang-600.0.57)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Push2/graindelay.py
# Compiled at: 2023-12-06 17:21:23
# Size of source mod 2**32: 561 bytes
from __future__ import absolute_import, print_function, unicode_literals
from enum import IntEnum
from ableton.v2.base import EventObject, liveobj_valid
from ableton.v2.control_surface import LiveObjectDecorator

class GrainDelayDeviceDecorator(LiveObjectDecorator, EventObject):

    def __init__(self, *a, **k):
        (super(GrainDelayDeviceDecorator, self).__init__)(*a, **k)
        self._add_on_off_option(name='Sync', pname='Delay Mode')
        self.register_disconnectables(self.options)