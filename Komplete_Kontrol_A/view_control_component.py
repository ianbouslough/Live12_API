# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
# [Clang 6.0 (clang-600.0.57)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Komplete_Kontrol_A/view_control_component.py
# Compiled at: 2023-12-06 17:21:23
# Size of source mod 2**32: 868 bytes
from __future__ import absolute_import, print_function, unicode_literals
import Live
from ableton.v2.control_surface import Component
from ableton.v2.control_surface.control import EncoderControl
NavDirection = Live.Application.Application.View.NavDirection

class ViewControlComponent(Component):
    vertical_encoder = EncoderControl()
    horizontal_encoder = EncoderControl()

    @vertical_encoder.value
    def vertical_encoder(self, value, _):
        direction = NavDirection.up if value < 0 else NavDirection.down
        self.application.view.scroll_view(direction, '', False)

    @horizontal_encoder.value
    def horizontal_encoder(self, value, _):
        direction = NavDirection.left if value < 0 else NavDirection.right
        self.application.view.scroll_view(direction, '', False)