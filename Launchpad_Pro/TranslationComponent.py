# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
# [Clang 6.0 (clang-600.0.57)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launchpad_Pro/TranslationComponent.py
# Compiled at: 2023-12-06 17:21:23
# Size of source mod 2**32: 1491 bytes
from __future__ import absolute_import, print_function, unicode_literals
from builtins import range
from functools import partial
import _Framework.ControlSurfaceComponent as ControlSurfaceComponent

class TranslationComponent(ControlSurfaceComponent):

    def __init__(self, translated_channel, should_enable=True, should_reset=True, *a, **k):
        self._translated_channel = translated_channel
        self._should_enable = bool(should_enable)
        self._should_reset = should_reset
        (super(TranslationComponent, self).__init__)(*a, **k)

    def __getattr__(self, name):
        if len(name) > 4:
            if name[:4] == 'set_':
                return partial(self._set_control_elements, name[4:])
        raise AttributeError(name)

    def _set_control_elements(self, name, control_elements):
        if bool(control_elements):
            buttons = control_elements
            for button in buttons:
                if button:
                    if self._should_reset:
                        button.reset()
                    else:
                        button.reset_state()
                    button.set_enabled(self._should_enable)
                    button.set_channel(self._translated_channel)