# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
# [Clang 6.0 (clang-600.0.57)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launch_Control/DeviceNavigationComponent.py
# Compiled at: 2023-11-21 04:17:31
# Size of source mod 2**32: 1659 bytes
from __future__ import absolute_import, print_function, unicode_literals
import Live
import _Framework.ControlSurfaceComponent as ControlSurfaceComponent
from _Framework.SubjectSlot import subject_slot

class DeviceNavigationComponent(ControlSurfaceComponent):
    _next_button = None
    _previous_button = None

    def set_next_device_button(self, button):
        self._next_button = button
        self._update_button_states()
        self._on_next_device.subject = button

    def set_previous_device_button(self, button):
        self._previous_button = button
        self._update_button_states()
        self._on_previous_device.subject = button

    @subject_slot('value')
    def _on_next_device(self, value):
        if value:
            self._scroll_device_view(Live.Application.Application.View.NavDirection.right)

    @subject_slot('value')
    def _on_previous_device(self, value):
        if value:
            self._scroll_device_view(Live.Application.Application.View.NavDirection.left)

    def _scroll_device_view(self, direction):
        self.application().view.show_view('Detail')
        self.application().view.show_view('Detail/DeviceChain')
        self.application().view.scroll_view(direction, 'Detail/DeviceChain', False)

    def _update_button_states(self):
        if self._next_button:
            self._next_button.turn_on()
        if self._previous_button:
            self._previous_button.turn_on()

    def update(self):
        super(DeviceNavigationComponent, self).update()
        if self.is_enabled():
            self._update_button_states()