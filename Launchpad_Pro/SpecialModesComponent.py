# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
# [Clang 6.0 (clang-600.0.57)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launchpad_Pro/SpecialModesComponent.py
# Compiled at: 2023-12-06 17:21:23
# Size of source mod 2**32: 2098 bytes
from __future__ import absolute_import, print_function, unicode_literals
from _Framework.ModesComponent import ModesComponent, ReenterBehaviour

class SpecialModesComponent(ModesComponent):

    def on_enabled_changed(self):
        super(SpecialModesComponent, self).on_enabled_changed()
        if not self.is_enabled():
            self._last_selected_mode = None


class SpecialReenterBehaviour(ReenterBehaviour):

    def __init__(self, mode_name=None, *a, **k):
        (super(ReenterBehaviour, self).__init__)(*a, **k)
        self._mode_name = mode_name

    def press_immediate(self, component, mode):
        was_active = component.selected_mode == mode
        super(ReenterBehaviour, self).press_immediate(component, mode)
        if was_active:
            if self._mode_name is not None:
                if component.get_mode(self._mode_name):
                    component.push_mode(self._mode_name)
                    component.pop_unselected_modes()


class CancelingReenterBehaviour(SpecialReenterBehaviour):

    def __init__(self, *a, **k):
        (super(CancelingReenterBehaviour, self).__init__)(*a, **k)
        self._reenter_mode_active = False

    def press_immediate(self, component, mode):
        was_active = component.selected_mode == mode
        super(CancelingReenterBehaviour, self).press_immediate(component, mode)
        if was_active:
            self._reenter_mode_active = True

    def release_immediate(self, component, mode):
        super(CancelingReenterBehaviour, self).release_immediate(component, mode)
        self._return(component, mode)

    def release_delayed(self, component, mode):
        super(CancelingReenterBehaviour, self).release_delayed(component, mode)
        self._return(component, mode)

    def _return(self, component, mode):
        if self._reenter_mode_active:
            component.push_mode(mode)
            component.pop_unselected_modes()
            self._reenter_mode_active = False