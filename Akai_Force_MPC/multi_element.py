# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
# [Clang 6.0 (clang-600.0.57)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Akai_Force_MPC/multi_element.py
# Compiled at: 2023-12-06 17:21:23
# Size of source mod 2**32: 1063 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.base import old_hasattr
from ableton.v2.control_surface.elements import MultiElement as MultiElementBase

class MultiElement(MultiElementBase):

    def __init__(self, *a, **k):
        (super(MultiElement, self).__init__)(*a, **k)
        self._parameter_to_map_to = None

    @property
    def touch_element(self):
        for control in self.owned_control_elements():
            if old_hasattr(control, 'touch_element'):
                return control.touch_element

    def connect_to(self, parameter):
        self._parameter_to_map_to = parameter
        for control in self.owned_control_elements():
            control.connect_to(parameter)

    def release_parameter(self):
        self._parameter_to_map_to = None
        for control in self.owned_control_elements():
            control.release_parameter()

    def mapped_parameter(self):
        return self._parameter_to_map_to