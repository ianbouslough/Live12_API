# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
# [Clang 6.0 (clang-600.0.57)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launchkey_MK3/clip_actions.py
# Compiled at: 2023-12-06 17:21:23
# Size of source mod 2**32: 1289 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.base import depends, liveobj_valid
from ableton.v2.control_surface import Component
from ableton.v2.control_surface.control import ButtonControl

class ClipActionsComponent(Component):
    is_private = True
    quantize_button = ButtonControl()

    @depends(quantization_component=None)
    def __init__(self, quantization_component=None, *a, **k):
        (super().__init__)(*a, **k)
        self._quantization_component = quantization_component
        self.register_slot(self.song.view, self._update_quantize_button, 'detail_clip')
        self._update_quantize_button()

    @quantize_button.pressed
    def quantize_button(self, _):
        self._quantization_component.quantize_clip(self.song.view.detail_clip)

    def _update_quantize_button(self):
        self.quantize_button.enabled = liveobj_valid(self.song.view.detail_clip)