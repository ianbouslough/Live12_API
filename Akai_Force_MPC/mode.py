# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
# [Clang 6.0 (clang-600.0.57)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Akai_Force_MPC/mode.py
# Compiled at: 2023-11-21 04:17:31
# Size of source mod 2**32: 630 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.mode import Mode

class ExtendComboElementMode(Mode):

    def __init__(self, combo_pairs=None, *a, **k):
        (super(ExtendComboElementMode, self).__init__)(*a, **k)
        self._combo_pairs = combo_pairs

    def enter_mode(self):
        for combo, nested in self._combo_pairs:
            combo.register_control_element(nested)

    def leave_mode(self):
        for combo, nested in self._combo_pairs:
            combo.unregister_control_element(nested)