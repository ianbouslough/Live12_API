# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
# [Clang 6.0 (clang-600.0.57)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/pushbase/pad_button_element.py
# Compiled at: 2023-11-21 04:17:31
# Size of source mod 2**32: 1419 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.base import const
from ableton.v2.control_surface.elements import ButtonElement

class PadButtonElement(ButtonElement):

    class ProxiedInterface(ButtonElement.ProxiedInterface):
        sensitivity_profile = const(None)

    def __init__(self, pad_id=None, pad_sensitivity_update=None, *a, **k):
        (super(PadButtonElement, self).__init__)(*a, **k)
        self._sensitivity_profile = 'default'
        self._pad_id = pad_id
        self._pad_sensitivity_update = pad_sensitivity_update

    def _get_sensitivity_profile(self):
        return self._sensitivity_profile

    def _set_sensitivity_profile(self, profile):
        if profile != self._sensitivity_profile:
            if self._pad_sensitivity_update is not None:
                self._sensitivity_profile = profile
                self._pad_sensitivity_update.set_pad(self._pad_id, profile)

    sensitivity_profile = property(_get_sensitivity_profile, _set_sensitivity_profile)

    def reset(self):
        self.sensitivity_profile = 'default'
        super(PadButtonElement, self).reset()