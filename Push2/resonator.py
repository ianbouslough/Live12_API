# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
# [Clang 6.0 (clang-600.0.57)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Push2/resonator.py
# Compiled at: 2023-12-06 17:21:23
# Size of source mod 2**32: 1238 bytes
from __future__ import absolute_import, print_function, unicode_literals
from enum import IntEnum
from ableton.v2.base import EventObject
from ableton.v2.control_surface import LiveObjectDecorator

class ResonatorDeviceDecorator(LiveObjectDecorator, EventObject):

    class Select(IntEnum):
        pitch = 0
        finetune = 1
        gain = 2

    def __init__(self, *a, **k):
        (super(ResonatorDeviceDecorator, self).__init__)(*a, **k)
        self._add_enum_parameter(name='Select',
          values=[
         'Pitch', 'Fine Tune', 'Gain'],
          default_value=(self.Select.pitch))
        self._add_on_off_option(name='Filter', pname='Filter On')
        self._add_on_off_option(name='Constant', pname='Const')
        self._add_on_off_option(name='I', pname='I On')
        self._add_on_off_option(name='II', pname='II On')
        self._add_on_off_option(name='III', pname='III On')
        self._add_on_off_option(name='IV', pname='IV On')
        self._add_on_off_option(name='V', pname='V On')
        self._add_switch_option(name='Mode', pname='Mode', labels=['Mode B', 'Mode A'])
        self.register_disconnectables(self.options)