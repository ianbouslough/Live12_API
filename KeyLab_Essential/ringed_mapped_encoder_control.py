# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
# [Clang 6.0 (clang-600.0.57)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/KeyLab_Essential/ringed_mapped_encoder_control.py
# Compiled at: 2023-11-21 04:17:31
# Size of source mod 2**32: 797 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.base import listens
from ableton.v2.control_surface.control import MappedControl

class RingedMappedEncoderControl(MappedControl):

    class State(MappedControl.State):

        def _update_direct_connection(self):
            super(RingedMappedEncoderControl.State, self)._update_direct_connection()
            self._on_parameter_value.subject = self._direct_mapping
            if self._direct_mapping:
                self._on_parameter_value()

        @listens('value')
        def _on_parameter_value(self):
            if self._control_element:
                if self.enabled:
                    self._control_element.set_ring_value(self._direct_mapping)