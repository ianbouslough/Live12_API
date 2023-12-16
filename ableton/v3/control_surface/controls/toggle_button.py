# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
# [Clang 6.0 (clang-600.0.57)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/control_surface/controls/toggle_button.py
# Compiled at: 2023-12-06 17:21:23
# Size of source mod 2**32: 1317 bytes
from __future__ import absolute_import, print_function, unicode_literals
from . import ButtonControl, Connectable, control_event

class ToggleButtonControl(ButtonControl):
    toggled = control_event('toggled')

    class State(ButtonControl.State, Connectable):
        requires_listenable_connected_property = True

        def connect_property(self, *a):
            (super().connect_property)(*a)
            self.is_on = self.connected_property_value

        def on_connected_property_changed(self, value):
            self.is_on = value

        def _on_pressed(self):
            super()._on_pressed()
            self.is_on = not self._is_on
            self._call_listener('toggled', self.is_on)
            self.connected_property_value = self.is_on