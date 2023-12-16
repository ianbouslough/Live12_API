# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
# [Clang 6.0 (clang-600.0.57)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launchkey_MK2/BackgroundComponent.py
# Compiled at: 2023-11-21 04:17:31
# Size of source mod 2**32: 537 bytes
from __future__ import absolute_import, print_function, unicode_literals
from _Framework.BackgroundComponent import BackgroundComponent as BackgroundComponentBase

class BackgroundComponent(BackgroundComponentBase):

    def _clear_control(self, name, control):
        super(BackgroundComponent, self)._clear_control(name, control)
        if control:
            control.add_value_listener(self._on_value_listener)

    def _on_value_listener(self, *a, **k):
        pass